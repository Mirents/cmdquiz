import random, os

filename = "question.txt"
numstring = 0
corr_answer = 0
wrong_answers = []
answered = []
ex = True
simbol = '$'

clear = lambda: os.system('clear')

def generatenumquestion():
	while True:
		r = random.randint(1, numstring) - 1
		#print('random is ' + str(r))
		if  len(answered) != len(listquestion):
			if r not in answered:
				#print('random generate: ' + str(r))
				answered.append(r)
				return r
		else:
			return -1

def hello():
	clear()
	print('Викторина командной строки GNU/Linux')
	print('Для выхода ввести \'ex\'')
	print('Для помощи ввести \'--help\'\n')
	try:
		input("Нажмите Enter для продолжения")
	except KeyboardInterrupt:
		print()

def help():
	clear()
	print('Викторина командной строки GNU/Linux')
	print('Для выхода ввести \'ex\'')
	print('Помощь - ввести \'--help\'')
	print('В качестве вопросов используется файл \'question.txt\' в формате:')
	print('	вопрос' + simbol + 'ответ')
	print('На некоторые вопросы возможны разные правильные ответы, уточнять в файле \'question.txt\'')
	print('Но такие ситуации по возможности исключены или имеются подсказки.')
	print('По умолчанию использование каталогов начинается с \'./\', кроме директории /home.')
	try:
		inp = input('\nПродолжить: y \ n: ')
	except KeyboardInterrupt:
		return False
	if inp == 'n':
		return False
	else:
		return True

def showresult(flag_exit):
	clear()
	ans = len(answered)
	if not flag_exit:
		ans -= 1
	if ans != 0:
		pok = 100*corr_answer/ans
	else:
		pok = 0

	if pok >= 0 and pok < 40:
		pok = 'нужно подучить'
	elif pok >= 40 and pok < 80:
		pok = 'достойный результат'
	else:
		pok = 'отличный результат'
	print('Результаты')
	print('Правильных ответов: ' + str(corr_answer) + ' из ' + str(ans) + ' - ' + pok)
	inp = input('\nПосмотреть неправильные ответы: y \ n: ')
	if inp == 'y':
		for i in wrong_answers:
			print('Вопрос: ' + get_question(listquestion[i]) + '\nОтвет:' + get_answer(listquestion[i]))
	else:
		exit(0)

def get_question(string):
	return string.split(simbol)[0]

def get_answer(string):
	return string.split(simbol)[1].rstrip()

try:
	f = open(filename)
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
		ques = get_question(listquestion[res])
		answ = get_answer(listquestion[res])
	else:
		break

	while ex:
		clear()
		print('Вопрос {:3} из {:3}'.format(len(answered), numstring))
		print('Вопрос: ' + ques)
		try:
			command = input("	Ответ: ")
		except KeyboardInterrupt:
			print()
		if command.lower() == "ex".lower():
			ex = False
			break
		elif command == answ:
			corr_answer += 1
			print('Верно\n')
			break
		elif command == '--help':
			if not help():
				ex = False
				break
		elif len(command) != 0:
			print('Не верно. Правильный ответ: {}\n'.format(answ))
			wrong_answers.append(res)
			try:
				input("	Нажмите Enter")
				break
			except KeyboardInterrupt:
				break
	if not ex:
		break

# Показать результаты
showresult(ex)
