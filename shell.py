import Titran

while True:
		text = input('basic > ')
		result, error = Titran.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)