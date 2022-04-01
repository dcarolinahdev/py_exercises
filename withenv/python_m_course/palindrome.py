# Lambda form
# palindrome = lambda param: param == param[::-1]

# Second try-except block code
# def palindrome(param):
# 	try:
# 		if len(param) == 0:
# 			raise ValueError("You can't type an empty string")
# 		return param == param[::-1]
# 	except ValueError as ve:
# 		print(ve)
# 		return False

# print(palindrome('ana'))
# print(palindrome('tucson'))

# First try-except block code
# try:
# 	print(palindrome(''))
# except TypeError:
# 	print("You only can type strings")

# With assert statements
def palindrome(param):
	assert len(param) > 0, "You can't type an empty string"
	return param == param[::-1]

print(palindrome(''))
