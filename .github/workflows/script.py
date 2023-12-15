import sys
from inputimeout import inputimeout, TimeoutOccurred

def main():
    try:
        user_input = inputimeout(prompt="Enter something: ", timeout=10)
        print(f"User input: {user_input}")
    except TimeoutOccurred:
        print("Timeout occurred. Exiting.")

if __name__ == "__main__":
    main()
