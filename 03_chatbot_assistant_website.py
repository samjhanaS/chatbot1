import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Chatbot")

demo.launch(share=True)