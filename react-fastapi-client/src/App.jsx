import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [answer, setAnswer] = useState("");
  const API_BASE_URL = "https://zany-space-robot-jj5xj9r9xw6ph9xp-8000.app.github.dev";
  // const API_BASE_URL = "http://localhost:8000";
  // const API_BASE_URL = "http://127.0.0.1:8000";


  async function askFastApi(message) {
    const response = await fetch(`${API_BASE_URL}/api/ai/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message
      })
    });

    const result = await response.json();

    return result.data.answer;
  }

  async function handleAsk() {
    const result = await askFastApi(message);
    setAnswer(result);
  }

  return (
    <div style={{ padding: "30px" }}>
      <h1>React에서 FastAPI AI 호출</h1>

      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="질문을 입력하세요"
        rows={5}
        style={{ width: "100%", padding: "10px" }}
      />

      <br />
      <br />

      <button onClick={handleAsk}>
        FastAPI에 질문하기
      </button>

      <hr />

      <h2>AI 응답</h2>
      <p>{answer}</p>
    </div>
  );
}

export default App;