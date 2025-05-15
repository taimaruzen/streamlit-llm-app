import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=api_key,
    temperature=0
)

def ask_expert(user_input, expert_type):
    if expert_type == "医者":
        system_prompt = "あなたは日本人の医者です。健康について丁寧に答えてください。"
    elif expert_type == "弁護士":
        system_prompt = "あなたは日本人の弁護士です。法律に関してわかりやすく答えてください。"
    else:
        system_prompt = "あなたは親切な専門家です。"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]
    response = llm.invoke(messages)
    return response.content

st.title("専門家AIチャット")
st.write("質問を入力して、専門家を選択してください。")

expert_type = st.radio("専門家を選んでください：", ["医者", "弁護士"])
user_input = st.text_input("質問を入力してください")

if st.button("送信"):
    if user_input:
        with st.spinner("AIが考えています..."):
            result = ask_expert(user_input, expert_type)
        st.success("AIの回答：")
        st.write(result)
    else:
        st.warning("質問を入力してください。")
