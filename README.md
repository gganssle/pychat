# pychat

A simple little Streamlit app to call OpenAI's models for customer conversation autocompletion and summarization.

# Running the App
1. First install the deps:

      `poetry install`

2. Then get an api key from OpenAI [here](https://platform.openai.com/account) and put it in a `key.json` file in the base directory, formatted like this:
> {
>  "key": "keystringhere"
>}

3. Finally, simply run the app:

      `poetry run streamlit run convoAI.py`


# License
Licensed [MIT](https://www.mit.edu/~amini/LICENSE.md). Feel free to use the code any way you wish!

