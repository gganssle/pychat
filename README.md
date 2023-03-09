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


# Auto-Resopnses
The OpenAI API is slow to respond, and I haven't cared enough to make the call asynchronous using [Sanic](https://sanic.dev/en/) or other. That means this app runs mildly slow when you enter a customer comment. If you want to stop using autoresponses, comment out the lines marked "auto responses" in `convoAI.py`.

Better yet, upgrade those lines to use an async call and hit me with a PR.

# License
Licensed [MIT](https://www.mit.edu/~amini/LICENSE.md). Feel free to use the code any way you wish!

