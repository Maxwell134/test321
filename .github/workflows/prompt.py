import pty, select
from inquirer import confirm

def main():
    with pty.openpty() as (master_fd, slave_fd):
        proceed = confirm(message="Do you want to proceed further?", tty=slave_fd)  # Use slave_fd as the tty argument for the prompt

        if proceed:
            print("Proceeding...")
        else:
            print("Stopping workflow.")
            # Use subprocess to execute a command to cancel the workflow
            # (e.g., `subprocess.run(['gh', 'workflow', 'cancel', ...])`)

if __name__ == "__main__":
    main()
