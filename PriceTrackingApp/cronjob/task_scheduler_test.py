import unittest
from unittest import mock

from cronjob.task_scheduler import create_task


class TaskSchedulerTest(unittest.TestCase):
    @mock.patch('subprocess.run')
    def test_create_task(self, mock_subprocess_run):

        mock_task_name = "test_task"
        mock_command = "foo.exe"

        result = create_task("test_task", ("minute", "1"), "foo.exe")

        mock_subprocess_run.assert_called_with(f"schtasks /Create /SC MINUTE /MO 1 /TN {mock_task_name} /TR {mock_command}")


if __name__ == '__main__':
    unittest.main()
