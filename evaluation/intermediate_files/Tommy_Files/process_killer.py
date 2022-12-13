"""Terminate all processes for a user-given software."""

import os
import signal

def process():
    """Find and terminate all processes."""
    # Ask user for the name of process
    name = input("Enter Software Name to Kill: ")
    try:

            # iterating through each instance of the process
        for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
            fields = line.split()

            # extracting Process ID from the output
            pid = fields[0]

            # terminating process
            os.kill(int(pid), signal.SIGKILL)
        print("Processes Successfully terminated")

    except(PermissionError):
        print(f"Unable to Kill '{name}'")

process()