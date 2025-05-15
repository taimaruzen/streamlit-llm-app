import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# .envファイルからAPIキー読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ChatOpenAIモデルを設定
llm = ChatOpenAI(openai_api_key=api_key, temperature=0)

# LLMに問い合わせる関数
def ask_expert(user_input, expert_type):
    if expert_type == "医者":
        system_prompt = "あなたは日本人の医者です。健康や病気について専門的かつ親切に答えてください。"
    elif expert_type == "弁護士":
        system_prompt = "あなたは日本人の弁護士です。法律の質問に専門的かつわかりやすく答えてください。"
    else:
        system_prompt = "あなたは賢い専門家です。"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]
    response = llm(messages)
    return response.content

# StreamlitのUI部分
st.title("専門家AIチャット")
st.write("質問を入力して、相談したい専門家を選んでください。")

expert_type = st.radio("相談相手を選んでください", ["医者", "弁護士"])
user_input = st.text_input("あなたの質問を入力")

if st.button("送信"):
    if user_input:
        with st.spinner("AIが考え中..."):
            result = ask_expert(user_input, expert_type)
        st.success("AIの回答：")
        st.write(result)
    else:
        st.warning("質問を入力してください。")
