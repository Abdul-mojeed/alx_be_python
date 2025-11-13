# Daily Reminder Script

# Prompt user for task details
task = input("Enter your task for today: ")
priority = input("Enter the task's priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Display reminder message using a loop (runs once for demonstration)
while True:
    match priority:
        case "high":
            reminder = f"Your task '{task}' is HIGH priority. Make sure to focus on it first."
        case "medium":
            reminder = f"Your task '{task}' has MEDIUM priority. Try to complete it after high-priority tasks."
        case "low":
            reminder = f"Your task '{task}' is LOW priority. Handle it when you have spare time."
        case _:
            reminder = f"Your task '{task}' has an UNKNOWN priority level."

    # Adjust message if time-bound
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"

    # Print final customized reminder
    print(reminder)

    # Break loop after one run (you can remove this break to make it repeat)
    break
