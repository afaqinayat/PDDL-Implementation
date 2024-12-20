# PDDL-Implementation

This directory contains the implementation of PDDL for the phishing attack and the ransomware attack.

# Installition of the Planner

To run the code, you need to install the metric-ff planner from the given link. All the detailed information is written there for the installation of the metric-ff planer. 
link:https://github.com/afaqinayat/metric-ff-crossplatform/blob/main/README.md#metric-ff

the information about the Fast-Downward planner
https://www.fast-downward.org/

.pddl files are used by both planner

# How to run the Planner

After the setup of the planner, you can use the Python script, which runs the planner and the .pddl file . Phishing and ransomware are both modeled separately.

To run the . pddl files, run the metric-ff_planner.py file. This will help you test whether your .pddl files are working or not.

For the planner Fast-Downwad, you can change the search algorithm to find the plans.
 
Then, for the classification of the attack steps, you need to run the new_modified_version.py. 

# Controls mapping

Control mapping files have controls that are common from both control frameworks NIST and ISO 27001 and are used for malware.








