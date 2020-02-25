# -*- coding: utf-8 -*-
# @Author: Tetiana Kravchuk
# @Date:   2020-02-23 21:12:30

import random
import linecache
import sys
import os


class game:
	def __init__(self):
		self.score = 4;
		self.current_word = []
		self.guessedLettersCount = 0
		self.guessedLetters = {}
		self.state = False


	def start(self):
		self.state = True
		self.guessedLettersCount = 0
		self.score = 4
		self.current_word = list(self.getWord(random.randint(0, self.getDictionarySize())))
		self.guessedLetters = []


	def getDictionarySize(self):
		input = open(os.getcwd()+"/dictionary.txt")
		count = 0
		for line in input:
			count += 1
		return count

	def getWord(self, number):
		return linecache.getline('dictionary.txt', number)

	def isCorrect(self, letter):

		# if letter is already guessed
		if letter in self.guessedLetters:
			return []

		# if letter is correct and was't guessed before
		if letter in self.current_word:

			letterIndexes = []			
			#get all indexes of letter
			for i in range(0, len(self.current_word)):
				if self.current_word[i] == letter:
					letterIndexes.append(i)
					self.guessedLettersCount+=1
					self.guessedLetters.append(letter)
			
			# if word is fully guessed
			if self.guessedLettersCount >= len(self.current_word)-1:
				self.score = 100
				self.state = False

			return letterIndexes
		
		else:
			self.score -= 1
			if self.score == 0:
				self.state = False
			return []

	def getCurrentWord(self):
		return self.current_word

	def getScore(self):
		return self.score

	def getState(self):
		return self.state





