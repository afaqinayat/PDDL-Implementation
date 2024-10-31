# Define the list of controls
list_of_controls = [
    {"Name": "Information security roles and responsibilities", "Price": "X", "Efficacy": "Medium", "Framework": "ISO/NIST", "Killchain_phases": ["Act on Objective"]},
    {"Name": "Contact with special interest groups", "Price": ["1188$", "144$"], "Efficacy": "low", "Framework": "ISO/NIST", "Killchain_phases": ["Reconnaissance"]},
    {"Name": "Human Resources Security", "Price": "X", "Efficacy": ["Low", "Medium"], "Framework": "ISO/NIST", "Killchain_phases": ["Reconnaissance", "Exploitation", "Act on Objective'"]},
    {"Name": "Information security awareness, education, and training", "Price": "660$", "Efficacy": ["Medium", "High"], "Framework": "ISO/NIST", "Killchain_phases": ["Reconnaissance", "Exploitation"]},
    {"Name": "Acceptable use of assets", "Price": "600$", "Efficacy": "Medium", "Framework": "ISO/NIST", "Killchain_phases": ["Exploitation"]},
    {"Name": "Access control policy", "Price": ["87.96$", "1848$"], "Efficacy": "High", "Framework": "ISO/NIST", "Killchain_phases": ["Exploitation"]},
    {"Name": "User access provisioning", "Price": "X", "Efficacy": "High", "Framework": "ISO/NIST", "Killchain_phases": ["Exploitation"]},
    {"Name": "Physical and environmental security", "Price": ["10,000$", "1248$"], "Efficacy": ["Low", "Medium", "Low", "Medium"], "Framework": "ISO/NIST", "Killchain_phases": ["Exploitation", "Installation", "Command and Control", "Act on Objective"]},
    {"Name": "Protection from malware", "Price": "69.90$", "Efficacy": ["High", "High"], "Framework": "ISO/NIST", "Killchain_phases": ["Delivery", "Installation"]},
    {"Name": "Information backup", "Price": ["85$"], "Efficacy": ["Low", "High"], "Framework": "ISO/NIST", "Killchain_phases": ["Installation", "Act on Objective"]},
    {"Name": "Controls against malware", "Price": ["399$", "99.99$", "60$"], "Efficacy": ["High", "High", "High"], "Framework": "ISO/NIST", "Killchain_phases": ["Delivery", "Exploitation", "Installation"]},
    {"Name": "Event logging", "Price": ["1800$", "9600$", "10400$"], "Efficacy": ["Medium", "High", "High"], "Framework": "ISO/NIST", "Killchain_phases": ["Reconnaissance", "Installation", "Command and Control (C2)"]},
    {"Name": "Technical vulnerability management", "Price": ["2275$", "7000$"], "Efficacy": ["Medium", "Low", "High"], "Framework": "ISO/NIST", "Killchain_phases": ["Command and Control", "Weaponization", "Exploitation"]},
    {"Name": "Information security continuity", "Price": "X", "Efficacy": "High", "Framework": "ISO/NIST", "Killchain_phases": ["Act on Objective"]},
]

# Open the .txt file and read the contents
with open("phases_based_classification.txt", "r") as f:
    lines = f.readlines()

# Create a dictionary to map Killchain_phases to controls
killchain_phase_to_controls = {}
for control in list_of_controls:
    for phase in control["Killchain_phases"]:
        if phase not in killchain_phase_to_controls:
            killchain_phase_to_controls[phase] = []
        killchain_phase_to_controls[phase].append(control)

# Parse the contents of the text file
killchain_phases_in_file = []
for line in lines:
    line = line.strip()
    if line:
        parts = line.split(": ")
        if len(parts) == 2:
            # Strip trailing commas and single quotes
            killchain_phase = parts[1].strip("',")
            killchain_phases_in_file.append(killchain_phase)

# Find the matching controls for each Killchain_phase in the file
for phase in killchain_phases_in_file:
    if phase in killchain_phase_to_controls:
        print(f"Killchain phase: {phase}")
        for control in killchain_phase_to_controls[phase]:
            print(f"  Control: {control['Name']}, Efficacy: {control['Efficacy']}, Price: {control['Price']}")
    else:
        print(f"Killchain phase: {phase} has no corresponding controls.")

