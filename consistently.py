a = '123'
b = '123'
c = '789'

def check_pass(pass1, pass2):
	if pass1 == pass2:
		print("Password is ok")
		return True
	else:
		print("Password is Error")
		return False

print(check_pass(a, b))
print(check_pass(b, c))