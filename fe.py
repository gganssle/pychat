import streamlit as st
import json
import openai


with open('key.json', 'r') as f:
  openai.api_key = json.load(f)['key']


# response = openai.Completion.create(
#   model = "text-davinci-003",
#   prompt="What's a synonym for happy?"
# )
# print(response)

def pull_response():
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful customer service agent."},
        {"role": "user", "content": "What's a synonym for happy?"}
      ]
  )
  return response['choices'][0]['message']['content']

def get_text():
  input_text = st.text_input("You: ","Ask the bot a question.")
  return input_text 


st.sidebar.title("Recommended Responses")
st.title("""
Customer Chat  
Please respond to your customer below in a timely manner. 
""")


ind = 1
if st.sidebar.button('Make recommendations.'):
  print(pull_response())
  st.title("Recommended responses initialized")
  ind = ind +1
        
user_input = get_text()


if True:
  st.text_area("Bot:", value=pull_response(), height=200, max_chars=None, key=None)

