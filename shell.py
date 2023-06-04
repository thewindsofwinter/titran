import Titran

while True:
		text = input('Titran > ')
		result, error = Titran.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)