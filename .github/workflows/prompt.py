from inquirer import confirm

def main():
  proceed = confirm(message="Do you want to proceed further?")
  if proceed:
    print("Proceeding...")
  else:
    print("Stopping workflow.")
    # Use subprocess to execute a command to cancel the workflow
    # (e.g., `gh workflow cancel ...`)

if __name__ == "__main__":
  main()
