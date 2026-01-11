# 📊 Spec-to-Assessment Workflow Generator (Multi-Agent MVP)

This repository contains a minimal, end-to-end multi-agent system that converts a semi-structured dataset requirement into:

- Clarifying questions & assumptions

- A validated dataset schema

- A learner-facing assessment workflow

- A quality control (QC) plan

- A runnable demo that collects responses and exports data

The project is built as part of a Spec-to-Assessment Workflow Generator assignment.

# 🎯 What this project demonstrates

- Translating fuzzy requirements into clear specifications

- Designing a multi-agent workflow with structured handoffs

- Creating validated data collection pipelines

- Shipping a small but working MVP within a tight timebox

- This is not a large product, but a focused system design + execution exercise.

# 🧠 High-level Architecture
Requirement JSON
      ↓
Requirement Analyst Agent
      ↓
Schema Architect Agent
      ↓
Assessment / Activity Designer Agent
      ↓
QA / Risk Agent
      ↓
CLI Demo → Dataset Export (JSONL)


## Each agent produces structured outputs, which are persisted as artifacts.

📁 Repository Structure
learntube_assignment/
├── src/
│   ├── agents/
│   │   ├── requirement_analyst.py
│   │   ├── schema_architect.py
│   │   ├── activity_designer.py
│   │   └── qa_agent.py
│   ├── artifact_writer.py
│   ├── orchestrator.py
│   └── demo.py
├── requirements/
│   └── phishing_requirement.json
├── artifacts/
│   ├── questions.md
│   ├── workflow.md
│   └── qa_plan.md
├── export/
│   └── dataset.jsonl
├── README.md
└── .gitignore

# ⚙️ Setup Instructions
## 1️⃣ Prerequisites

- Python 3.9+

- Conda or virtualenv (recommended)

## 2️⃣ Create environment (optional but recommended)
- conda create -n learntube python=3.10
- conda activate learntube

## 3️⃣ Install dependencies
- pip install pydantic


(No external APIs are required for the current version.)

## ▶️ How to Run the Demo

From the project root directory, run:

- python -m src.demo

What happens when you run this:

- The requirement JSON is loaded

- All agents are executed in sequence

- Markdown artifacts are generated:

1. artifacts/questions.md

2. artifacts/workflow.md

3. artifacts/qa_plan.md

A sample scenario is shown in the CLI

You enter responses as a learner

The response is exported to:

- export/dataset.jsonl

# 📄 Generated Artifacts

The system produces the following outputs:

1. questions.md
Clarifying questions, assumptions, and interpreted requirement

2. workflow.md
Learner-facing activity flow, prompts, and rubric

3. qa_plan.md
Quality control strategy, automated checks, and risk handling

# export/dataset.jsonl
Sample dataset records generated from demo runs

All records include minimal traceability metadata:

- task_id

- created_at

- session_id

- domain

- version

# 🔁 Switching the Requirement ( basically this flow is usable with any input requirement ):

To run the pipeline on a different requirement:

- Add a new JSON file under requirements/

- Update the file path in src/demo.py

Re-run:

- python -m src.demo


The same pipeline works across different domains.

# 🚀 Future Improvements (LLM-Powered Enhancements)

This MVP intentionally uses deterministic logic to keep the system simple and reproducible.
In future iterations, Large Language Models (LLMs) can be leveraged to make the system more dynamic and autonomous:

Possible Enhancements

1. LLM-generated clarifying questions & assumptions

2. Dynamic schema generation from natural-language requirements

3. Auto-generated learner prompts and rubrics

4. LLM-assisted QA checks (inconsistency detection, reasoning quality)

5. Cost & throughput estimation agent

6. Retry/repair loops for invalid structured outputs

LLMs would be integrated behind strict JSON contracts and validation, preserving reliability while increasing flexibility.



✅ One-line Summary

A minimal, multi-agent system that turns dataset requirements into executable assessment workflows and validated datasets.
