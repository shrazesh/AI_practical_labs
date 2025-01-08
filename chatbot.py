def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. How can I assist you today?")

    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm just a program, but I'm doing great! How about you?",
        "what is your name": "I'm just a chatbot without a name, but I'm here to assist you!",
        "what is the time": "I can't tell the time, but you can check your device!",
        "what is the date today": "You can check your device for today's date!",
        "bye": "Goodbye! Have a nice day!",
        "exit": "Goodbye! Have a nice day!"
    }

    while True:
        user_input = input("You: ").lower()

        found_response = False
        for key in responses:
            if key in user_input:
                print(f"Chatbot: {responses[key]}")
                found_response = True
                if key == "bye" or key == "exit":
                    return
                break

        if not found_response:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()
