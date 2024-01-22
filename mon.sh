#!/bin/bash

cd /home/veeru

# Define the path to the paft.log file
log_file="./paft.log"

# Function to get the current timestamp of the file
get_file_timestamp() {
  stat -c %Y "$log_file"
}


# Loop to check the timestamp every 5 seconds
while true; do
  current_timestamp=$(date +%s)
  file_timestamp=$(get_file_timestamp)
  time_difference=$((current_timestamp - file_timestamp))
  
  # Check if the timestamp hasn't changed for 3 minutes (180 seconds)
  if [ "$time_difference" -ge 300 ]; then
    echo `date`" : paft.log timestamp hasn't changed for 5 minutes. Killing the process - START"
    
    # Add the command to kill the process here, e.g., "kill <process_id>"
    # Replace <process_id> with the actual process ID you want to kill.
    rm paft.log
    sudo /bin/systemctl stop paft
    sudo /bin/systemctl start paft

    echo `date`" : paft.log timestamp hasn't changed for 5 minutes. Killing the process - COMPLETED"

    # Exit the script after killing the process
    exit 0
  fi
  
  echo `date`" : paft running normally"
  # Sleep for 60 seconds before checking again
  sleep 180
done
