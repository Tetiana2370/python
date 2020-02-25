# -*- coding: utf-8 -*-
# @Author: Tetiana Kravchuk
# @Date:   2020-02-17 20:15:24
# from game import * 

from game import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt, pyqtSlot

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)	
		

		self.game = game()
		self.game.start()
		self.canvasLabel = QLabel()

		canvas = QtGui.QPixmap(400, 300)
		self.canvasLabel.setPixmap(canvas)
		self.painter = QtGui.QPainter(self.canvasLabel.pixmap())
		pen = QtGui.QPen()
		pen.setWidth(3)
		self.painter.setPen(pen)
		self.painter.end()


		self.wordLabel = QPushButton()
		self.newGameButton = QPushButton("PLAY AGAIN")

		self.buttons = {}


	def setWindow(self):
		
		window = QWidget()

		layoutV = QVBoxLayout()
		layoutInnerV = QVBoxLayout()
		layoutH1 = QHBoxLayout()
		layoutH2 = QHBoxLayout()
		layoutH3 = QHBoxLayout()

		# devide window to saparate parts 
		self.newGameButton.hide()
		layoutInnerV.addWidget(self.newGameButton)
		layoutInnerV.addWidget(self.wordLabel)
		layoutV.addWidget(self.canvasLabel)

		# layoutV.addLayout(layout0)
		layoutV.addLayout(layoutInnerV)
		layoutV.addLayout(layoutH1)
		layoutV.addLayout(layoutH2)
		layoutV.addLayout(layoutH3)

		# add buttons with letters 
		self.initLetterButtons(0, 9, layoutH1)
		self.initLetterButtons(9, 18, layoutH2)
		self.initLetterButtons(18, 26, layoutH3)

		hidden_word = "_" * (len(self.game.getCurrentWord())- 1)
		#print("hidden_word is " + str(self.game.getCurrentWord()))
		self.wordLabel.setText(" ".join(hidden_word))
	
		
		self.newGameButton.clicked.connect(self.newGameButtonListener)
		self.clearPainter()
		self.setCentralWidget(window)
		self.setWindowTitle("Hangman game")
		window.setLayout(layoutV)


	def initLetterButtons(self, start, end, layout):

		for i in range(start, end):
			
			button = QPushButton(alphabet[i])
			button.setStyleSheet("""QPushButton {
				border-radius: 10px;
			}
			""")
			self.buttons[alphabet[i]] =  button
			button.clicked.connect(self.buttonListener)
			layout.addWidget(button)

	#drawing actions

	def drawWrongChoice(self):

		self.painter.begin(self.canvasLabel.pixmap())

		if(self.game.getScore() == 3):
			#head
			self.painter.drawEllipse(240, 70, 60, 60) 
		elif(self.game.getScore() == 2):
			#body
			self.painter.drawLine(270, 130, 270, 230)
		elif(self.game.getScore() == 1):
			#hands
			self.painter.drawLine(230, 150, 320, 150)
		elif(self.game.getScore() == 0): 
			#legs 
			self.painter.drawLine(270, 230, 230, 300)
			self.painter.drawLine(270, 230, 320, 300)
		
		self.canvasLabel.repaint()
		self.painter.end()
		
	def nextTurn(self, letter):

		prevScore = self.game.getScore()
		indexes = self.game.isCorrect(letter)

		if(self.game.getScore() == 100):
			self.wordLabel.setText("YOU WON")
			self.newGameButton.show()

		elif(self.game.getScore() == 0):
			self.drawWrongChoice()
			self.wordLabel.setText("GAME OVER")
			self.newGameButton.show()

		elif len(indexes) > 0:
			tmp = list(self.wordLabel.text().split(" "))
			for i in indexes:
				tmp[i] = letter
			
			self.wordLabel.setText(" ".join(tmp))

		elif(prevScore == self.game.getScore()):
			return

		elif prevScore > self.game.getScore():
			self.drawWrongChoice()


	def clearPainter(self):


		self.painter.begin(self.canvasLabel.pixmap())
		

		self.painter.fillRect(0, 0, 400, 300, Qt.white)

		self.painter.drawLine(10, 10, 300, 10)
		self.painter.drawLine(70, 10, 70, 300)
		self.painter.drawLine(270, 10, 270, 70)

		self.painter.end()

	
	#button listeners

	def buttonListener(self):

		if(self.game.getState() == False):
			return

		sender = self.sender()
		prevScore = self.game.getScore()

		chosenLetter = sender.text()
		
		self.nextTurn(chosenLetter)

		if(prevScore > self.game.getScore()):
			self.buttons[chosenLetter].setStyleSheet('QPushButton {color: red;}')
		else:
			self.buttons[chosenLetter].setStyleSheet('QPushButton {color: green;}')


	def newGameButtonListener(self):

		self.newGameButton.hide()
		self.game.start()

		hidden_word = "_" * (len(self.game.getCurrentWord()) - 1)
		self.wordLabel.setText(" ".join(hidden_word))
		self.clearPainter()

		for button in self.buttons.values():
			button.setStyleSheet(			"""
			QPushButton {
				border-radius: 10px;
			}
			"""
			)


app = QApplication(sys.argv)

window = MainWindow()
window.setWindow()
window.show()
app.exec_()