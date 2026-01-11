from src.models import DataSpec


def run(requirement: dict) -> DataSpec:
    outputs = requirement["outputs_needed"]
    label_spaces = requirement.get("label_spaces", {})

    properties = {}
    required = []

    for field in outputs:
        if field in label_spaces:
            properties[field] = {
                "type": "string",
                "enum": label_spaces[field]
            }
        else:
            properties[field] = {"type": "string"}

        required.append(field)

    schema = {
        "type": "object",
        "required": required,
        "properties": properties
    }

    return DataSpec(
        schema=schema,
        version="v1",
        domain=requirement["domain"]
    )
