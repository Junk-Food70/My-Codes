import base64, requests
from LLMs import HF_API_KEY

API_URL = ""
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}", "Content-Type": "application/json"} 
MODELS = [ "zai-org/GLM-4.5V", 
          "Qwen/Qwen2.5-VL-72B-Instruct", 
          "Qwen/Qwen2.5-VL-32B-Instruct", 
          "google/gemma-3-27b-it", ]

def data_url(b: bytes) -> str:
    return "data:image/jpeg;base64," + base64.b64encode(b).decode("utf-8")

def extract_err(r: requests.Response) -> str:
    try:
        j = r.json()
        return j.get("error", {}).get("message") or str(j)
    except Exception:
        return (r.text or "").strip() or r.reason or "Requests failed"
    
def box(title: str, lines: list[str], icon: str):
    w = max(30, len(title) + 4, *(len(x) for x in lines)) 
    print("\n" + "" + "-" * (w + 2) + "")
    print(f"| {icon} {title.ljust(w-2)} |")
    print("" + "-" * (w + 2) + "")
    for X in lines:
        print("" + "-" * (w + 2) + "\n")
        
def caption_single_image():
    image_source = input("🖼️ Enter image filename (default: test.jpg):").strip() or "test.jpg"
    try:
        with open(image_source, "rb") as f:
            image_bytes = f.read()
    except Exception as e:
        box("File Error", [f"Could not load: {image_source}", f"Reason: {e}"], "❌")
        return
    
    base = {
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": "Generate a caption for the following image."},
                {"type": "image", "image_url": data_url(image_bytes)}
            ]
        }]
    }
    
    last = None
    for model in MODELS:
        payload = dict(base, model=model)
    
        try: 
            r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=120)
        except requests.RequestException as e:
            last = f"Request failed: {e}"
            continue
    
        if r.status_code != 200:
            last = extract_err(r)
            continue
        try:
            d = r.json()
        except Exception:
            last = "Non-JSON response received from the API."
            continue
        
        cap = (d.get("choices", [{}])[0].get("message", {}).get("content") or "").strip()
        if cap:
            box("Caption Generated",[
                f"🖼️Model: {model}", 
                f"📝Caption: {cap}"], "✅")
            return
        last = "No caption returned from the API."
        
    box("Caption Generation Failed", [f"Reason: {last}"], "❌")
    
def main():
    caption_single_image()
    
if __name__ == "__main__":
    main()