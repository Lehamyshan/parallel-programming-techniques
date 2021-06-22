import asyncio
from time import sleep

a = '123'
b = '123'
c = '789'

async def check_pass(pass1, pass2, t):
	if pass1 == pass2:
		await asyncio.sleep(t)
		print("Password is ok")
		return True
	else:
		await asyncio.sleep(t)
		print("Password is Error")
		return False

loop = asyncio.get_event_loop()
tasks = [
	loop.create_task(check_pass(a, b, 5)), 
	loop.create_task(check_pass(b, c, 1))]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()