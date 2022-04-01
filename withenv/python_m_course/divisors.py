def divisors(num):
	try:
		if num < 0:
			raise ValueError("You must type a positive number")
		divisors = [i for i in range(1, num + 1) if num % i == 0]
	except ValueError as ve:
		print(ve)
		return False

def run():
	try:
		num = int(input("Write a number: "))
		print(divisors(num))
		print("The end")
	except ValueError:
		print("You must type a number")

if __name__ == '__main__':
	run()