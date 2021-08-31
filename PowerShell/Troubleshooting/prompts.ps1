
#Log Function
Function Log {
    Get-Date | Out-File -FilePath $PSScriptRoot\DailyLog.txt -Append
    Get-ChildItem $PSScriptRoot\ -Filter *.log | Out-File -FilePath $PSScriptRoot\Requirements1\DailyLog.txt -Append
        
    }
    
    #List-Files Function
    Function List-Files {
        Param(
            [string]$Path = "$PSScriptRoot\" #Creates a string variable
        )
        
        $logFiles = Get-ChildItem $Path | Sort-Object | Format-Table #Gets childeren items in path and sorts them into a table.
        $logFiles | Out-File $PSScriptRoot\C916contents.txt	#Updates the C916 file with a list of files in the Requirements folder.
        
    }
    #Counter function for number 3. 
    Function Counter {
        Get-Counter -Counter "\Processor(_Total)\% Processor Time" -SampleInterval 5 -MaxSamples 4 #Grabs the Get-Counter for the processor
        Get-Counter -Counter "\Memory\Available MBytes" -SampleInterval 5 -MaxSamples 4 #Grabs the Get-Counter for the avaliable memory.
    
    }
    #Variable for the while loop. This is the number selection. Variable must be defined prior to starting the loop.
    $number = 0
    
    #Start of Try block for the while loop and a print statement. Will not exit until the 5 key is pressed.
    Try 
    {
        while ( $number -ne 5)
        {
            write-host ' Please review the following list and select a number to run a script. 
    
    1. List the log files within the Requirements1 folder and outputs it to a text file called DailyLog.txt.
    2. List the files inside the Requirements1 folder and outputs it to a text file called C916contents.txt.
    3. List the current CPU %, Processor Time, and physical memory usage and prints it to the terminal.
    4. Show the running processes and prints it to the terminal in order from greatest to least in processor time.
    5. Stop the script.
    '
            $n = Read-Host -Prompt '>> Select a Number'
            switch -Exact ($n)
            {
                1 {Log} #This executes the log function above and appends the DailyLog.txt file.
                2 {List-Files} #This executes the List-Files function above and lists the files inside the Reqirements1 folder.
                3 {Counter}  # Counts CPU Processor time and Physical memory use. SampleInterval is how many seconds inbetween each capture and -MaxSample is how many to collect.
                4 {Get-Process | Select-Object Name, ID, TotalProcessorTime | Sort-Object TotalProcessorTime -Descending | Out-GridView} #This gets the current running processes and sorts it in another window.
                5 {$number = 5}
            }
        }
    }
    Catch [System.OutOfMemoryException] 
    {
        Write-Host "A system out of memeory exception has occured."
    } 