const button = document.getElementById("assessButton");
const useCaseInput = document.getElementById("useCase");
const results = document.getElementById("results");
const errorMessage = document.getElementById("error");

const overallStatus = document.getElementById("overallStatus");
const requirements = document.getElementById("requirements");
const risks = document.getElementById("risks");
const actions = document.getElementById("actions");


button.addEventListener("click", async () => {

    errorMessage.textContent = "";

    let useCase;

    try {
        useCase = JSON.parse(useCaseInput.value);
    } catch {
        errorMessage.textContent = "Invalid JSON.";
        return;
    }

    button.disabled = true;
    button.textContent = "Assessing...";

    try {

        const response = await fetch("/assess", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                use_case: useCase
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Assessment failed.");
        }

        displayAssessment(data);

    } catch (error) {

        errorMessage.textContent = error.message;

    } finally {

        button.disabled = false;
        button.textContent = "Assess Use Case";
    }
});


function displayAssessment(data) {

    results.classList.remove("hidden");

    overallStatus.textContent = data.overall_status;

    overallStatus.className =
        data.overall_status === "PASS"
            ? "pass"
            : "unknown";

    requirements.innerHTML = "";

    data.assessments.forEach(item => {

        const element = document.createElement("div");

        element.className = "requirement";

        element.innerHTML = `
            <div class="requirement-header">
                <h3>${item.requirement_id}</h3>

                <span class="status ${item.status.toLowerCase()}">
                    ${item.status}
                </span>
            </div>

            <p>
                <strong>Reasoning:</strong>
                ${item.reasoning}
            </p>

            <p>
                <strong>Evidence:</strong>
                ${item.evidence}
            </p>

            <p>
                <strong>Recommended Action:</strong>
                ${item.recommended_action}
            </p>
        `;

        requirements.appendChild(element);
    });


    risks.innerHTML = "";

    data.risks.forEach(risk => {

        const li = document.createElement("li");

        li.textContent = risk;

        risks.appendChild(li);
    });


    actions.innerHTML = "";

    data.recommended_actions.forEach(action => {

        const li = document.createElement("li");

        li.textContent = action;

        actions.appendChild(li);
    });
}