from openai import OpenAI
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# OpenAI 클라이언트 생성
client = OpenAI()

# gpt-5.4-mini gpt-5.4-nano
response  = client.chat.completions.create(
    model="gpt-4o-mini", 
    messages=[
        {
            "role": "user",
            "content": "AI를 활용한 보고서 작성 방법을 5단계로 설명해줘.",
        }
    ],
    stream=True,
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)