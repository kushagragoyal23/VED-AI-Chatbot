print("===================================")
print("        Welcome to VED 🤖")
print("===================================")
print("Hello! I'm VED.")
print("Your AI Assistant.")
print("Type 'bye' anytime to exit.")
print("===================================")

while True:

    user = input("You: ").lower()

    if user == "hi":
        print("👋 Hi! I'm VED. How can I help you today?")

    elif user == "hello":
        print("👋 Hello! Nice to meet you.")

    elif user == "what is your name":
        print("🤖 I'm VED, your AI Assistant.")

    elif user == "who created you":
        print("🚀 I was created by Kushagra Goyal and built under GOYAL DIGITAL LABS as part of the AI Internship at DecodeLabs.")
        
    elif user == "how are you":
        print("😊 I'm doing great! Thanks for asking.")

    elif user == "what can you do":
        print("🤖 I can answer simple questions and chat with you.")

    elif user == "thank you":
        print("😊 You're welcome!")

    elif user == "good morning":
        print("🌞 Good Morning! Have a productive day.")

    elif user == "good night":
        print("🌙 Good Night! Sweet dreams.")

    elif user == "bye":
        print("👋 Goodbye! Have a great day.")
        break

    else:
        print("❌ Sorry! I don't understand that yet. Please try another question.") 