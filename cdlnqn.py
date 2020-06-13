import random

filename = "question.txt"
numstring = 0
yesanswer = 0
answer = []

def generatenumquestion():
	while True:
		r = random.randint(1, numstring) - 1
		#print('random is ' + str(r))
		if  len(answer) != len(listquestion):
			if r not in answer:
				#print('random generate: ' + str(r))
				answer.append(r)
				return r
		else:
			return -1

def hello():
	print('Викторина командной строки GNU/Linux')
	print('Для выхода ввести \'ex\'')
	print('Для помощи ввести \'--help\'\n')

def help():
	print('Викторина командной строки GNU/Linux')
	print('Для выхода ввести \'ex\'')
	print('Помощь - ввести \'--help\'')
	print('В качестве вопросов используется файл \'question.txt\' в формате:')
	print('	вопрос|ответ')
	print('На некоторые вопросы возможны разные правильные ответы, уточнять в файле \'question.txt\'')
	inp = input('\nПродолжить y \ n: ')
	if inp == 'n':
		exit(0)

def showresult():
	print('Правильных ответов: ' + str(yesanswer) + ' из ' + str(len(listquestion)))
	exit(0)

try:
	f = open(filename)
	with open(filename, 'r') as f:
		listquestion = list(f)
	numstring = len(listquestion)
	hello()
except FileNotFoundError:
	print("Error, file not found")
	exit(0)
finally:
	f.close()

while True:
	res = generatenumquestion()
	if res != -1:
		quest = listquestion[res].split('|')[0]
		ques = quest.split('\n')[0]
		answt = listquestion[res].split('|')[1]
		answ = answt.split('\n')[0]
		#print(answ)
	else:
		break

	while True:
		print('	Вопрос: ' + ques)
		command = input("		Ответ: ")
		if command.lower() == "ex".lower():
			exit(0)
		elif command == answ:
			yesanswer += 1
			print('Правильный ответ\n')
			break
		elif command == '--help':
			help()
		elif len(command) != 0:
			print('Неправильный ответ\n')
			break

showresult()