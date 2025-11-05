@"
# python-practice-gowtham

Small learning projects demonstrating Python fundamentals and a FastAPI micro-app.

## Projects
- `basics.py` — Python syntax examples
- `calc.py` — CLI calculator
- `lists_practice.py` — List operations
- `app.py` — FastAPI demo with:
  - `GET /` → health/greeting
  - `GET /greet/{name}` → personalized greeting

## Run locally (Windows PowerShell)
1. python -m venv venv
2. .\venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. uvicorn src.app:app --reload --port 8000
5. Visit http://127.0.0.1:8000/docs


## Notes
- Part of a 12-week AI developer learning plan (FastAPI, LangChain, OpenAI, AWS).
"@ > README.md

git add README.md
git commit -m "docs: add README"
git push
