#CSV writing

#!/usr/bin/env python3

import csv
import re

errors = {}
per_user = {}

with open('syslog.log') as file:
  lines = file.readlines()
  for line in lines:
    pattern = r"ticky: ([\w+]*):? ([\w' ]*) [\[[#0-9]*\]?]? ?\((.*)\)$"
    match = re.search(pattern, line)
    type, message, user = match.group(1), match.group(2), match.group(3)

    if user not in per_user:
      per_user[user] = {'INFO': 0,'ERROR': 0 }
    per_user[user][type] += 1
    if type=='ERROR':
      errors[message] = errors.get(message, 0) + 1

error_number_list = sorted(errors.items(), key=lambda item: item[1], reverse=True)
error_number_list.insert(0, ('Error', 'Count'))
error_users_list = sorted(per_user.items(), key=lambda item: item[0])
error_users_list.insert(0, ('Username', 'INFO', 'ERROR'))

with open('error_message.csv', 'w', newline='') as file:
  header = '{}, {}\n'.format(error_number_list[0][0], error_number_list[0][1])
  file.write(header)
  for key, value in error_number_list[1:]:
    line = '{}, {}\n'.format(key, value)
    file.write(line)

with open('user_statistics.csv', 'w', newline='') as file:
  header = '{}, {}, {}\n'.format(error_users_list[0][0], error_users_list[0][1], error_users_list[0][2])
  file.write(header)
  for key, value in error_users_list[1:]:
    line='{}, {}, {}\n'.format(key, value["INFO"], value["ERROR"])
    file.write(line)

# Multitasking with pool

#!/usr/bin/env python3

from multiprocessing import Pool
import os
import subprocess

src = "/home/student-04-253dc9278212/data/prod/"
dest = "/home/student-04-253dc9278212/data/prod_backup/"

os.getcwd()

folders = []
def run(directory):
  subprocess.call(["rsync", "-arq", src+directory, dest+directory])

for root, dirs, files in os.walk("/home/student-04-253dc9278212/data/prod/"):
  for folder in dirs:
    print(folder)
    folders.append(folder)

print(folders)

p = Pool(len(folders))
p.map(run, folders)

-------- Alternative --------

src = "/home/student-04-253dc9278212/data/prod"
dirs = next(os.walk(src))[1]

def backingup(dirs):
    dest = "/home/student-04-253dc9278212/data/prod_backup"
    subprocess.call(["rsync", "-arq", dirs, dest])


p = Pool(len(dirs))
p.map(backingup, dirs)

# PIL image editing

#!/usr/bin/env python3

import os
from PIL import Image

path = 'supplier-data/images/'

for file in os.listdir(path):
    if '.tiff' in file:
        img = Image.open(path + file).convert("RGB")
        filename = file.split('.')[0]
        img.resize((600, 400)).save(path + filename + '.jpeg' , 'jpeg')
# PSUTILS

#! /usr/bin/env python3

import os
import shutil
import psutil
import socket
from emails import generate_error_report, send_email
 
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    # return usage > 80
    return usage < 80
 
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
 
def check_available_memory():
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500
 
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'
 
to_be_checked = {
    check_cpu_usage(): "CPU usage is over 80%",
    check_disk_usage("/"): "Available disk space is less than 20%",
    check_available_memory(): "Available memory is less than 500MB",
    check_localhost(): "localhost cannot be resolved to 127.0.0.1"
}

error = False
for action, message in to_be_checked.items():
    if not action: 
        error_message = message
        error = True
if error:
    try:
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = "Error - {}".format(error_message)
        body = "Please check your system and resolve the issue as soon as possible"
        message = generate_error_report(sender, receiver, subject, body)
        send_email(message)
        print('test')
    except NameError:
        pass
        
        
