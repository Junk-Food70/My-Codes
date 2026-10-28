from hf import generate_response
import time 

def temperature_prompt_activity():
    print("=" * 70)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE + INSTRUCTIONS")
    print("=" * 70)
    
    print("nPART 1: TEMPERATURE EXPLORATION")
    base = input("Enter a creative prompt:").strip()
    
    for t, label in [(0.1, "LOW (0.1) - Deterministic"), (0.5, "MEDIUM (0.5) - Balanced"), (0.9, "HIGH (0.9) - Creative")]:
        print(f"\n--- {label} ---")
        print(generate_response(base, temperature=t, max_tokens=512))
        time.sleep(1)
        
        
    print("\nPART 2: INSTRUCTIONS-BASED PROMPTS")
    topic = input("Choose a topic (e.g., climate change, AI, space exploration):").strip()
    
    prompts = [
        f"Summarize key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I'm a 10-years-old child.",
        f"Write a pro/con list about {topic}.",
        f"Write a short story about {topic}."
    ]
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\n--- INSTRUCTIONS {i} ---\n{prompt}")
        print(generate_response(prompt, temperature=0.7, max_tokens=512))
        time.sleep(1)
        
        
        print
        ("\nPART 3: YOUR OWN INSTRUCTIONS")
        custom = input("Enter your own instruction-based prompt:").strip()
        try:
            temp = float(input("Enter a temperature value (0.0 to 1.0):").strip())
            if not (0.1 <= temp <= 1.0): raise ValueError
        except ValueError:
                print("Invalid temperature. Temperature must be between 0.1 and 1.0. Using default 0.7.")
                temp = 0.7
                
        print(f"\n--- YOUR PROMPT @ TEMPERATURE {temp} ---")
        print(generate_response(custom, temperature=temp, max_tokens=512))
        
        print("\nREFLECTION:")
        print("1) What changed when prompts became more specific?")
        print("2) What improved when context was added?")
        print("3) Which prompt felt most useful and why?")
        print("\nCHALLENGE: Create a prompt chain:")
        print("Generate content -> rewrite with constraints -> create a sequel (try different temps).")
        
        
def pseudo_stream(text, delay = 0.013):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # New line at the end
    
def bonus_stream():
    choice = input("\nBONUS: streaming-like output? (y/n):").strip().lower()
    if choice == "y":
        prompt = input("Enter a prompt for streaming output:").strip()
        out = generate_response(prompt, temperature=0.7, max_tokens=512)
        print("\nStreaming-like response (not real streaming):")
        pseudo_stream(out)
        
        
if __name__ == "__main__":
    temperature_prompt_activity()
    bonus_stream()