name_file_in = "question.txt"
name_file_to = "to.txt"
text = ''
simbol = '$'

try:
	f_in = open(name_file_in)
	text = list(f_in)
	f_to = open(name_file_to, 'w')
except FileNotFoundError:
	print("Error, file not found")
	exit(0)

for i in text:
	string = i.rstrip().split('|')
	if len(string) > 2:
		f_to.write(string[0] + simbol + string[1] + '|' + string[2] + '\n')
	else:
		f_to.write(string[0] + simbol + string[1] + '\n')

f_in.close()
f_to.close()