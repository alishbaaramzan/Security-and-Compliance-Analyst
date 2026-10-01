from .requirements import REQUIREMENTS


EVIDENCE_MAP = {
    "AI-001": [
        "business_owner",
    ],
    "AI-002": [
        "data_processed",
        "data_sensitivity",
        "ai_provider",
        "security_controls",
    ],
    "AI-003": [
        "human_oversight",
    ],
    "AI-004": [
        "logging_monitoring",
    ],
    "AI-005": [
        "access_controls",
    ],
    "AI-006": [
        "ai_provider",
        "third_party_security_assessment",
    ],
    "AI-007": [
        "intended_use",
        "limitations",
    ],
    "AI-008": [
        "risk_level",
        "additional_review",
    ],
}


# python functions

def get_requirements() -> list[dict]:
    """Return all security requirements."""
    return REQUIREMENTS


def get_required_evidence(requirement_id: str) -> dict:
    """Return the evidence needed to assess a requirement."""

    if requirement_id not in EVIDENCE_MAP:
        raise ValueError(f"Unknown requirement: {requirement_id}")

    return {
        "requirement_id": requirement_id,
        "required_evidence": EVIDENCE_MAP[requirement_id],
    }


def get_use_case_field(use_case: dict, field: str) -> dict:
    """Retrieve a field from the submitted use case."""

    if field not in use_case:
        return {
            "field": field,
            "found": False,
            "value": None,
        }

    return {
        "field": field,
        "found": True,
        "value": use_case[field],
    }


# tool definitions

TOOLS = [
    {
        "type": "function",
        "name": "get_requirements",
        "description": (
            "Retrieve the complete list of AI security requirements "
            "AI-001 through AI-008."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "get_required_evidence",
        "description": (
            "Determine what evidence is needed to assess a specific "
            "AI security requirement."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "requirement_id": {
                    "type": "string",
                    "description": "Requirement ID, for example AI-001.",
                }
            },
            "required": ["requirement_id"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "get_use_case_field",
        "description": (
            "Retrieve a specific field from the submitted AI use case. "
            "Use this to obtain evidence needed for the assessment."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "field": {
                    "type": "string",
                    "description": "Name of the use-case field to retrieve.",
                }
            },
            "required": ["field"],
            "additionalProperties": False,
        },
        "strict": True,
    },
]