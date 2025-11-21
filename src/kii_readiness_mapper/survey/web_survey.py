from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from ..questionnaire.loader import QuestionnaireLoader
from ..questionnaire.scoring import ScoringEngine
from ..domain.enums import Sector, SystemType

app = FastAPI()

# We need to locate templates. For now, we'll assume they are in a 'templates' dir relative to this file
# or we can embed a simple string template for simplicity in this MVP.
# Let's use a simple string template to avoid creating extra directories/files for now, 
# or create a templates directory if we want to be proper.
# Given the constraints, I'll use a simple string template approach or a minimal setup.

TEMPLATES_DIR = Path(__file__).parent / "templates"
TEMPLATES_DIR.mkdir(exist_ok=True)

# Create a basic template
INDEX_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>KII Readiness Survey</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .section { margin-bottom: 20px; border: 1px solid #ddd; padding: 15px; border-radius: 5px; }
        .question { margin-bottom: 15px; }
        .btn { background: #3498db; color: white; padding: 10px 20px; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Анкета KII Readiness</h1>
    <form action="/submit" method="post">
        {% for section in questionnaire.sections %}
        <div class="section">
            <h2>{{ section.title }}</h2>
            {% for question in section.questions %}
            <div class="question">
                <p><strong>{{ question.text }}</strong></p>
                {% if question.type == 'yes_no' %}
                    <label><input type="radio" name="{{ question.id }}" value="true"> Да</label>
                    <label><input type="radio" name="{{ question.id }}" value="false"> Нет</label>
                {% elif question.type == 'single_choice' %}
                    <select name="{{ question.id }}">
                    {% for opt in question.options %}
                        <option value="{{ opt.value }}">{{ opt.label }}</option>
                    {% endfor %}
                    </select>
                {% else %}
                    <input type="text" name="{{ question.id }}">
                {% endif %}
            </div>
            {% endfor %}
        </div>
        {% endfor %}
        <button type="submit" class="btn">Отправить</button>
    </form>
</body>
</html>
"""

RESULT_HTML = """
<!DOCTYPE html>
<html>
<head><title>Результат</title></head>
<body>
    <h1>Результат оценки</h1>
    <p>Оценка готовности: {{ scores.overall_readiness }}%</p>
    <a href="/">Пройти заново</a>
</body>
</html>
"""

with open(TEMPLATES_DIR / "index.html", "w") as f:
    f.write(INDEX_HTML)

with open(TEMPLATES_DIR / "result.html", "w") as f:
    f.write(RESULT_HTML)

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Initialize loader (assuming banks are in standard location)
# In a real app, this path should be configurable
BANKS_DIR = Path(__file__).parent.parent / "questionnaire" / "banks"
loader = QuestionnaireLoader(BANKS_DIR)
questionnaire = loader.load_questionnaire(Sector.HEALTH, SystemType.IS) # Default for demo

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "questionnaire": questionnaire})

@app.post("/submit", response_class=HTMLResponse)
async def submit(request: Request):
    form_data = await request.form()
    answers = dict(form_data)
    
    # Convert "true"/"false" strings to booleans
    for k, v in answers.items():
        if v == "true": answers[k] = True
        elif v == "false": answers[k] = False
            
    engine = ScoringEngine()
    scores = engine.calculate_scores(questionnaire, answers)
    
    return templates.TemplateResponse("result.html", {"request": request, "scores": scores})

def run_server(host: str, port: int):
    import uvicorn
    uvicorn.run(app, host=host, port=port)
