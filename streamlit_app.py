# import streamlit as st
# import google.generativeai as genai

# st.title("🐻‍❄️ FoodRec Chatbot App")
# # st.html("<b>🐻‍❄️ Lab3 Chatbot App</b>")
# st.subheader("Conversation")

# # Capture Gemini API Key
# gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type the API", type="password")
# # Initialize the Gemini Model
# if gemini_api_key:
# 	try:
# 		# Configure Gemini with the provided API Key
# 		genai.configure(api_key=gemini_api_key)
# 		model = genai.GenerativeModel("gemini-pro")
# 		st.success("Gemini API Key successfully configured.")
# 	except Exception as e:
# 		st.error(f"An error occurred while setting up the Gemini model: {e}")
		
# # Initialize session state for storing chat history
# if "chat_history" not in st.session_state:
# 	st.session_state.chat_history = [] # Initialize with an empty list
	
# # Display previous chat history using st.chat_message (if available)
# for role, message in st.session_state.chat_history:
# 	st.chat_message(role).markdown(message)


# # Capture user input and generate bot response
# if user_input := st.chat_input("Say something..."):
# 	# Store and display user message
# 	st.session_state.chat_history.append(("user", user_input))
# 	st.chat_message("user").markdown(user_input)

# 	# Use Gemini AI to generate a bot response
# 	if model:
# 		try:
# 			response = model.generate_content(user_input)
# 			bot_response = response.text
			
# 			# Store and display the bot response
# 			st.session_state.chat_history.append(("assistant", bot_response))
# 			st.chat_message("assistant").markdown(bot_response)
# 		except Exception as e:
# 			st.error(f"An error occurred while generating the response: {e}")
# 		# Use Gemini AI to generate a bot response

# import streamlit as st
# import google.generativeai as genai

# st.title("🐻‍❄️ FoodRec Chatbot App")
# st.subheader("Conversation")

# # Capture Gemini API Key
# gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type the API", type="password")

# # Initialize the Gemini Model
# if gemini_api_key:
#     try:
#         # Configure Gemini with the provided API Key
#         genai.configure(api_key=gemini_api_key)
#         model = genai.GenerativeModel("gemini-pro")
#         st.success("Gemini API Key successfully configured.")
#     except Exception as e:
#         st.error(f"An error occurred while setting up the Gemini model: {e}")

# # Initialize session state for storing chat history and conversation context
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []  # Initialize with an empty list

# if "awaiting_hungry_response" not in st.session_state:
#     st.session_state.awaiting_hungry_response = False  # Flag to track if bot asked about hunger

# # Display previous chat history using st.chat_message (if available)
# for role, message in st.session_state.chat_history:
#     st.chat_message(role).markdown(message)

# # List of keywords related to food to detect user intent for food recommendations
# food_keywords = ["food", "hungry", "meal", "recommendation", "eat", "dish", "cuisine"]

# # List of positive responses to detect affirmative answers
# positive_responses = ["yes", "yep", "okay", "sure", "absolutely", "definitely", "of course", "yeah", "affirmative"]

# # Function to check if user input contains any keyword from a list
# def contains_keyword(user_input, keywords):
#     return any(keyword in user_input.lower() for keyword in keywords)

# # Capture user input and generate bot response
# if user_input := st.chat_input("Say something..."):
#     # Store and display user message
#     st.session_state.chat_history.append(("user", user_input))
#     st.chat_message("user").markdown(user_input)

#     # Process user input based on conversation context
#     if st.session_state.awaiting_hungry_response:
#         # Check if the user responded positively
#         if contains_keyword(user_input, positive_responses):
#             # Generate a food recommendation response using Gemini AI
#             if 'model' in locals():
#                 try:
#                     # Custom prompt for food recommendation
#                     food_prompt = f"Can you recommend a delicious Thai {meal_type.lower()} option?"
#                     response = model.generate_content(food_prompt)
#                     bot_response = response.text

#                     # Store and display the bot response
#                     st.session_state.chat_history.append(("assistant", bot_response))
#                     st.chat_message("assistant").markdown(bot_response)
#                 except Exception as e:
#                     st.error(f"An error occurred while generating the response: {e}")
#         else:
#             # User did not respond positively; respond accordingly
#             bot_response = "Alright, let me know if you need any food recommendations!"
#             st.session_state.chat_history.append(("assistant", bot_response))
#             st.chat_message("assistant").markdown(bot_response)
        
#         # Reset the hunger response flag
#         st.session_state.awaiting_hungry_response = False
#     else:
#         # Check if the user input contains any food-related keywords
#         if contains_keyword(user_input, food_keywords):
#             # Generate a food recommendation response using Gemini AI
#             if 'model' in locals():
#                 try:
#                     # Custom prompt for food recommendation
#                     food_prompt = "Can you recommend a delicious meal or food option?"
#                     response = model.generate_content(food_prompt)
#                     bot_response = response.text

