import openai
import subprocess

# Set your OpenAI API key
client = openai.OpenAI(
    api_key="sk-proj-EbjgdKmmAq1xjSVPM4j1T3BlbkFJs3lLGE05hZE0MLNzbN7O",
    max_retries=0,
)

# Function to classify an action using the OpenAI model
def classify_action(action_name, context=""):
    # Create a prompt for the OpenAI model with more focus on context
    prompt = (
        f"Given the following context:\n\n{context}\n\n"
        f"Classify this specific action based on the cyberattack life cycle: '{action_name}'.\n"
        "Choose the most relevant stages from this list: Reconnaissance, Weaponization, Delivery, Exploitation, "
        "Installation, Command and Control, Act on Objective.\n"
        "Only provide the classification stages, do not repeat the action. Separate multiple stages with commas."
    )
    
    # Use the OpenAI API to classify the action
    response = client.with_options(max_retries=5).chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-3.5-turbo",
    )

    # Get the classification from the response
    classification = response.choices[0].message.content.strip()
    
    return classification

# Function to classify actions in a plan with additional context
def classify_actions(plan_steps):
    classified_plan = []
    for i, step in enumerate(plan_steps):
        # Check if the line contains a colon before splitting
        if ":" in step:
            # Split the step string using colon ':' and get the action name
            step_number, action_name = step.split(":", 1)
            action_name = action_name.strip()  # Remove any leading/trailing spaces
            
            # Create a context by combining previous steps to provide more information
            context = "\n".join(plan_steps[max(0, i-3):i])  # Take the previous 3 steps as context
            
            # Classify the action using the OpenAI model
            lifecycle_stage = classify_action(action_name, context)
            classified_plan.append(f"{step_number.strip()}: {action_name.strip()}, Classification: {lifecycle_stage}")
    return classified_plan

# Function to run Metric-FF and classify the plan
def run_metric_ff_and_classify_plan(domain_file, problem_file):
    # Define Metric-FF executable path
    ff_executable = "/home/afaq/Downloads/metric-ff-crossplatform/ff-v1.0"
    
    # Run Metric-FF and capture output with subprocess.Popen
    with subprocess.Popen([ff_executable, "-o", domain_file, "-f", problem_file], stdout=subprocess.PIPE) as process:
        plan_output, _ = process.communicate()
    
    # Decode output and split into lines
    plan_lines = plan_output.decode().splitlines()
    
    # Find the index of the line containing the plan steps
    start_index = None
    for i, line in enumerate(plan_lines):
        if "ff: found legal plan as follows" in line:
            start_index = i + 1
            break

    if start_index is None:
        raise RuntimeError("Plan steps not found in the output")
    
    # Extract plan steps
    plan_steps = plan_lines[start_index:]

    # Classify plan steps using the OpenAI model
    classified_plan = classify_actions(plan_steps)
    
    return classified_plan

# Example usage
domain_file = "/home/afaq/Downloads/metric-ff-crossplatform/DomainPAG.pddl"
problem_file = "/home/afaq/Downloads/metric-ff-crossplatform/ProblemPAG.pddl"

# Run Metric-FF and classify the plan using the OpenAI model
classified_plan = run_metric_ff_and_classify_plan(domain_file, problem_file)

# Print the classified plan
print("Classified Plan using OpenAI:")
for classification in classified_plan:
    print(classification)

