import { useState } from "react";
import { analyzeConflict } from "../utils/api";

export default function Home() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState<any>(null);

  const handleAnalyze = async () => {
    const data = await analyzeConflict(message);
    setResult(data);
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">AI Conflict Analyzer</h1>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        className="w-full border p-2"
        placeholder="Enter message to analyze"
      />
      <button onClick={handleAnalyze} className="mt-4 bg-blue-600 text-white px-4 py-2">
        Analyze
      </button>
      {result && (
        <div className="mt-4">
          <p><strong>Conflict Score:</strong> {result.conflict_score}</p>
          <p><strong>Sentiment:</strong> {result.sentiment}</p>
          <p><strong>Emotion:</strong> {result.emotion}</p>
          <p><strong>Language:</strong> {result.language}</p>
        </div>
      )}
    </div>
  );
}
