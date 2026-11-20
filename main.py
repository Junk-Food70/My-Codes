from groq import generate_response

def run_activity():
    print("ZERO-SHOT, ONE-SHOT, FEW-SHOT LEARNING ACTIVITY")
    
    category = input("Enter the category (e.g., 'animals', 'fruits', 'countries'): ").strip()
    item = input(f"Enter a specific {category} to classify: ").strip()
    
    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return
    
    zero_shot_prompt = f"Is {item} a {category}? Answer with 'Yes' or 'No'."
    print("\n---- ZERO-SHOT LEARNING ----")
    print(f"Response: {generate_response(zero_shot_prompt, temperature=0.3, max_tokens=1024)}")
    
    one_shot = f""""Example: 
    Category: fruit
    Item: apple 
    Answer: Yes, apple is a fruit.
    
    Now, you try:
    Category: {category} 
    Item: {item}
    Answer: """
    print("\n---- ONE-SHOT LEARNING ----")
    print(f"Response: {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")
    
    #Creative Prompt
    creative_prompt = f"""Write a one-sentence story about the given word.
    
    Example 1: Word: moon 
    Story: The moon lit up the night sky as a little astronaut began an exciting adventure.
    
    Word: {item}
    Story: """
    print("\n---- CREATIVE FEW-SHOT -EXAMPLE---")
    print(f"Response: {generate_response(creative_prompt, temperature=0.7, max_tokens=1024)}")
    
    
    # Reflection questions
    print("\n---- REFLECTION QUESTIONS ----")
    print("1. How did the responses differ between zero-shot, one-shot, and few-shot?")
    print("2. Which approach do you think is more effective for this task and why?")
    print("3. How did the examples influence the model's output?")
    
    
    
if __name__ == "__main__":
    run_activity()