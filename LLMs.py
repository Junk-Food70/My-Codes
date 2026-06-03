import requests
HF_API_KEY = "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"
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# Default model name can be easily changed
DEFAULT_MODEL_NAME = "google/pegasus-xsum"

def build_api_url(model_name):
    return f"https://api-inference.huggingface.co/models/{model_name}"

def query(payload, model_name=DEFAULT_MODEL_NAME):
    
    """
    
    Sends a PoST request to the Hugging Face API with the given payload and model name.
    
    """
    
    api_url = build_api_url(model_name)
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()

def summarize_text (text, min_length, max_length, model_name=DEFAULT_MODEL_NAME):
    
    """
    
    Summarizes the given text using the specified model and length parameters.
    
    """
    
    payload = {
        
        "inputs": text,
        
        "parameters": {"min_length": min_length, "max_length": max_length}
    }
    print(Fore.BLUE + Style.BRIGHT + f"\n???? Performing AI summarisation with using model: {model_name}")
    
    result = query(payload, model_name=model_name)
    
    # Check if the response has the expected structure
    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print(Fore.RED + Style.BRIGHT + f"\n!!!! Error: Failed to summarize text with model:", result)
        return None
    

if __name__ == "__main__":
    
    # Ask for the user's name
    
    print(Fore.YELLOW + Style.BRIGHT + "???? Hi there! What is your name?")
    user_name = input("Your name:").strip()
    if not user_name:
        user_name = "User"
        
    print(Fore.GREEN + Style.BRIGHT + f"Welcome, {user_name}! Let's give your text some AI magic ✨")
    
    # Prompt the user for the text input
    
    print(Fore.YELLOW + Style.BRIGHT + "???? Please enter the text you want to summarize:")
    user_text = input("Please enter a text:").strip()
    if not user_text:
        print(Fore.RED + Style.BRIGHT + "No text entered. Exiting.")
    else:
        # Ask for the desired summary length
        
        print(Fore.YELLOW + Style.BRIGHT + "???? How long do you want the summary to be? (Enter a number for max length)")
        try:
            max_length = int(input("Max summary length (e.g., 50):").strip())
            min_length = max(10, max_length // 2)  # Set a reasonable minimum length
            summary = summarize_text(user_text, min_length, max_length)
            if summary:
                print(Fore.CYAN + Style.BRIGHT + f"\n???? Here is your AI-generated summary:\n{summary}")
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Invalid input for summary length. Please enter a valid number.")
            