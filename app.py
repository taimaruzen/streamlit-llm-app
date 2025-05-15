import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# .envファイルの読み込み
load_dotenv()

# APIキーの取得
api_key = os.getenv("OPENAI_API_KEY")

# ChatOpenAIの初期化（gpt-4o使用）
llm = ChatOpenAI(
    openai_api_key=api_key,
    model="gpt-4o",
    temperature=0
)

# 回答を生成する関数
def ask_expert(user_input, expert_type):
    if expert_type == "医者":
        system_prompt = "あなたは日本人の医者です。健康や病気について専門的に優しく答えてください。"
    elif expert_type == "弁護士":
        system_prompt = "あなたは日本人の弁護士です。法律についてわかりやすく正確に答えてください。"
    else:
        system_prompt = "あなたは親切な専門家です。"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)
    return response.content

# Streamlit UI部分
st.title("専門家AIチャット")
st.write("相談内容を入力し、相談する専門家を選んでください。")

expert_type = st.radio("専門家を選択", ["医者", "弁護士"])
user_input = st.text_input("質問を入力してください")

if st.button("送信"):
    if user_input:
        with st.spinner("AIが回答中..."):
            answer = ask_expert(user_input, expert_type)
        st.success("AIの回答：")
        st.write(answer)
    else:
        st.warning("質問を入力してください。")
