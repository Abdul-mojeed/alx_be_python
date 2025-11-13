# daily_reminder.py

# Prompt for user inputs
task = input("Enter a task: ")
priority = input("Enter the priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Process the task based on priority
match priority.lower():
    case "high":
        reminder = f"Your task '{task}' is a high priority task."
    case "medium":
        reminder = f"Your task '{task}' is a medium priority task."
    case "low":
        reminder = f"Your task '{task}' is a low priority task."
    case _:
        reminder = f"Your task '{task}' has an unknown priority level."

# Check if the task is time-sensitive
if time_bound.lower() == "yes":
    reminder += " That requires immediate attention today!"

# Display the customized reminder
print(reminder)
