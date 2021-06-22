from threading import Thread


a = '123'
b = '123'
c = '789'

storage = {}

def check_pass(pass1, pass2, store, key):
	if pass1 == pass2:
		storage[key] = 1 
		print("Password is ok")
		return True
	else:
		storage[key] = 0
		print("Password is Error")
		return False

th_1 = Thread(target = check_pass, args = (a, b, storage, 'one'))
th_2 = Thread(target = check_pass, args = (a, c, storage, 'two'))

th_1.start()
th_2.start()

th_1.join()
th_2.join()