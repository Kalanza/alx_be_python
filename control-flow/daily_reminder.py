task = input("Enter your task description. ")
priority = input("Enter your task's priority (high, medium, low) ").lower()
time_bound = input("Is the task time-bound(yes or no) ").lower()

match priority:
    case 'high':
      reminder = f'Critical Reminder: {task} (Priority: high)'
    case 'medium':
      reminder = f'Reminder: {task} (Priority: medium)'
    case 'low':
      reminder = f'Low-priority Reminder: {task} (Priority: low)'

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# Final Output
print(reminder)