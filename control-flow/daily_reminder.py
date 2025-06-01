# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that should be completed today."
        else:
            reminder += "."
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " with a time constraint."
        else:
            reminder += "."
    case _:
        reminder = "Invalid priority level entered. Please use high, medium, or low."

# Print the customized reminder
if priority in ["high", "medium", "low"]:
    action_required = " Immediate action is required!" if (priority == "high" and time_bound == "yes") else ""
    print(f"\nReminder: {reminder}{action_required}")
else:
    print(f"\n{reminder}")