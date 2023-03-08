import streamlit as st
import json, time
import openai
import numpy as np


# init
with open('key.json', 'r') as f:
  openai.api_key = json.load(f)['key']

st.set_page_config(layout="wide")


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


def message_extractor():
  values = [val for val in st.session_state.values()]
  keys = [key for key in st.session_state.keys()]
  response = ''

  for i in range(len(values)):
    if values[i] != '':
      response = response + f'{keys[i]}:\t{values[i]}\n'

  return response


# layout #############
col1, col2, col3 = st.columns([2,4,2])

with col1:
  st.header("Customer Input")
  st.image("assets/customer.png", width=100)
  customer_input = st.text_input('Customer:','', key='cust')
  st.session_state[f'{time.time()}_customer'] = customer_input


with col2:
  st.header("Conversation History")
  st.text_area("Messages:", value=message_extractor(), height=500)
  agent_input = st.text_input("Response: ","")
  st.session_state[f'{time.time()}_agent'] = agent_input
    

with col3:
  st.header("Agent Assistance")
  st.image("assets/agent.png", width=130)
  st.text_area("Responses: ","Select a response.", height=300)


