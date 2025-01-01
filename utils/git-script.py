#!/usr/bin/env python3

import os
import subprocess
import sys


# Path to the local repository directory
REPO_PATH = '..'

# Check if the repository path exists
if not os.path.exists(REPO_PATH):
    print(f"Error: Directory '{REPO_PATH}' does not exist.")
    sys.exit(1)

# Change to the repository directory
os.chdir(REPO_PATH)


def execute_command(command):
    """
    Executes a shell command and returns the output or error.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return None, e.stderr.strip()


def git_actions():
    """
    Checks for changes in the repository, commits them, and pushes to the 'testnet' branch.
    """
    # check for git branch
    status = execute_command('git branch')
    print(f"Git Status: {status}")

    # Check for changes in the repository
    out, err = execute_command("git status --porcelain")
    if out:
        print("Changes detected. Proceeding with commit and push operations...")

        # Add all changes
        out, err = execute_command("git add .")
        if err:
            print(f"Error during 'git add': {err}")
            return

        # Commit the changes
        commit_message = "Auto-commit changes"
        out, err = execute_command(f"git commit -m \"{commit_message}\"")
        if err:
            print(f"Error during 'git commit': {err}")
            return
        print("Commit successful.")

        # Push changes to the 'testnet' branch
        out, err = execute_command("git push origin testnet")
        if err:
            print(f"Error while pushing to 'testnet': {err}")
        else:
            print("Changes successfully pushed to 'testnet'.")
    else:
        print("No changes detected. Nothing to commit or push.")


if __name__ == "__main__":
    try:
        print("Starting git actions...")
        git_actions()
    except Exception as e:
        print(f"Unexpected error: {e}")
