# kii-readiness-mapper

[![CI](https://github.com/ranas-mukminov/kii-readiness-mapper/actions/workflows/ci.yml/badge.svg)](https://github.com/ranas-mukminov/kii-readiness-mapper/actions)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](pyproject.toml)

🇬🇧 English | 🇷🇺 [Русская версия](README.ru.md)

> [!IMPORTANT]
> This tool is for **self-assessment only** and does not replace official categorization or legal advice.

**kii-readiness-mapper** is a specialized CLI and Web tool designed to help organizations assess their readiness for compliance with the Russian Federal Law 187-FZ "On the Security of Critical Information Infrastructure (CII)". It automates the preliminary analysis process, helping IT and Security teams identify potential CII objects, evaluate current security measures, and generate readiness reports for internal audits.

## Key Features

*   **Interactive Questionnaires**: CLI and Web-based surveys tailored to different sectors (Healthcare, Energy, Finance, etc.).
*   **Readiness Assessment**: Estimates the probability of being classified as a CII subject based on organizational profile and system characteristics.
*   **Gap Analysis**: Identifies missing organizational and technical measures required by FSTEC regulations.
*   **Report Generation**: Automatically generates detailed reports in Markdown and HTML formats.
*   **Profile Management**: Uses structured YAML/JSON profiles to model your organization and information systems.
*   **Extensible Architecture**: Modular design allows for easy addition of new regulatory rules and survey templates.

## Architecture / Components

The solution consists of several Python modules working together:

*   **Survey Engine**: Collects data via CLI (`typer`) or Web UI (`fastapi`).
*   **Assessment Core**: Analyzes collected data against a rule set derived from 187-FZ and FSTEC orders.
*   **Domain Models**: Pydantic models representing the organization, systems, and security controls.
*   **Report Builder**: Jinja2-based engine for rendering human-readable results.

## Requirements

*   **OS**: Linux, macOS, or Windows.
*   **Python**: Version 3.10 or higher.
*   **Dependencies**: `typer`, `fastapi`, `uvicorn`, `jinja2`, `pyyaml`, `pydantic` (installed automatically).
*   **Access**: No root privileges required for standard usage.

## Quick Start

1.  **Install the tool**:
    ```bash
    pip install kii-readiness-mapper
    ```

2.  **Initialize a profile**:
    ```bash
    kii-readiness init-profile --output my-org.yaml
    ```

3.  **Run a survey**:
    ```bash
    kii-readiness run-cli-survey --sector health --output answers.yaml
    ```

4.  **Generate a report**:
    ```bash
    kii-readiness assess-profile --profile my-org.yaml --answers answers.yaml --output report.md
    ```

## Installation

### Install via pip (Recommended)

```bash
pip install kii-readiness-mapper
```

### Install from Source

If you want to use the latest version from the repository:

```bash
# Clone the repository
git clone https://github.com/ranas-mukminov/kii-readiness-mapper.git
cd kii-readiness-mapper

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the package
pip install .
```

### For Development

To install with development dependencies (linting, testing):

```bash
pip install -e ".[dev]"
```

## Configuration

The tool uses YAML files for configuration and data storage.

### Organization Profile (`org-profile.yaml`)
Describes the legal entity and its primary activities.

```yaml
organization:
  name: "My Hospital"
  inn: "1234567890"
  sector: "healthcare"
  employees_count: 500
  is_government_entity: false
```

### Answers File (`answers.yaml`)
Contains the raw data collected during the survey process.

```yaml
system_id: "his-core-01"
answers:
  has_personal_data: true
  criticality_level: "high"
  external_connections: true
  downtime_impact: "critical"
```

## Usage & Common Tasks

### Initialize Organization Profile
Create a template file to describe your organization.

```bash
kii-readiness init-profile --output config/org.yaml
```

### Conduct a Survey
Run an interactive questionnaire in the terminal to gather data about a specific system.

```bash
kii-readiness run-cli-survey \
  --sector healthcare \
  --system-type "medical-info-system" \
  --output data/survey_results.yaml
```

### Assess Readiness
Process the profile and survey answers to calculate readiness scores and identify gaps.

```bash
kii-readiness assess-profile \
  --profile config/org.yaml \
  --answers data/survey_results.yaml \
  --out results/assessment.json
```

### Generate Report
Convert the assessment result into a readable format (Markdown or HTML).

```bash
kii-readiness generate-report \
  --result results/assessment.json \
  --format markdown \
  --output reports/final_report.md
```

### Run Web Interface
Start a local web server to fill out surveys via a browser.

```bash
kii-readiness run-web-survey --port 8000
# Open http://localhost:8000 in your browser
```

## Update / Upgrade

To update the tool to the latest version:

```bash
git pull origin main
pip install . --upgrade
```

Check `CHANGELOG.md` for any breaking changes before upgrading.

## Logs & Troubleshooting

*   **Logs**: By default, the tool outputs logs to `stderr`.
*   **Validation Errors**: If you see `ValidationError`, check your YAML files against the schema. The error message usually points to the specific field causing the issue.
*   **Missing Dependencies**: Ensure you are running in the correct virtual environment where the package was installed.
*   **Web UI Issues**: If the web interface doesn't load, check if port 8000 is free or specify a different port using `--port`.

## Security Notes

*   **Data Privacy**: The reports generated by this tool may contain sensitive information about your infrastructure vulnerabilities. **Do not publish these reports publicly.**
*   **Local Execution**: All processing happens locally on your machine. No data is sent to external servers.
*   **Access Control**: Restrict access to the generated YAML/JSON files to authorized personnel only.

## Project Structure

*   `src/kii_readiness_mapper/` - Main source code.
    *   `assessment/` - Logic for analyzing gaps and readiness.
    *   `questionnaire/` - Survey definitions and logic.
    *   `cli/` - Command-line interface implementation.
*   `scripts/` - Helper scripts for linting and security checks.
*   `tests/` - Unit and integration tests.
*   `examples/` - Sample profiles and reports.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

1.  Fork the repository.
2.  Create a feature branch.
3.  Ensure all tests pass (`pytest`) and code is linted (`scripts/lint.sh`).
4.  Submit a Pull Request.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Author and Commercial Support

**Author**: [Ranas Mukminov](https://github.com/ranas-mukminov)

For production-grade implementation, infrastructure audits, and formal CII categorization support, please visit **[run-as-daemon.ru](https://run-as-daemon.ru)**. We offer commercial consulting services to help you navigate 187-FZ requirements and build secure, compliant infrastructure.
