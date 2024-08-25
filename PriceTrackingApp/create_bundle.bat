pyinstaller --name="Trackmazon" ^
    --add-data="back_end\list_common_user_agents.txt:back_end" ^
    --add-data="cronjob\job_logs:cronjob\job_logs" ^
    --add-data="cronjob\job.bat:cronjob" ^
    --add-data="cronjob\job_wrapper.vbs:cronjob" ^
    --clean ^
    --icon future_icon.ico ^
    main.py