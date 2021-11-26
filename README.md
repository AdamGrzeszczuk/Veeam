# Veeam
##Technical assessment for Veeam job application - Python



### Technical Task
Select any one problem from the list and solve it by writing a program in one of these programming languages:
Python 
C/C++
C#
We recommend using standard libraries where appropriate. No need to make another implementation of well-known algorithms.
Solutions should be uploaded to GitHub or GitLab platform.



### Problem 1
Implement a program that will launch a specified process and periodically (with a provided time interval) collect the following data about it:
CPU usage (percent);
Memory consumption: Working Set and Private Bytes (for Windows systems) or Resident Set Size and Virtual Memory Size (for Linux systems);
Number of open handles (for Windows systems) or file descriptors (for Linux systems).
Data collection should be performed all the time the process is running. Path to the executable file for the process and time interval between data collection iterations should be provided by user. Collected data should be stored on the disk. Format of stored data should support automated parsing to potentially allow, for example, drawing of charts.

Solution:
File: Cpu_Memory_data.py


### Problem 2
Implement a program that synchronizes two folders: source and replica. The program should maintain a full, identical copy of destination folder at replica folder.
Requirements:
Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;
Synchronization should be performed periodically;
File creation/copying/removal operations should be logged to a file and to the console output;
Folder paths, synchronization interval and log file path should be provided using the command line arguments.

Solution:
File: replica.py
Arguments:
- interval in seconds (interger),
- source directory,
- destination directory (+ destination folder - will be created if doesn't exist),
- log file directory + log file name.		

ex.: python3 replica.py interval src_dir dst_dir log_dir


### Problem 3
Unfortunatelly I was not able to complete the 3rd problem due to limited knowledge related the subject itself. 

I would appreciate any kind of feedback.
Thank you, 
Adam
