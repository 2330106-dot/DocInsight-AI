import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    // ✅ File type validation
    if (!file.name.endsWith(".pdf") && !file.name.endsWith(".docx")) {
      alert("Only PDF or DOCX allowed");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const res = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Error uploading file");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>📄 DocInsight AI</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Processing..." : "Analyze Document"}
      </button>

      {loading && <p>⏳ Processing...</p>}

      {result && (
        <div className="result">
          <h2>📊 Resume Analysis</h2>

          {/* ✅ Colored Score */}
          <h3 style={{ color: result.resume_score > 75 ? "green" : "orange" }}>
            Score: {result.resume_score}/100
          </h3>

          <h4>✅ Keywords Found:</h4>
          <p>
            {result.keywords && result.keywords.length > 0
              ? result.keywords.join(", ")
              : "No keywords found"}
          </p>

          <h4>⚠ Suggestions:</h4>
          <ul>
            {result.suggestions && result.suggestions.length > 0 ? (
              result.suggestions.map((item, index) => (
                <li key={index}>{item}</li>
              ))
            ) : (
              <li>No suggestions</li>
            )}
          </ul>

          <h3>Word Count: {result.word_count}</h3>

          <h3>Formatted Text:</h3>
          <p style={{ whiteSpace: "pre-line", textAlign: "left" }}>
            {result.ai_suggestion}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;