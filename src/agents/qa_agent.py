from src.models import QAPlan


def run(requirement: dict) -> QAPlan:
    return QAPlan(
        automated_checks=[
            "Schema validation",
            "Enum value validation",
            "PII regex scan (email, phone)",
            "Empty or generic response detection"
        ],
        sampling_strategy="10% random spot-check + gold set comparison",
        pii_handling="Reject or flag records containing detected PII"
    )
