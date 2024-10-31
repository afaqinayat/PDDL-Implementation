import openai
import subprocess

# Set your OpenAI API key
# openai.api_key = 'sk-proj-EbjgdKmmAq1xjSVPM4j1T3BlbkFJs3lLGE05hZE0MLNzbN7O'

# selected_engine_id = "gpt-3.5-turbo-0125"

#--------------------------------------------------
#Modified Section
#--------------------------------------------------
client = openai.OpenAI(

    #api_key="sk-proj-EbjgdKmmAq1xjSVPM4j1T3BlbkFJs3lLGE05hZE0MLNzbN7O",
    api_key="sk-proj-8ApId7GDXVTF57nlXTOTT3BlbkFJFeotypJICpLaWwhoXxiT",
    max_retries=0,
)
#------------------------------------------------------

# Function to classify an action using a specified engine
def classify_action(action_name):
    # Create a prompt for the OpenAI model
    

    # Use the OpenAI API to classify the action
    # response = openai.Completion.create(
    #     engine=engine_id,
    #     prompt=prompt,
    #     max_tokens=1
    # )


#--------------------------------------------------
#Modified Section
#--------------------------------------------------
    category="Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Act on Objective"

    response=client.with_options(max_retries=5).chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Classify each cyber action in the following:{action_name} in most relevant one category from this cyberattack life cycle list: {category}. In output i want dictionary of the all the actions like x: 'y', here x is the index of action and y is classification result from given list",
            }
        ],
        model="gpt-3.5-turbo",
    )

    # print(response.choices[0].message.content.strip())

#------------------------------------------------------
    

    # Get the classification from the response
    classification = response.choices[0].message.content.strip()

    return classification

# Function to classify actions in a plan using a specified engine
def classify_actions(plan_steps):
    classified_plan = []
    for step in plan_steps:
        # Check if the line contains a colon before splitting
        if ":" in step:
            # Split the step string using colon ':' and get the action name
            action_name = step.split(":")[1].strip()
            # Classify the action using the specified engine
            # lifecycle_stage = classify_action(action_name)
            classified_plan.append(action_name)
    print(classified_plan)
    return classify_action(plan_steps)

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
            # Set start_index to the line after this heading
            break

    if start_index is None:
        raise RuntimeError("Plan steps not found in the output")

    # Extract plan steps
    plan_steps = plan_lines[start_index:]

    for step in plan_steps:
      print(step)


    # Classify plan steps using the specified engine
    classified_plan = classify_actions(plan_steps)

    return classified_plan

# Example usage
domain_file = "/home/afaq/Downloads/metric-ff-crossplatform/DomainPAG.pddl"
problem_file = "/home/afaq/Downloads/metric-ff-crossplatform/ProblemPAG.pddl"

# Run Metric-FF and classify the plan using the specified engine
classified_plan = run_metric_ff_and_classify_plan(domain_file, problem_file)

# Print the classified plan
print("Classified Plan using OpenAI:")
print(classified_plan)
