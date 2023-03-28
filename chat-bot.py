# define a function to get user input
def get_input():
    user_input = input("You: ")
    return user_input.lower()

# define a function to check if the user input contains a specific keyword
def contains_keyword(user_input, keyword):
    if keyword in user_input:
        return True
    else:
        return False

# define a function to generate a response based on the user input
def generate_response(user_input):
    # create a dictionary of responses for each keyword
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hello! How can I help you today?",
        "problem": "What seems to be the problem?",
        "issue": "What seems to be the problem?",
        "error": "Can you please tell me more about the error message you received?",
        "help": "Sure, I'm here to help! What do you need help with?",
        "thanks": "You're welcome! Is there anything else I can assist you with?",
        "thank you": "You're welcome! Is there anything else I can assist you with?"
    }
    
    # check if the user input contains a specific keyword
    for keyword, response in responses.items():
        if contains_keyword(user_input, keyword):
            return response
    
    # if no keywords match, return a generic response
    return "I'm sorry, I didn't quite understand that. Can you please rephrase or ask another question?"

# greet the user and ask for their name
print("Welcome to Technical Support. My name is ChatBot. What's your name?")
user_name = input("You: ")

# greet the user by name
print(f"Hello, {user_name}! How can I assist you today?")

# start the conversation loop
while True:
    # get user input
    user_input = get_input()
    
    # check if the user wants to end the conversation
    if contains_keyword(user_input, "bye") or contains_keyword(user_input, "goodbye"):
        print("Goodbye! Have a nice day.")
        break
    
    # generate a response based on the user input
    response = generate_response(user_input)
    
    # print the response
    print(f"ChatBot: {response}")
