#ALGORITHM
#algorithm 1 - look ahead
#MOON > WOLF
#WOON no
#MOLN no
#MOOF no
#parse through all 4 characters, swapping them until one of the old characters is the same as a new character
#that character is now locked and cannot be swapped except in the most dire of cases (dead end)
#if the parsing fails, do a second layer of testing (begin cycling)
#MOON
#BOON
#boon fail (if you fail DST one level into manual alphabet search, move back one level)
#GOON
#DST always comes first
#GOOF!
#GOLF!
#WOLF!

#RAIN > CRAB
#DST fail
#AAIN
#DST fail
#BAIN

#how it will work:
#every word is an object that stores two things: the word itself and a set/list of 

#MOON
#WOON MOLN MOON MOOF
#AOONs
#BOON!
#BOLN BOON BOOF
import sys 
import re

class Word(object):
	global word
	global tree

	def __init__(self, worde):
		self.word = worde
	def get_word(self):
		return self.word

#for i in range(65,26+64):
#	print("{0} {1}".format(i-64, chr(i)))

#Precondition: replace char in word of index with letter
#Returns: modified word
class WordSorter(object):

	global english_words

	def swap_letter(self, word, letter, index):
		if len(letter) > 1:
			print("you can only swap in one letter")
			return
		if isinstance(index, int) == False:
			print("your index isn't an integer")
			return
		try:
			word = list(word)
			word[index] = letter
			word = "".join(word)
		except IndexError:
			print("index passed is out of bounds")
			return
		return word
	#Param: word to be tested
	#Returns: whether the word is part of the english language 
	def is_english_word(self, word):
		return word.lower() in self.english_words

	#Precondition: For each letter of word, see if replacing that letter of the word with the letter at the same index in the target word produces a real english word.
	#Returns: the new word (if successful) or nil
	def direct_sub_test(self, word, targetWord):
		word.word = word.word.lower()
		print(word.word)
		targetWord.word = targetWord.word.lower()
		print(targetWord.word)
		print("{0} {1}".format(len(word.word),len(targetWord.word)))
		if len(word.word) != len(targetWord.word):
			print("cannot compare words of different lengths")
			return
		s_word = word.word
		s_tword = targetWord.word
		print("{0} {1}".format(s_word, s_tword))
		for i in range(0, len(word.word)):
			temp = self.swap_letter(s_word, s_tword[i], i)
			if self.is_english_word(temp):
				return temp
		return None

	def __init__(self):
		with open("C:\\Users\\Jordan\Documents\\Programming\\english_words.txt") as word_file:
			self.english_words = set(word.strip().lower() for word in word_file)

	#main func test
	def main(self):
		word_size = 'test'
		bword = Word(worde = "moon")
		tword = Word(worde = "goof")
		print(self.direct_sub_test(bword, tword))

		while isinstance(word_size, int) == False:
			word_size = input('How long will the words be?')
			try:
				word_size = int(word_size)
				break
			except ValueError:
				print("sry m8 u dun fukd up. gibe number") 
		input_word = input('Base word: ')
		while len(input_word) != word_size:
			print("try again m8. wrong word length")
			input_word = input('Base word: ')
		input_word2 = input('Arrival word: ')
		while len(input_word2) != word_size:
			print("try again m8. wrong word length")
			input_word2 = input("Arrival word:")
		base_word = Word(worde = input_word)
		target_word  = Word(worde = input_word2)

wordSort = WordSorter()
wordSort.main()