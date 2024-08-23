import datetime
import os.path

from cronjob.task_scheduler import create_task


def track_sent_mail(sent_mail):
    current_timestamp = datetime.datetime.now().isoformat()[:-7].replace(':', '-')

    log_file = open(os.path.join("cronjob", "job_logs", f"job_result_{current_timestamp}.html"), 'w')
    log_file.write(sent_mail['HTMLPart'])
    log_file.close()


def create_updates_job():
    # return create_task("trackmazon_update_task", ("MINUTE", "1"), os.path.abspath(os.path.join("cronjob","job.bat")))
    return create_task("trackmazon_update_task", ("MINUTE", "1"), os.path.abspath(os.path.join("cronjob","job_wrapper.vbs")))
