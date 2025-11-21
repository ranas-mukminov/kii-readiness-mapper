from ..domain.models import KiiReadinessResult, OrganizationProfile

class MarkdownReportGenerator:
    def generate(self, result: KiiReadinessResult, profile: OrganizationProfile) -> str:
        """
        Generate a Markdown report from the result.
        """
        md = f"# Отчёт о готовности к КИИ: {profile.name}\n\n"
        
        md += "## Основные выводы\n"
        md += f"- **Потенциальный субъект КИИ**: {'Да' if result.potential_kii_subject else 'Нет'} ({result.subject_confidence})\n"
        md += f"- **Вероятная категория**: {result.estimated_category.value}\n"
        md += f"- **Оценка готовности**: {result.criticality_score:.1f}%\n\n"
        
        md += "## Сводка\n"
        md += f"{result.summary_text}\n\n"
        
        md += "## Ключевые риски и несоответствия\n"
        if result.key_risks:
            for risk in result.key_risks:
                md += f"- {risk}\n"
        else:
            md += "Критичных рисков не выявлено (или данные не полны).\n"
            
        md += "\n---\n"
        md += "*Сгенерировано kii-readiness-mapper. Не является официальным заключением.*"
        
        return md
