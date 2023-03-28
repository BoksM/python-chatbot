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

# define a function to generate a response based on the user input and user type
def generate_response(user_input, user_type):
    # create a dictionary of responses for each keyword
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hello! How can I help you today?",
        "problem": "What seems to be the problem?",
        "issue": "What seems to be the problem?",
        "error": "Can you please tell me more about the error message you received?",
        "help": "Sure, I'm here to help! What do you need help with?",
        "thanks": "You're welcome! Is there anything else I can assist you with?",
        "thank you": "You're welcome! Is there anything else I can assist you with?",
        "connect": {
            "staff": "To connect to the WLC_OpenAccess wireless network:\n1. On your personal device which you want to connect to the wireless network, search the wireless network profiles and select the 'WLC_OpenAccess' network.\n2. Once your device has connected to the 'WLC_OpenAccess' wireless profile, you will be redirected to an online portal requiring authentication. If you are not automatically redirected, open your browser and navigate to any website, you should be redirected to the online authentication portal.\n3. Staff members can authenticate themselves by entering their network credentials. These are the same credentials used to log on to a College PC.\n4. Once successfully authenticated, you will be connected to the wireless network.",
            "student": "To connect to the WLC_OpenAccess wireless network:\n1. On your personal device which you want to connect to the wireless network, search the wireless network profiles and select the 'WLC_OpenAccess' network.\n2. Once your device has connected to the 'WLC_OpenAccess' wireless profile, you will be redirected to an online portal requiring authentication. If you are not automatically redirected, open your browser and navigate to any website, you should be redirected to the online authentication portal.\n3. Students can authenticate themselves by entering their network credentials. These are the same credentials used to log on to a College PC.\n4. Once successfully authenticated, you will be connected to the wireless network.",
            "guest": "To connect to the WLC_OpenAccess wireless network:\n1. On your personal device which you want to connect to the wireless network, search the wireless network profiles and select the 'WLC_OpenAccess' network.\n2. Once your device has connected to the 'WLC_OpenAccess' wireless profile, you will be redirected to an online portal requiring authentication. If you are not automatically redirected, open your browser and navigate to any website, you should be redirected to the online authentication portal.\n3. Guests can authenticate themselves by entering the guest credentials provided to them by the College.\n4. Once successfully authenticated, you will be connected to the wireless network.",
            "Password": "To change your password: 1) Log in to your college computer, or any unused staff computer, and press and hold the CTRL, ALT and DEL keys together. A system menu will be displayed from where you simply select the ‘Change a password’ option. 2) After selecting the option to ‘Change a password’, you will be asked to enter your old password. This is the password you are currently using to login to the computer."
            
        }
    }
    
    # check if the user input contains a specific keyword
    for keyword, response in responses.items():
        if contains_keyword(user_input, keyword):
            if isinstance(response, dict):
                return response[user_type]
            else:
                return response
    
    # if no keywords match, return a generic response
    return "I'm sorry, I didn't quite understand that. Can you please rephrase or ask another question?"

# greet the user and ask for their name
print("Welcome to Technical Support. My name is ChatBot. What's your name?")
user_name = input("You: ")

# greet the user and ask for their name
print("Are you a staff member, guest or student?")
user_type = input("You: ")

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
    response = generate_response(user_input, user_type)
    
    # print the response
    print(f"ChatBot: {response}")
