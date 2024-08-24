"""
wrapper implementation for schtasks.exe, windows task scheduler
docs: https://learn.microsoft.com/en-us/windows/win32/taskschd/schtasks
"""
import os.path
import subprocess
"""
schtasks /Create /SC MINUTE /MO 1 /TN test /TR c:\windows\system32\notepad.exe
"""

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


    process_to_execute = f"schtasks /Create /SC {SC} /MO {MO} /TN {name} /TR \"{command}\""
    return subprocess.run(process_to_execute)

# TODO: (if eva has time) write a delete_task function that takes a task's name and deletes it, to clean up the program :)

# schtasks /Delete /TN trackmazon_update_task /F


# TODO: delete below this line \/
def test_create_task_foo():
    #os.path.abspath("foo.py")
    mock_task_name = "write_test_file"
    # mock_command = f"C:\\Users\\evasa\\PycharmProjects\\CFGDegree\\Foundation_Exam\\PriceTrackingApp\\Scripts\\python.exe C:\\Users\\evasa\\Documents\\Git\\CFG-Group-6\\PriceTrackingApp\\cronjob\\foo.py"
    # mock_command = "C:\\Users\\evasa\\Documents\\Git\\CFG-Group-6\\PriceTrackingApp\\cronjob\\job.bat"
    mock_command = "C:\\Users\\evasa\\Documents\\Git\\CFG-Group-6\\PriceTrackingApp\\cronjob\\job_wrapper.vbs"

    create_task(mock_task_name, ("MINUTE", "1"), mock_command)

if __name__ == "__main__":
    test_create_task_foo()