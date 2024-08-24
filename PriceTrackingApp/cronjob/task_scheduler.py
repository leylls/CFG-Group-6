"""
wrapper implementation for schtasks.exe, windows task scheduler
docs: https://learn.microsoft.com/en-us/windows/win32/taskschd/schtasks
"""
import os.path
import subprocess

# schtasks /Create /SC MINUTE /MO 1 /TN test /TR c:\windows\system32\notepad.exe


def create_task(name, frequency, command):
# TODO: @eva to write pydoc for this function to explain the parameters

    SC = None
    MO = None

    match frequency:
        case (schedule, modifier):
            # TODO: eva to add the other options for scedule to ensure it is valid
            if schedule.upper() not in ["MINUTE", "SECOND", "DAYS"] or (not modifier.isnumeric()):
                raise ValueError("uh oh")
            else:
                SC = schedule.upper()
                MO = modifier
        case _:
            raise ValueError("uh oh")

    # Ensuring to delete any other (possible) pre-existing task with the same name
    subprocess.run(f"schtasks /Delete /TN {name} /F")

    process_to_execute = f"schtasks /Create /SC {SC} /MO {MO} /TN {name} /TR \"{command}\""
    # TODO to delete the print-out of "SUCCESS"
    return subprocess.run(process_to_execute)

# TODO: (if eva has time) write a delete_task function that takes a task's name and deletes it, to clean up the program :)

def delete_cronjob_task(taskname):
    process_to_execute = f"schtasks /Delete /TN {taskname} /F"
    # TODO to delete the print-out of "SUCCESS"
    return subprocess.run(process_to_execute)

# schtasks /Delete /TN trackmazon_update_task /F
