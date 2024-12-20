import os
import subprocess

def run_fast_downward(domain_file, problem_file, planner_path="./downward"):
    """
    Run the Fast Downward planner and display the output in the console.
    """
    # Define the planner command
    command = [
        os.path.join(planner_path, "/home/afaq/downward/fast-downward.py"),  # Path to the planner script
        domain_file,
        problem_file,
        "--search",
        "eager_greedy([ff()])"  # Example heuristic
        #"astar(hmax())"
    ]

    print(f"Running Fast Downward planner...")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print both stdout and stderr for debugging
    print("Planner Output (stdout):")
    print(result.stdout)

    print("Planner Error Output (stderr):")
    print(result.stderr)

    # Check if the planner ran successfully
    if result.returncode != 0:
        raise RuntimeError(f"Planner failed with error:\n{result.stderr}")
    
    # Output the plan
    print("Planner Output (plan steps):")
    print(result.stdout)

# Main execution
if __name__ == "__main__":
    # Specify the domain and problem files
    domain_file = "/home/afaq/downward/DomainPAG.pddl"  # Replace with your domain file
    problem_file = "/home/afaq/downward/ProblemPAG.pddl"  # Replace with your problem file
    planner_path = "/home/afaq/downward"  # Path to the Fast Downward planner

    try:
        # Step 1: Run the Fast Downward planner and display the output
        run_fast_downward(domain_file, problem_file, planner_path)

    except Exception as e:
        print(f"Error: {e}")
