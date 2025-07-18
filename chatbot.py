def rule_based_chatbot():
    print("Bot: Hello! I'm your assistant. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if "bye" in user_input or "exit" in user_input:
            print("Bot: Goodbye! Have a great day 😊")
            break
        
        # Rule-based responses
        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How can I assist you today?")
        
        elif "your name" in user_input:
            print("Bot: I'm a simple rule-based chatbot created to help you.")

        elif "how are you" in user_input:
            print("Bot: I'm just a bunch of code, but thanks for asking!")

        elif "time" in user_input:
            from datetime import datetime
            print(f"Bot: The current time is {datetime.now().strftime('%H:%M:%S')}")

        elif "date" in user_input:
            from datetime import date
            print(f"Bot: Today's date is {date.today().strftime('%B %d, %Y')}")

        elif "help" in user_input:
            print("Bot: I can chat with you, tell the time, date, and share some basic info. Try asking!")

        else:
            print("Bot: I'm not sure how to respond to that. Please ask something else.")

# Run the chatbot
rule_based_chatbot()
