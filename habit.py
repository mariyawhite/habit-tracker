import sys
import os
from datetime import datetime
import csv


def start_session():
    if os.path.exists(".current_session"):
        print("Error: session already active.")
        print("Run `python3 habit.py end` first.")
        return

    habit = input("Habit: ")
    feeling_before = input("How do you feel before starting? ")

    start_time = datetime.now().isoformat()

    with open(".current_session", "w") as f:
        f.write(f"{habit}\n")
        f.write(f"{feeling_before}\n")
        f.write(f"{start_time}\n")

    print("Session started.")

def end_session():
    if not os.path.exists(".current_session"):
        print("Error: no active session.")
        print("Run `python3 habit.py start` first.")
        return

    activity = input("What did you do? ")
    feeling_after = input("How do you feel after finishing? ")

    end_time = datetime.now().isoformat()

    with open(".current_session", "r") as f:
        habit = f.readline().strip()
        feeling_before = f.readline().strip()
        start_time = f.readline().strip()

    start_dt = datetime.fromisoformat(start_time)
    end_dt = datetime.fromisoformat(end_time)
    duration = (end_dt - start_dt).total_seconds() / 60

    file_exists = os.path.exists("habit_log.csv")

    with open("habit_log.csv", "a", newline="") as log:
        writer = csv.writer(log)

        if not file_exists:
            writer.writerow([
                "habit",
                "feeling_before",
                "feeling_after",
                "activity",
                "start_time",
                "end_time",
                "duration_minutes"
            ])

        writer.writerow([
            habit,
            feeling_before,
            feeling_after,
            activity,
            start_time,
            end_time,
            round(duration, 1)
        ])

    os.remove(".current_session")

    print("Session logged.")

commands = {
    "start": start_session,
    "end": end_session
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python habit.py [start|end]")
        sys.exit(1)

    command = sys.argv[1]

    if command in commands:
        commands[command]()
    else:
        print("Unknown command")

