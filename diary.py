import time
import os

dosya_ismi = "/home/burak/Desktop/python/diary.txt"
file = open(dosya_ismi, "a")
lines = []

def save():
	time_stamp = time.ctime()
	file.write(f"DATE:\t{time_stamp}\n\n")
	for line in lines:
		file.write(f"{line}\n")
	file.write("\n-------------------------\n\n")

print("Type exit / done / bitti to save your log")
print("Type cancel / iptal for exit without log")
print("Type open / ac for opening the log file")
print("Things i have done today:\n")
while True:
	line = input()
	if line == "exit" or line == "done" or line == "bitti":
		save()
		print("\nKayit tamamlandi")
		break
	elif line == "iptal" or line == "cancel":
		break
	elif line == "open" or line == "ac":
		os.system(f"sudo nano {dosya_ismi}")
		break
	else:
		lines.append(line)