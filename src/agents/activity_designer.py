from src.models import WorkflowSpec


def run(requirement: dict) -> WorkflowSpec:
    prompt = (
        "Read the following scenario carefully and answer the questions below."
    )

    steps = [
        "Determine the nature of the scenario",
        "Provide required classifications",
        "Justify your reasoning briefly"
    ]

    rubric = {
        "correct_classification": "Correctly identifies scenario intent",
        "evidence_quality": "Uses valid evidence from the text",
        "reasoning": "Clear and concise rationale"
    }

    return WorkflowSpec(
        prompt=prompt,
        steps=steps,
        rubric=rubric,
        max_time_minutes=requirement["constraints"]["max_time_per_task_minutes"]
    )
