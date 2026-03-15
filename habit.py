import sys
from datetime import datetime


def start_session():
    habit = input("Habit: ")
    before = input("How do you feel before starting? ")

    start_time = datetime.now().isoformat()

    with open(".current_session", "w") as f:
        f.write(f"{habit}\n")
        f.write(f"{before}\n")
        f.write(f"{start_time}\n")

    print("Session started.")

def end_session():
    print("Ending habit session...")

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