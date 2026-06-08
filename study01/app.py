import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("LLM 기반 Streamlit 챗봇입니다.")

# 대화 이력 초기화
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 지금까지 대화 내용 출력
for role, content in st.session_state["messages"]:
    with st.chat_message(role):
        st.write(content)

# 사용자 입력
user_input = st.chat_input("메시지를 입력하세요.")

if user_input:
    # 1) 사용자 메시지 화면 및 이력에 추가
    st.session_state["messages"].append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # 2) OpenAI LLM 호출용 messages 리스트 만들기
    messages = []
    messages.append({"role": "system", "content": "친절한 LLM 튜터입니다."})

    for item in st.session_state["messages"]:
        role = item[0]
        content = item[1]

        one_message = {}
        one_message["role"] = role
        one_message["content"] = content

        messages.append(one_message)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )

    assistant_reply = response.choices[0].message.content

    # 3) 모델 응답 출력 및 이력에 추가
    st.session_state["messages"].append(("assistant", assistant_reply))
    with st.chat_message("assistant"):
        st.write(assistant_reply)