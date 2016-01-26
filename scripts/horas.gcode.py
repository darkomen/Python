import os

directory = os.listdir(".")
files = []
time = [0,0]
for f in directory:
	if f.endswith(".gcode"):
		files.append(f)


for gcode in files:
	with open(gcode,'r') as infile:
		lines = infile.readlines()

	dic = (str(lines[3])[13:-1].replace('hours','').replace(' minutes','').split('  '))

	if len(dic) == 1:
		dic.append(dic[0])
		dic[0] = 0
	time[0], time[1] = time[0] + int(dic[0]), time[1] + int(dic[1])

print("{} horas y {} minutos".format(time[0], time[1]))

