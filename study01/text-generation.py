from openai import OpenAI
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# OpenAI 클라이언트 생성
client = OpenAI()

# gpt-5.4-mini gpt-5.4-nano
completion = client.chat.completions.create(
    model="gpt-4o-mini", 
    messages=[
        {
            "role": "user",
            "content": "SQL Injection에 대해 한 문장으로 설명해줘.",
        }
    ],
)

print(completion.choices[0].message.content)