import streamlit as st
import json, time
import numpy as np
import openai
from scripts import messages, chat_api


# init
with open('key.json', 'r') as f:
  openai.api_key = json.load(f)['key']

st.set_page_config(layout="wide")


# layout 
col1, col2, col3 = st.columns([2,4,2])

# customer inputs
with col1:
  st.header('Customer Input')
  st.image("assets/customer.png", width=100)
  customer_input = st.text_input(
    'Customer:',
    '', 
    key='cust',
    on_change = lambda: setattr(st.session_state, 'agnt', '')
  )
  st.session_state[f'{time.time()}_customer'] = customer_input


# trailing message history
with col2:
  st.header("Conversation")

  # the text entry box
  agent_input = st.text_input(
    'Response:',
    '', 
    key='agnt',
    on_change = lambda: setattr(st.session_state, 'cust', '')
  )
  st.session_state[f'{time.time()}_agent'] = agent_input
  # messages.debug_state_printer(st.session_state)

  # the message history div
  st.text_area(
    'Messages:', 
    value=messages.message_extractor(st.session_state), 
    height=500, 
    key='msgs'
  )

  
# agent assitance tool
with col3:
  # header
  st.header("Agent Assistance")
  st.image("assets/agent.png", width=130)

  # summarization tool
  if st.button(
      'Summarize Conversation',
      on_click = lambda: messages.button_callback(st.session_state)
    ):
    label = 'Summarized conversation:'
    seed = chat_api.summarize(messages.message_extractor(st.session_state))
  else:
    label = 'Suggested response:'
    seed = ''

  # conversational summary
  st.text_area(
    label,
    height=300, 
    key='resp',
    value = seed
  )


