import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")