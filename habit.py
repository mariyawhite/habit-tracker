import sys

def start_session():
    print("Starting habit session...")

def end_session():
    print("Ending habit session...")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python habit.py [start|end]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "start":
        start_session()
    elif command == "end":
        end_session()
    else:
        print("Unknown command")