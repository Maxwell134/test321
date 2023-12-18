from github_actions import GitHubActions

github = GitHubActions()

proceed_or_abort = github.core.prompt(
    "Do you want to proceed with the action? (Enter 'proceed' or 'abort'):"
)

if proceed_or_abort.lower() == "proceed":
    github.core.set_output("exit_code", 0)
    print("Proceeding with the action...")
else:
    github.core.set_output("exit_code", 1)
    print("Aborting the action as per user input.")

