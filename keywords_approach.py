import subprocess

# Define the stages of the cyber attack lifecycle
cybersecurity_lifecycle = {
    "user-visits": "Reconnaissance",
    "user-opens": "Weaponization",
    "attacker-sends-email": "Delivery",
    "key-logger-activated": "Exploitation",
    "key-logger-installed ": "Installation",
    "attacker-intercepts": "Command and Control",
    "actions_on_objectives": "Actions on Objectives"
}


'''cybersecurity_lifecycle = {
     "Reconnaissance": ["visit", "scan", "gather", "enumerate"],
    "Weaponization": ["exploit", "deliver", "download", "craft"],
    "Delivery": ["send", "email", "attach", "transmit"],
    "Exploitation": ["exploit", "inject", "compromise", "execute"],
    "Installation": ["install", "execute", "load", "drop"],
    "Command and Control": ["connect", "communicate", "control", "intercept"],
    "Actions on Objectives": ["steal", "exfiltrate", "modify", "delete"]
}
'''
def classify_actions(plan_steps):
    classified_plan = []
    for step in plan_steps:
        # Check if the line contains a colon before splitting
        if ":" in step:
            # Split the step string using colon ':' and get the action name
            action_name = step.split(":")[1].strip()
            # Iterate through cybersecurity lifecycle keywords to classify the action
            lifecycle_stage = None
            for keyword, stage in cybersecurity_lifecycle.items():
                if keyword.lower() in action_name.lower():
                    lifecycle_stage = stage
                    break
            classified_plan.append((action_name, lifecycle_stage))
    return classified_plan



'''def classify_actions(plan_steps):
    classified_plan = []
    for step in plan_steps:
        # Check if the line contains a colon before splitting
        if ":" in step:
            # Split the step string using colon ':' and get the action name
            action_name = step.split(":")[1].strip()
            # Iterate through cybersecurity lifecycle keywords to classify the action
            lifecycle_stage = None
            
            for keyword, stage in cybersecurity_lifecycle.items():
                if keyword in action_name.lower():
                    lifecycle_stage = stage
                    break
            classified_plan.append((action_name, lifecycle_stage))
    return classified_plan

    '''

def run_metric_ff_and_classify_plan(domain_file, problem_file):
    # Define Metric-FF executable path
    ff_executable = "/home/afaq/Downloads/metric-ff-crossplatform/ff-v1.0"

    # Run Metric-FF and capture output
    with subprocess.Popen([ff_executable, "-o", domain_file, "-f", problem_file], stdout=subprocess.PIPE) as process:
        plan_output, _ = process.communicate()

    # Decode output and split into lines
    plan_lines = plan_output.decode().splitlines()

    # Find the index of the line containing the plan steps
    start_index = None
    for i, line in enumerate(plan_lines):
        if "ff: found legal plan as follows" in line:
            start_index = i + 1  # Set start_index to the line after this heading
            break

    if start_index is None:
        raise RuntimeError("Plan steps not found in the output")

    # Extract plan steps
    plan_steps = plan_lines[start_index:]

    # Classify plan steps
    classified_plan = classify_actions(plan_steps)
    return classified_plan

# Example usage
domain_file = "/home/afaq/Downloads/metric-ff-crossplatform/DomainPAG.pddl"
problem_file = "/home/afaq/Downloads/metric-ff-crossplatform/ProblemPAG.pddl"

classified_plan = run_metric_ff_and_classify_plan(domain_file, problem_file)


# Print the classified plan
print("Classified Plan:")
for action, stage in classified_plan:
    print(f"- {action} ({stage})")
