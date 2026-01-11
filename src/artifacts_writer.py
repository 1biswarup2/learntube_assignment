from pathlib import Path

ARTIFACT_DIR = Path("artifacts")
ARTIFACT_DIR.mkdir(exist_ok=True)


def write_questions_md(clarification):
    content = "# Clarifying Questions\n\n"
    for q in clarification.clarifying_questions:
        content += f"- {q}\n"

    content += "\n## Assumptions\n\n"
    for a in clarification.assumptions:
        content += f"- {a}\n"

    content += "\n## Interpreted Requirement\n\n"
    content += clarification.interpreted_requirement + "\n"

    (ARTIFACT_DIR / "questions.md").write_text(content)


def write_workflow_md(workflow):
    content = "# Activity Workflow\n\n"
    content += "## Prompt\n\n"
    content += workflow.prompt + "\n\n"

    content += "## Steps\n\n"
    for i, step in enumerate(workflow.steps, 1):
        content += f"{i}. {step}\n"

    content += "\n## Rubric\n\n"
    for k, v in workflow.rubric.items():
        content += f"- **{k}**: {v}\n"

    content += f"\n**Time Limit:** {workflow.max_time_minutes} minutes\n"

    (ARTIFACT_DIR / "workflow.md").write_text(content)


def write_qa_plan_md(qa_plan):
    content = "# Quality Control Plan\n\n"

    content += "## Automated Checks\n\n"
    for check in qa_plan.automated_checks:
        content += f"- {check}\n"

    content += "\n## Sampling Strategy\n\n"
    content += qa_plan.sampling_strategy + "\n"

    content += "\n## PII Handling\n\n"
    content += qa_plan.pii_handling + "\n"

    (ARTIFACT_DIR / "qa_plan.md").write_text(content)
