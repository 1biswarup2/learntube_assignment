import json
from datetime import datetime
from uuid import uuid4

from src.orchestrator import run_pipeline


def main():
    with open("requirements/phishing_requirement.json") as f:
        requirement = json.load(f)

    artifacts = run_pipeline(requirement)

    print("\n--- Scenario ---")
    scenario = "Your account is suspended. Click the link to verify."
    print(scenario)

    response = {}
    for field in requirement["outputs_needed"]:
        response[field] = input(f"{field}: ")

    record = {
        "task_id": str(uuid4()),
        "created_at": datetime.utcnow().isoformat(),
        "session_id": str(uuid4()),
        "domain": requirement["domain"],
        "version": "v1",
        "scenario_text": scenario,
        **response
    }

    with open("export/dataset.jsonl", "a") as f:
        f.write(json.dumps(record) + "\n")

    print("\n✅ Record written to export/dataset.jsonl")


if __name__ == "__main__":
    main()
