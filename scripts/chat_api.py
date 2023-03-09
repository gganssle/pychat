import openai

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
