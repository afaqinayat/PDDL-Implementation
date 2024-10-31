
import subprocess

def run_metric_ff_and_capture_plan(domain_file, problem_file):
    # Define Metric-FF executable path
    ff_executable = "/home/afaq/Downloads/metric-ff-crossplatform/ff-v1.0"

    # Run Metric-FF and capture output
    with subprocess.Popen([ff_executable, "-o", domain_file, "-f",problem_file], stdout=subprocess.PIPE) as process:
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
    return plan_steps


domain_file = "/home/afaq/Downloads/metric-ff-crossplatform/DomainPAG.pddl"
problem_file = "/home/afaq/Downloads/metric-ff-crossplatform/ProblemPAG.pddl"

plan_steps = run_metric_ff_and_capture_plan(domain_file, problem_file)
print("Plan Steps:")
for step in plan_steps:
    print(step)
