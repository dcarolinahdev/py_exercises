import random, os

def read_data(filepath="./files/data.txt"):
	words = []
	with open(filepath, "r", encoding="utf-8") as f:
		for line in f:
			words.append(line.strip().upper())
	return words

def set_index_dict(word):
	letter_index_dict = {}
	for idx, letter in enumerate(word):
		# if letter is not in dict -> append an empty list with letter as key
		if not letter_index_dict.get(letter):
			letter_index_dict[letter] = []
		# append the index with the letter as key
		letter_index_dict[letter].append(idx)
	return letter_index_dict

def print_game_status(guessing_letters, footer):
	header = "¡Guess the word!\n"
	for e in guessing_letters:
		header += e + " "
	print(header+"\n"+footer)

def run():
	data = read_data(filepath="./files/data.txt")
	current_word = random.choice(data)
	cw_tolist = [letter for letter in current_word]
	guessing_letters = ["_"] * len(cw_tolist)
	letter_index_dict = set_index_dict(current_word)
	
	# ----- GAME -----
	while True:
		os.system("clear")
		print_game_status(guessing_letters, "")

		# try to guess and validate char
		letter = input("Write a letter: ").strip().upper()
		assert letter.isalpha(), "You only can write letters"
		# replace if necessary
		if letter in cw_tolist:
			for idx in letter_index_dict[letter]:
				guessing_letters[idx] = letter
		# end of the game
		if "_" not in guessing_letters:
			os.system("clear")
			print_game_status(guessing_letters, "¡You win!")
			break

if __name__ == '__main__':
	run()
