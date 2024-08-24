Set WshShell = CreateObject("WScript.Shell" )
WshShell.Run chr(34) & "BATCH_FILE_LOCATION" & Chr(34), 0
Set WshShell = Nothing