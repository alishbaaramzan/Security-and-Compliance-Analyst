import json

from openai import OpenAI

from .models import Assessment
from .requirements import REQUIREMENTS


SYSTEM_PROMPT = """
You are an AI security assessment analyst.

Your job is to perform the INITIAL assessment of an internal AI use case.

Assess the submitted use case against EVERY requirement provided to you.

Rules:

1. Assess every requirement exactly once.
2. PASS only when the submitted information provides sufficient evidence
   that the requirement is satisfied.
3. FAIL when the submitted information indicates that the requirement
   is not satisfied.
4. UNKNOWN when there is not enough information to determine whether
   the requirement is satisfied.
5. Never invent facts that are not present in the submitted use case.
6. Treat UNKNOWN as a gap requiring follow-up.
7. Explain your reasoning using evidence from the submitted use case.
8. Provide a concrete recommended action for every FAIL or UNKNOWN.
9. If a third-party AI service is used, pay particular attention to
   AI-002 and AI-006.
10. If the use case is high-risk, AI-008 requires additional review.
11. This is an initial assessment, not final security approval.
12. Do not approve deployment solely because most requirements pass.

Return the assessment using the required structured format.
"""


class SecurityAnalyst:
    def __init__(self, client: OpenAI | None = None):
        self.client = client or OpenAI()

    def assess(self, use_case: dict) -> Assessment:
        prompt = {
            "use_case": use_case,
            "requirements": REQUIREMENTS,
        }

        response = self.client.responses.parse(
            model="gpt-5.6-luna",
            instructions=SYSTEM_PROMPT,
            input=json.dumps(prompt),
            text_format=Assessment,
        )

        if response.output_parsed is None:
            raise ValueError("The model did not return a valid assessment.")

        return response.output_parsed