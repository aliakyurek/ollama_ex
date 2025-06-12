from ollama import chat
from ollama import ChatResponse
from langchain_ollama import ChatOllama
from litellm import completion
from openai import OpenAI

def func1():
    response: ChatResponse = chat(model='qwen3:8b', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)

def func2():
    client = OpenAI(
        base_url = 'http://localhost:11434/v1',
        api_key='ollama', # required, but unused
    )

    response = client.chat.completions.create(
        model="qwen3:8b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
      ]
    )
    print(response.choices[0].message.content)

def func3():

    llm = ChatOllama(
        model="qwen3:8b",
        temperature=0,
        # other params...
    )
    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
            ("human", "I love programming."),
    ]
    response =  llm.invoke(messages)
    print(response.content)

def func4():
    response = completion(
        model="ollama/qwen3:8b",
        messages=[{"content": "respond in 20 words. who are you?", "role": "user"}]
    )
    print(response)


func2()



