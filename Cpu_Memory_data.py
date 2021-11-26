import psutil
import os 
import subprocess
import csv

try:
    interval = int(input("Set the interval in seconds: "))
except ValueError:
    print ("Try again but now try to use integers.")
    quit()
file = input(f"Type down the file directory: ")
if not os.path.isfile(file):
    print ("No such file/directory incorrect, please try again.")
    quit()
process = subprocess.Popen(file)
# getting the process ID to get the details
process_id = process.pid
print(f"\n PROCESS ID: {process_id}\n")
flag=True

# creating csv file to store data - file might be used later on visualize the data
with open("Cpu_Memory_data_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # headers
    writer.writerow(["CPU Usage", "Resident Set Size", "Virtual Memory Size","File Descriptors number"])
    while flag:
        # getting process details
        print (f"\nThe CPU usage is: {psutil.cpu_percent(interval)}%")
        memory_usage = psutil.Process(process_id)
        print(f"Current Resident Set Size: {memory_usage.memory_info().rss/1024} MB") 
        print(f"Current Virtual Memory Size” {memory_usage.memory_info().vms/1024} MB") 
        print(f"The number of file descriptors  : {memory_usage.num_fds()}\n")
        # saving the details in csv file
        writer.writerow([
            psutil.cpu_percent(interval),
            memory_usage.memory_info().rss/1024,
            memory_usage.memory_info().vms/1024,
            memory_usage.num_fds()])
        file.flush()

 

 #   /usr/lib/thunderbird/thunderbird