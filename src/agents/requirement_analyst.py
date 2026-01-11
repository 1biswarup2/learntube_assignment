from src.models import ClarificationOutput


def run(requirement: dict) -> ClarificationOutput:
    questions = [
        "Should multiple recommended actions be allowed?",
        "Are evidence spans expected to quote text verbatim?",
        "Is rubric grading automated or manual?",
        "What is the max length for free-text responses?"
    ]

    assumptions = [
        "Multiple recommended actions are allowed",
        "Evidence spans quote exact phrases",
        "Rubric grading is rule-based for MVP",
        "Free-text responses are limited to short paragraphs"
    ]

    interpreted = (
        f"This project collects structured learner judgments for "
        f"{requirement.get('domain')} scenarios under time constraints."
    )

    return ClarificationOutput(
        clarifying_questions=questions,
        assumptions=assumptions,
        interpreted_requirement=interpreted
    )
