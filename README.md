# PDDL-Implementation

This directory contains the implementation of PDDL for the phishing attack and the ransomware attack.

# Installition of the Planner

To run the code, you need to install the metric-ff planner from the given link. All the detailed information is written there for the installation of the metric-ff planer. 
link:https://github.com/afaqinayat/metric-ff-crossplatform/blob/main/README.md#metric-ff

the information about the Fast-Downward planner
https://www.fast-downward.org/

.pddl files are used by both planner

# How to run the Planner

After the planner is set up, you can use the Python script, which runs the planner and the .pddl file. Phishing and ransomware are both modeled separately.

To run the . pddl files, run the metric-ff_planner.py file. This will help you test whether your .pddl files are working or not.

For the planner Fast-Downwad, run the script_run_planner files, and you can also change the search algorithm to find the plans.
 # Classification
 For the keyword match, the keyword_approach file needs to be run.
For the classification of the attack steps using OpenAI, you need to run the new_modified_version.py. 

# Controls mapping

Control mapping files have controls that are common from both control frameworks, NIST and ISO 27001 which are used for malware. This will provide the recommended controls.








