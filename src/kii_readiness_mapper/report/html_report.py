from jinja2 import Template
from ..domain.models import KiiReadinessResult, OrganizationProfile

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Отчёт КИИ: {{ profile.name }}</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #2c3e50; }
        .summary { background-color: #f8f9fa; padding: 15px; border-radius: 5px; }
        .risk { color: #e74c3c; }
        .footer { margin-top: 50px; font-size: 0.8em; color: #7f8c8d; }
    </style>
</head>
<body>
    <h1>Отчёт о готовности к КИИ: {{ profile.name }}</h1>
    
    <div class="summary">
        <h2>Основные выводы</h2>
        <ul>
            <li><strong>Потенциальный субъект КИИ:</strong> {{ 'Да' if result.potential_kii_subject else 'Нет' }} ({{ result.subject_confidence }})</li>
            <li><strong>Вероятная категория:</strong> {{ result.estimated_category.value }}</li>
            <li><strong>Оценка готовности:</strong> {{ "%.1f"|format(result.criticality_score) }}%</li>
        </ul>
        <p>{{ result.summary_text }}</p>
    </div>

    <h2>Ключевые риски</h2>
    <ul>
    {% for risk in result.key_risks %}
        <li class="risk">{{ risk }}</li>
    {% else %}
        <li>Критичных рисков не выявлено.</li>
    {% endfor %}
    </ul>

    <div class="footer">
        Сгенерировано kii-readiness-mapper. Не является официальным заключением.
    </div>
</body>
</html>
"""

class HtmlReportGenerator:
    def generate(self, result: KiiReadinessResult, profile: OrganizationProfile) -> str:
        """
        Generate an HTML report from the result.
        """
        template = Template(HTML_TEMPLATE)
        return template.render(result=result, profile=profile)
