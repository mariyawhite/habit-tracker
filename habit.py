import sys

def start_session():
    print("Starting habit session...")

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