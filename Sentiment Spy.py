import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN} Welcome Sentiment Spy!{Style.RESET_ALL}")
while True:
    user_input = input("Please enter something")
    if not user_input:
        print(f"{Fore.RED} Please enter some text or a valid sentence.{Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE} Exiting Sentiment Spy")
        break
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
    elif polarity > 0.25:
       sentiment_type = "Positive"
       color = Fore.GREEN
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
    
    print(f"{color}{sentiment_type} Sentiment detected!"
          f"(Polarity:{polarity:.2f}) {Style.RESET_ALL}")
    

