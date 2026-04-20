from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import PyPDF2
import docx
import textwrap

app = FastAPI()

# ✅ Enable CORS for your Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://doc-insight-ai-orcin.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- TEXT EXTRACTION --------
def extract_text(filename, content):
    text = ""

    if filename.endswith(".pdf"):
        from io import BytesIO
        reader = PyPDF2.PdfReader(BytesIO(content))
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()

    elif filename.endswith(".docx"):
        from io import BytesIO
        file = BytesIO(content)
        doc = docx.Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])

    return text


# -------- TEXT IMPROVEMENT --------
def improve_text(text):
    try:
        lines = text.split("\n")
        formatted = "\n\n".join([line.strip() for line in lines if line.strip()])
        return formatted[:1000]
    except:
        return "Improvement not available"


# -------- RESUME ANALYZER --------
def analyze_resume(text):
    score = 50
    suggestions = []

    # Keyword checks
    keywords = ["python", "java", "sql", "react", "project", "internship"]
    found_keywords = [k for k in keywords if k in text.lower()]

    score += len(found_keywords) * 5

    # ✅ Updated condition
    if len(found_keywords) < 2:
        suggestions.append("Add more technical keywords (Python, SQL, React)")

    # Length check
    if len(text.split()) < 300:
        suggestions.append("Resume is too short. Add more details.")
        score -= 10

    # Sections check
    if "project" not in text.lower():
        suggestions.append("Add a Projects section")
        score -= 10

    if "experience" not in text.lower():
        suggestions.append("Add Experience/Internship section")
        score -= 10

    if "education" not in text.lower():
        suggestions.append("Add Education section")
        score -= 10

    # ✅ Always give suggestions
    if not suggestions:
        suggestions.append("Great resume! Consider adding measurable achievements (e.g., increased efficiency by 20%).")
        suggestions.append("Use strong action verbs (Developed, Built, Optimized).")

    score = max(0, min(score, 100))

    return {
        "score": score,
        "suggestions": suggestions,
        "keywords_found": found_keywords
    }


# -------- ROUTE --------
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()

    text = extract_text(file.filename, content)

    word_count = len(text.split())
    ai_output = improve_text(text)

    resume_analysis = analyze_resume(text)

    return {
        "word_count": word_count,
        "ai_suggestion": ai_output,
        "resume_score": resume_analysis["score"],
        "suggestions": resume_analysis["suggestions"],
        "keywords": resume_analysis["keywords_found"]
    }