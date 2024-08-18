#!/bin/bash

# Executable path
CURRENT_DIR="$(pwd)"
EXECUTABLE_NAME="price_tracker.exe"  #CHANGE NAME TO FINAL EXECUTABLE NAME!
EXECUTABLE_PATH="$CURRENT_DIR/$EXECUTABLE_NAME"

# Check if the executable exists
if [ ! -f "$EXECUTABLE_PATH" ]; then
    echo "Executable not found at $EXECUTABLE_PATH."
    exit 1
fi

# Set up cron job to run at boot and to pass on the cron_job=true argument when running executable
(crontab -l 2>/dev/null; echo "@reboot $EXECUTABLE_PATH cron_job=True") | crontab -

echo "Cron job set up to run $EXECUTABLE_PATH on system reboot with cron_job=true."