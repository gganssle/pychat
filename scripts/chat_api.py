import openai


def pull_response():
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful customer service agent."},
        {"role": "user", "content": "What's a synonym for happy?"}
      ]
  )

  return response['choices'][0]['message']['content']


def summarize(conversation):
  '''
  Use an OpenAI model to summarize a conversation.

  Args:
    convo       [string] conversational text
  Returns:
    response    [string] summarized conversation
  Raises:
    None
  '''
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful customer service agent."},
        {"role": "user", "content": f'Very briefly summarize the following conversation: \"{conversation}\"'}
      ]
  )

  return response['choices'][0]['message']['content']



# example syntax for the davinci model family
# response = openai.Completion.create(
#   model = "text-davinci-003",
#   prompt="What's a synonym for happy?"
# )
# print(response)

