Set WshShell = CreateObject("WScript.Shell" )
WshShell.Run chr(34) & "C:\Users\evasa\Documents\Git\CFG-Group-6\PriceTrackingApp\cronjob\job.bat" & Chr(34), 0
Set WshShell = Nothing