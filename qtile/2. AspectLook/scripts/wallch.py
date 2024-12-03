import random, os, subprocess

path = "/home/Dew/Pictures/.walls/"
count = 0

for file in os.scandir(path):
	if file.is_file():
		count += 1;
		
selected = random.randint(0,count)

file = path + str(selected) + ".jpg"

subprocess.run(["nitrogen","--set-zoom-fill",file])
subprocess.run(["bash","/home/Dew/.config/polybar/cuts/scripts/pywal.sh",file])