#                     # Store and display the bot response
#                     st.session_state.chat_history.append(("assistant", bot_response))
#                     st.chat_message("assistant").markdown(bot_response)
#                 except Exception as e:
#                     st.error(f"An error occurred while generating the response: {e}")
#         else:
#             # Generate a different response for non-food-related inputs
#             bot_response = "Tell me.. are you hungry?"
#             st.session_state.chat_history.append(("assistant", bot_response))
#             st.chat_message("assistant").markdown(bot_response)
            
#             # Set the flag to indicate that the bot is awaiting a hunger response
#             st.session_state.awaiting_hungry_response = True
            
import streamlit as st
import google.generativeai as genai
from datetime import datetime
import pytz

st.title("🍜 This Meal? Chatbot App")
st.subheader("Conversation")

# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type the API", type="password")

# Initialize the Gemini Model
if gemini_api_key:
    try:
        # Configure Gemini with the provided API Key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        st.success("Gemini API Key successfully configured.")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")

# Initialize session state for storing chat history and conversation context
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Initialize with an empty list

if "awaiting_hungry_response" not in st.session_state:
    st.session_state.awaiting_hungry_response = False  # Flag to track if bot asked about hunger

# Display previous chat history using st.chat_message (if available)
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

# List of keywords related to food to detect user intent for food recommendations
food_keywords = ["food", "hungry", "meal", "recommendation", "eat", "dish", "cuisine"]

# List of positive responses to detect affirmative answers
positive_responses = ["yes", "yep", "okay", "sure", "absolutely", "definitely", "of course", "yeah", "affirmative"]

# Function to check if user input contains any keyword from a list
def contains_keyword(user_input, keywords):
    return any(keyword in user_input.lower() for keyword in keywords)

# Function to determine the meal based on current time in GMT+7
def get_current_meal():
    tz = pytz.timezone('Asia/Bangkok')  # Timezone for GMT+7 (Thailand)
    current_time = datetime.now(tz).time()

    if current_time >= datetime.strptime("06:00", "%H:%M").time() and current_time <= datetime.strptime("10:00", "%H:%M").time():
        return "breakfast"
    elif current_time > datetime.strptime("10:00", "%H:%M").time() and current_time <= datetime.strptime("14:00", "%H:%M").time():
        return "lunch"
    elif current_time > datetime.strptime("14:00", "%H:%M").time() and current_time <= datetime.strptime("18:00", "%H:%M").time():
        return "afternoon snack"
    elif current_time > datetime.strptime("18:00", "%H:%M").time() and current_time <= datetime.strptime("21:00", "%H:%M").time():
        return "dinner"
    else:
        return "late night snack"

# Capture user input and generate bot response
if user_input := st.chat_input("Say something..."):
    # Store and display user message
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").markdown(user_input)

    # Process user input based on conversation context
    if st.session_state.awaiting_hungry_response:
        # Check if the user responded positively
        if contains_keyword(user_input, positive_responses):
            # Determine current meal based on GMT+7 timezone
            meal_type = get_current_meal()

            # Generate a food recommendation response using Gemini AI
            if 'model' in locals():
                try:
                    # Custom prompt for Thai food recommendation based on meal type
                    food_prompt = f"Can you recommend a delicious Thai {meal_type} option?"
                    response = model.generate_content(food_prompt)
                    bot_response = response.text

                    # Store and display the bot response
                    st.session_state.chat_history.append(("assistant", bot_response))
                    st.chat_message("assistant").markdown(bot_response)
                except Exception as e:
                    st.error(f"An error occurred while generating the response: {e}")
        else:
            # User did not respond positively; respond accordingly
            bot_response = "Alright, let me know if you need any food recommendations!"
            st.session_state.chat_history.append(("assistant", bot_response))
            st.chat_message("assistant").markdown(bot_response)
        
        # Reset the hunger response flag
        st.session_state.awaiting_hungry_response = False
    else:
        # Check if the user input contains any food-related keywords
        if contains_keyword(user_input, food_keywords):
            # Determine current meal based on GMT+7 timezone
            meal_type = get_current_meal()

            # Generate a Thai food recommendation response using Gemini AI based on the current meal time
            if 'model' in locals():
                try:
                    # Custom prompt for Thai food recommendation
                    food_prompt = f"Can you recommend a delicious Thai {meal_type} option?"
                    response = model.generate_content(food_prompt)
                    bot_response = response.text

                    # Store and display the bot response
                    st.session_state.chat_history.append(("assistant", bot_response))
                    st.chat_message("assistant").markdown(bot_response)
                except Exception as e:
                    st.error(f"An error occurred while generating the response: {e}")
        else:
            # Generate a different response for non-food-related inputs
            bot_response = "Tell me... are you hungry?"
            st.session_state.chat_history.append(("assistant", bot_response))
            st.chat_message("assistant").markdown(bot_response)
            
            # Set the flag to indicate that the bot is awaiting a hunger response
            st.session_state.awaiting_hungry_response = True


