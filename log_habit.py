import json
import sys
from datetime import date

def load_data():
    with open("habits.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("habits.json", "w") as f:
        json.dump(data, f, indent=2)

def log_habit(habit_name):
    data = load_data()
    today = str(date.today())

    if habit_name not in data:
        data[habit_name] = []

    if today not in data[habit_name]:
        data[habit_name].append(today)
        print(f"Logged '{habit_name}' for {today}")
    else:
        print(f"'{habit_name}' already logged today")

    save_data(data)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        habit = sys.argv[1]
        log_habit(habit)
    else:
        data = load_data()
        habits = list(data.keys())

        if not habits:
            print("No habits yet. Run: python3 log_habit.py <habit_name>")
        else:
            print("Pick a habit:")
            for i, h in enumerate(habits, 1):
                print(f"{i}. {h}")
            print(f"{len(habits) + 1}. New habit")

            choice = input("> ")
            choice = int(choice)

            if choice == len(habits) + 1:
                new_habit = input("New habit name: ")
                log_habit(new_habit)
            else:
                log_habit(habits[choice - 1])