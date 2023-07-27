$commands = @(
    'cd "C:\program files (x86)\Pulse-Eight\USB-CEC Adapter"',
    'echo "on 0" | .\cec-client.exe -s COM3',
    'echo "as" | .\cec-client.exe -p 1 -s COM3',
    'echo "on 0" | .\cec-client.exe -s COM4',
    'echo "as" | .\cec-client.exe -p 1 -s COM4',
    'echo "on 0" | .\cec-client.exe -s COM5',
    'echo "as" | .\cec-client.exe -p 1 -s COM5',
    'echo "on 0" | .\cec-client.exe -s COM6',
    'echo "as" | .\cec-client.exe -p 1 -s COM6'
)

foreach ($command in $commands) {
    Invoke-Expression $command
}