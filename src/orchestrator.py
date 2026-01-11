from src.agents import (
    requirement_analyst,
    schema_architect,
    activity_designer,
    qa_agent
)
from src.artifacts_writer import (
    write_questions_md,
    write_workflow_md,
    write_qa_plan_md
)


def run_pipeline(requirement: dict):
    clarifications = requirement_analyst.run(requirement)
    dataspec = schema_architect.run(requirement)
    workflow = activity_designer.run(requirement)
    qa_plan = qa_agent.run(requirement)

    write_questions_md(clarifications)
    write_workflow_md(workflow)
    write_qa_plan_md(qa_plan)

    return {
        "clarifications": clarifications,
        "dataspec": dataspec,
        "workflow": workflow,
        "qa_plan": qa_plan
    }
