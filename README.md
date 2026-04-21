# 📄 DocInsight AI – Resume Analyzer

An AI-powered Resume Analyzer web application that evaluates resumes based on ATS (Applicant Tracking System) criteria. It extracts text from uploaded resumes, analyzes keywords, and provides actionable suggestions to improve resume quality.

---

## 🚀 Live Demo

- 🌐 Frontend: https://doc-insight-ai-orcin.vercel.app  
- ⚙️ Backend API: https://docinsight-backend.onrender.com/docs  

---

## ✨ Features

- 📂 Upload resumes in **PDF or DOCX format**
- 📊 Calculates **ATS Resume Score (0–100)**
- 🔍 Detects **important technical keywords**
- ⚠️ Provides **improvement suggestions**
- 🧾 Displays **formatted extracted text**
- 🎨 Clean and responsive user interface

---

## 🛠 Tech Stack

### Frontend
- React.js
- Axios
- CSS (Custom Styling)

### Backend
- FastAPI
- Python
- PyPDF2 (PDF parsing)
- python-docx (DOCX parsing)

### Deployment
- Vercel (Frontend)
- Render (Backend)

---

## 📸 Screenshots

_Add screenshots of your application here (recommended for better presentation)_
<img width="1759" height="903" alt="image" src="https://github.com/user-attachments/assets/8b83790a-9a55-4d9d-853a-6f11e9d6abac" />
<img width="1593" height="929" alt="image" src="https://github.com/user-attachments/assets/1e75bc90-7918-4c4a-806b-759680f1ef54" />


---

## ⚙️ How It Works

1. User uploads a resume (PDF/DOCX)
2. Backend extracts text from the file
3. Resume is analyzed for:
   - Keywords
   - Sections (Education, Projects, Experience)
   - Length
4. System generates:
   - Resume Score
   - Suggestions
   - Keyword insights
5. Results are displayed on the frontend

---

## 🧠 Resume Analysis Logic

- Base score starts at **50**
- Keywords increase score (+5 each)
- Missing sections reduce score
- Short resumes reduce score
- Suggestions are always provided for improvement

---


