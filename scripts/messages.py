import streamlit as st
import numpy as np


def message_extractor(state):
  # pull the values from state
  values = np.array([val for val in state.values()])
  keys = np.array([key.split('_')[-1] for key in state.keys()])
  ts = np.array([key.split('_')[0] for key in state.keys()])
  
  # chronological sort
  indices = np.argsort(ts)
  values = values[indices]
  keys = keys[indices]
  
  # format the messages
  response = ''
  for i in range(len(values)):
    if (values[i] != '') & (keys[i] not in ['cust', 'agnt', 'resp', 'msgs']):
      response = response + f'{keys[i]}:\t{values[i]}\n'

  return response


def debug_state_printer(state):
  for key in state.keys():
    print(key, '\t', state[key])
  print('\n\n')

