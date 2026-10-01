# AI Security & Compliance Analyst

An AI-powered agent that performs an initial security and compliance assessment of internal AI use cases.

The goal of this project was not to build a chatbot that simply answers security questions. Instead, I wanted to build a small tool-using agent that can investigate a use case,
determine what evidence it needs, retrieve that evidence, assess predefined security requirements, identify gaps and risks and return a structured assessment.

## Requirements
The agent assesses the use case against these eight requirements:

AI-001	AI application must have an identified business owner.

AI-002	Sensitive information must not be submitted to an AI system without appropriate controls.

AI-003	AI-generated outputs used for business decisions must have appropriate human oversight.

AI-004	AI application must maintain appropriate logging and monitoring.

AI-005	AI application must have defined access controls.

AI-006	Third-party AI models and services must undergo appropriate security assessment.

AI-007	AI application must have documented intended use and limitations.

AI-008	High-risk AI use cases must undergo additional review before deployment.


Each requirement is assessed as:

PASS: sufficient evidence indicates that the requirement is satisfied.
FAIL: available evidence indicates that the requirement is not satisfied.
UNKNOWN: there is not enough information to make a determination.

## Workflow
The agent follows an iterative tool-calling loop.

Step 1 Understand the task

Step 2 Determine the requirements: The agent can call get_requirements(). This retrieves the complete list of AI-001 through AI-008.This keeps the requirements separate from the model's own general knowledge.

Step 3 Determine required evidence: For a specific requirement, the agent can call get_required_evidence(requirement_id). The agent can then determine which information it needs to inspect.

Step 4 Retrieve evidence: The agent can call get_use_case_field(field). The agent can repeat this process for other fields and requirements.

Step 5 Reason over the evidence: Once it has sufficient evidence, the model determines whether each requirement is PASS, FAIL, UNKNOWN. It also provides reasoning and identifies the evidence supporting its conclusion.

Step 6 Identify risks and actions: The agent produces identified risks, gaps, requirement-specific actions,overall recommended actions.

Step 7 Validate the output: The final response is parsed into a Pydantic model.

## Output Screenshot
<img width="929" height="463" alt="image" src="https://github.com/user-attachments/assets/9af2f916-684d-4887-881d-9059f5cfec4b" />

<img width="379" height="416" alt="image" src="https://github.com/user-attachments/assets/101fbd53-d813-427c-941b-cd8e2d5a89e7" />

<img width="370" height="400" alt="image" src="https://github.com/user-attachments/assets/515e7594-2495-4f95-b770-770af5b6ca45" />

<img width="395" height="407" alt="image" src="https://github.com/user-attachments/assets/4a497032-539d-4c53-bae9-eff794858b0a" />
