# Lambda form
# palindrome = lambda param: param == param[::-1]

def palindrome(param):
	return param == param[::-1]

print(palindrome('ana'))
print(palindrome('tucson'))

# First try-except block code
try:
	print(palindrome(1))
except TypeError:
	print("You only can type strings")