# Simple Rule-Based Chatbot

print("🤖 Hello! I am a simple chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    # Greeting
    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you today?")

    # Asking name
    elif "your name" in user_input:
        print("Bot: My name is RuleBot 😊")

    # Asking how are you
    elif "how are you" in user_input:

        print("Bot: I'm just a program, but I'm doing great!")

    # Asking about weather
    elif "weather" in user_input:
        print("Bot: I can't check real weather, but I hope it's nice outside!")

    # Asking about time
    elif "time" in user_input:
        print("Bot: Sorry, I can't tell the exact time right now.")

    # Exit condition
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a great day! 👋")
        break

    # Default response
    else:
        print("Bot: I'm sorry, I don't understand that.")

