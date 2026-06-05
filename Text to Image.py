from huggingface_hub import InferenceClient 
from datetime import datetime
from PIL import Image
HF_API_KEY = "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"

# MODEEL PRIORITY LIST - Primary model first, fallbacks only if it fails 
MODELS = [
    "ByteDance/SDXL-Lighting"
    "stabilityai/stable-diffusion-xl-base-1.0",
"stabilityai/sdxl-turbo",
"runwayml/stable-diffusion-v1-5", # Fallback 2
]

# Initialize client
client = InferenceClient(api_key=HF_API_KEY)

print(f"Primary model: {MODELS[0]}")
print("Type 'quit' to exit\n")

while True:
    prompt = input("Enter prompt:").strip()
    if prompt.lower() in ["quit", "exit", "q"]:
        break
    if not prompt:
        continue
    
    print("Generating...")
    image = None
    
    # Try each model in order until one succeds
    for model in MODELS:
        try:
            image = client.text_to_image(model=model, inputs=prompt)
            break  #Success! Exit the loop
        except Exception:
            print(f"Executive next...")
            continue
        
        # If we got an image, display it
        if image:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"generated_{timestamp}.png"
            image.save(filename)
            print(f" Saved: {filename}")
            image.show()
            print()
        else:
            print("Error: All models failed to generate an image for the prompt.\n")
        
print("Goodbye!")

        