import shutil
import time
import os
import sys
import logging
import datetime

# user inputs
try:
	interval = sys.argv[1]
	src = sys.argv[2]
	if src[-1] != "/":
		src = src + "/"
	if not os.path.exists(src):
		print("Source path doesn't exist. Provide correct directory.")
		quit()
	dst = sys.argv[3]
	if dst[-1] != "/":
		dst = dst + "/"
	log_file = sys.argv[4]	
except IndexError:
	print("""
		Please provide correct arguments (space separated):
		interval in seconds (interger),
		source directory,
		destination directory (+ destination folder - will be created if doesn't exist),
		log file directory + log file name.		

		ex.: python3 replica.py interval src_dir dst_dir log_dir
		""")
	quit()

# config for log file and adding user data to log file/console status
logging.basicConfig(filename=log_file, level=logging.DEBUG)

logging.debug(f"Source path: {src}")
logging.debug(f"Destination path: {dst}")
logging.debug(f"Time interval: {interval}s")
logging.debug(f"Log File location: {log_file}\n")
print(f"Source path: {src}")
print(f"Destination path: {dst}")
print(f"Time interval: {interval}s")
print(f"Log File location: {log_file}\n")

interval =int(interval)

# checking if destination folder exists, if not creates one
if not os.path.exists(dst):
	os.mkdir(dst)

while True:
	src_items = os.listdir(src)
	dst_items = os.listdir(dst)

# checks if destination file is in source file, if not file is removed
	for item in dst_items:
		if item not in src_items:
			os.remove(dst + item)
			logging.debug(f"{item} removed from destination directory - {datetime.datetime.now()}")
			print(f"{item} removed from destination directory - {datetime.datetime.now()}")
# checks if file exists in destination folder. if so, then it logs overwriting the file, 
# if not, it logs creating the file
	for item in src_items:
		if os.path.exists(dst + item):
			logging.debug(f"{item} overwritten in destination directory - {datetime.datetime.now()}.")
			print(f"{item} overwritten in destination directory - {datetime.datetime.now()}.")
			shutil.copy(src + item, dst)
		else:
			logging.debug(f"{item} created in destination directory - {datetime.datetime.now()}.")
			print(f"{item} created in destination directory - {datetime.datetime.now()}.")
			shutil.copy(src + item,  dst)
	print (f"\n")
	logging.debug("\n")
	time.sleep(interval)


