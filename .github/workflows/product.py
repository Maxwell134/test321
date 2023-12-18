import signal
import time

def handler(signum, frame):
    print("Timeout reached. Exiting...")
    exit(1)

# Set the timeout in seconds
timeout = 300

# Register the signal handler
signal.signal(signal.SIGALRM, handler)
signal.alarm(timeout)

try:
    # Your main script logic goes here
    print("Executing main script logic...")
    time.sleep(10)  # Simulating some long-running task
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Cancel the alarm (disable the timeout)
    signal.alarm(0)
