import random, os

filename = "question.txt"
numstring = 0
yesanswer = 0
answer = []
ex = True

clear = lambda: os.system('clear')

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
	clear()
	print('Викторина командной строки GNU/Linux')
	print('Для выхода ввести \'ex\'')
	print('Для помощи ввести \'--help\'\n')

def help():
	clear()
	print('Викторина командной строки GNU/Linux')
	print('Для выхода ввести \'ex\'')
	print('Помощь - ввести \'--help\'')
	print('В качестве вопросов используется файл \'question.txt\' в формате:')
	print('	вопрос|ответ')
	print('На некоторые вопросы возможны разные правильные ответы, уточнять в файле \'question.txt\'')
	print('Но такие ситуации по возможности исключены или имеются подсказки.')
	print('По умолчанию использование каталогов начинается с \'./\'.')
	inp = input('\nПродолжить y \ n: ')
	if inp == 'n':
		exit(0)

def showresult(flag_exit):
	ans = len(answer)
	if not flag_exit:
		ans -= 1
	pok = 100*yesanswer/ans
	if pok >= 0 and pok < 40:
		pok = 'нужно подучить'
	elif pok >= 40 and pok < 80:
		pok = 'достойно'
	else:
		pok = 'отлично'
	print('Правильных ответов: ' + str(yesanswer) + ' из ' + str(ans) + ' - ' + pok)
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

	while ex:
		#clear()
		print('Вопрос {:3} из {:3}'.format(len(answer), numstring))
		print('Вопрос: ' + ques)
		command = input("	Ответ: ")
		if command.lower() == "ex".lower():
			ex = False
			break
		elif command == answ:
			yesanswer += 1
			print('Верно\n')
			break
		elif command == '--help':
			help()
		elif len(command) != 0:
			print('Не верно. Правильный ответ: {}\n'.format(answ))
			#input("	Нажмите Enter")
			break
	if not ex:
		break

clear()
showresult(ex)
