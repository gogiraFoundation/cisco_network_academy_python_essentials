#!/bin/bash

# Paths to scripts
PYTHON_SCRIPT="utils/git-script.py"
NOTIFICATION_SCRIPT="./notification.py"

# Log and counter file paths
LOG_FILE="./utils/log/actions-log/git_actions.log"
COUNTER_FILE="./utils/log/counter-log/failure_counter.txt"

# Maximum number of allowed failures
MAX_FAILURES=35

# Ensure log directories exist
mkdir -p "$(dirname "$LOG_FILE")"
mkdir -p "$(dirname "$COUNTER_FILE")"

# Initialize the failure counter if it doesn't exist
if [ ! -f "$COUNTER_FILE" ]; then
    echo 0 > "$COUNTER_FILE"
fi

# Function to run the Python script and log output
run_python_script() {
    echo "$(date '+%Y-%m-%d %H:%M:%S'): Running script $PYTHON_SCRIPT..." >> "$LOG_FILE"
    python3 "$PYTHON_SCRIPT" >> "$LOG_FILE" 2>&1
    if [ $? -ne 0 ]; then
        FAILURE_COUNTER=$(($(cat "$COUNTER_FILE") + 1))
        echo $FAILURE_COUNTER > "$COUNTER_FILE"
        echo "$(date '+%Y-%m-%d %H:%M:%S'): Script failed. Failure count: $FAILURE_COUNTER" >> "$LOG_FILE"
    else
        echo "$(date '+%Y-%m-%d %H:%M:%S'): Script succeeded." >> "$LOG_FILE"
        FAILURE_COUNTER=0
        echo $FAILURE_COUNTER > "$COUNTER_FILE"
    fi
}

# Function to send a notification
send_notification() {
    echo "$(date '+%Y-%m-%d %H:%M:%S'): Sending notification - Script failed after $MAX_FAILURES attempts" >> "$LOG_FILE"
    python3 "$NOTIFICATION_SCRIPT" >> "$LOG_FILE" 2>&1
}

# Main execution
echo "starting operation"
run_python_script

# Check failure count
FAILURE_COUNTER=$(cat "$COUNTER_FILE")
if [ "$FAILURE_COUNTER" -ge "$MAX_FAILURES" ]; then
    send_notification
fi