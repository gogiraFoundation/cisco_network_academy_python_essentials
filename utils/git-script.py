#!/usr/bin/env python3

import os
import subprocess
import sys
from datetime import datetime


# Path to the local repository directory
REPO_PATH = '..'

# Check if the repository path exists
if not os.path.exists(REPO_PATH):
    print(f"Error: Directory '{REPO_PATH}' does not exist.")
    sys.exit(1)

# Change to the repository directory
os.chdir(REPO_PATH)


def log_message(message):
    """
    Logs a message with a timestamp.
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")


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
    # Ensure git is available
    log_message("Checking for git installation...")
    git_version, err = execute_command("git --version")
    if err:
        log_message(f"Error: Git is not installed or not available. Details: {err}")
        return

    log_message(f"Git version detected: {git_version}")

    # Check current branch
    log_message("Checking current git branch...")
    branch_output, err = execute_command("git branch --show-current")
    if err:
        log_message(f"Error: Failed to determine the current branch. Details: {err}")
        return

    current_branch = branch_output.strip()
    log_message(f"Current branch: {current_branch}")

    # Check for changes in the repository
    log_message("Checking for changes in the repository...")
    out, err = execute_command("git status --porcelain")
    if out:
        log_message("Changes detected. Proceeding with commit and push operations...")

        # Add all changes
        out, err = execute_command("git add .")
        if err:
            log_message(f"Error during 'git add': {err}")
            return

        # Commit the changes
        commit_message = "Auto-commit changes"
        out, err = execute_command(f"git commit -m \"{commit_message}\"")
        if err:
            log_message(f"Error during 'git commit': {err}")
            return
        log_message("Commit successful.")

        # Push changes to the current branch (or 'testnet' branch)
        log_message(f"Pushing changes to branch '{current_branch}'...")
        out, err = execute_command(f"git push origin {current_branch}")
        if err:
            log_message(f"Error while pushing to branch '{current_branch}': {err}")
        else:
            log_message("Changes successfully pushed.")
    else:
        log_message("No changes detected. Nothing to commit or push.")


if __name__ == "__main__":
    try:
        log_message("Starting git actions...")
        git_actions()
    except Exception as e:
        log_message(f"Unexpected error: {e}")
