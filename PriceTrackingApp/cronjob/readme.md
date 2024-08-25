# How the cronjob dir is structured - and what are its files

I made this file to make this whole cron-job thing a bit more lightweight for the team. Perhaps useful too for instructors.

## `job.bat` & `job_wrapper.vbs`

These file work together to make the insertion of the command in the create_task() less painful (i.e. for Windows to like it)
`job.bat` tells cmd to run the written commands in different lines (otherwise having it within the python script way cause problems of syntax)
`job_wrapper.vbs` this is a "visual basic script" - Its a -deprecated- programming language. I am only using it to "turn-off" the display of the cmd when
it runs the cron-job, otherwise it will flash on the user's pc (and we dont like that). I copied the code from here: 
'https://stackoverflow.com/questions/411247/running-a-cmd-or-bat-in-silent-mode#:~:text=Add%20a%20comment-,15,Follow,-answered%20Jan%2015`

## `trackmazon_task`

(Previously `cron_price_tracking_and_email_notif.py`)
This is Violeta's and Leyla's full logic of what the cron-job will run.

## `task_scheduler.py`

Here lies the functions that will interact with Window's built-in Task Scheduler through the Command Prompt (cmd).
I separated to make a direct boundary from what it is internal code interaction and code that is interacting with external programms, like this is.

## `utils.py`

In this file I have put some code to interacts with the boundary (i.e. `task_scheduler.py`) and the cron-job logic (i.e. `cron_price_tracking_and_email_notif.py`)
