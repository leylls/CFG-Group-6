"""
wrapper implementation for schtasks.exe, windows task scheduler
docs: https://learn.microsoft.com/en-us/windows/win32/taskschd/schtasks
"""
import os.path
import subprocess



def create_task(name, frequency, command):
    """
    Creates a TaskScheduler task with the given parameters.
    :param name:
    :param frequency:
    :param command:
    :return:
    """

    SC = None
    MO = None

    match frequency:
        case (schedule, modifier):
            if schedule.upper() not in ["DAILY", "MINUTE"] or not modifier.isnumeric():
                raise ValueError("uh oh")
            else:
                SC = schedule.upper()
                MO = modifier
        case _:
            raise ValueError("uh oh")

    # Ensuring to delete any other (possible) pre-existing task with the same name
    subprocess.run(f"schtasks /Delete /TN {name} /F", stdout=subprocess.DEVNULL)

    process_to_execute = f"schtasks /Create /SC {SC} /MO {MO} /TN {name} /TR \"{command}\""
    return subprocess.run(process_to_execute, stdout=subprocess.DEVNULL)


def delete_cronjob_task(taskname):
    process_to_execute = f"schtasks /Delete /TN {taskname} /F"
    return subprocess.run(process_to_execute, stdout=subprocess.DEVNULL)

# schtasks /Delete /TN trackmazon_update_task /F
