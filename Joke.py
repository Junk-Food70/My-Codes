import requests 

def get_random_joke():
    # Fetch a random joke from official Joke API.
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    
    if response.status_code == 200:
        # One line to print the JSON response:
        print(f"Full JSON Response: {response.json()}")
        
        joke_data = response.json()
        return f"{joke_data['setup']} {joke_data['punchline']}"
    else:
        return "Failed to retrieve joke."
    
def main():
    print("Welcoe to Random Joke Generator!")
    
    while True:
        user_input = input("Press Enter to get a random joke, or type 'q'/'exit' to quit:").strip().lower()
        
        if user_input == 'q' or user_input == 'exit':
            print("Goodbye!")
            break
        
        joke = get_random_joke()
        print(f"\nRandom Joke: {joke}\n")
        
if __name__ == "__main__":
    main()