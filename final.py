#new comment!

#this is a second comment!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint, shuffle 

question_idx = 0
correct = ""
guess = ""
score = 0

questions = [
            ("What is the tallest mountain?", ["Everest", "Rainier", "Kilimanjaro", "Fuji"]),
            ("What is smallest animal?", ["bacteria", "dog", "flea", "ant"]),
            ("What is the fourth planet from the sun?", ["Mars", "Earth", "Uranus", "Neptune"])
        ]

shuffle(questions)

def set_question(q, answers):
    question.setText(q)
    r1.setText(answers[0])
    r2.setText(answers[1])
    r3.setText(answers[2])
    r4.setText(answers[3])
    button_group.setExclusive(False)
    r1.setChecked(False)
    r2.setChecked(False)
    r3.setChecked(False)
    r4.setChecked(False)
    button_group.setExclusive(True)


def next_question():
    global question_idx, correct, guess, score

    #get text of correct
    if r1.isChecked():
        guess = r1.text()
    if r2.isChecked():
        guess = r2.text()
    if r3.isChecked():
        guess = r3.text()
    if r4.isChecked():
        guess = r4.text()

    if guess == correct:
        score += 1

    if question_idx >= len(questions):
        button.hide() 
        result_box.show()
        question_box.hide()
        result.setText("Your final score: " + str(score))
    else:
        correct = questions[question_idx][1][0]
        answers = questions[question_idx][1]
        shuffle(answers)
        set_question(questions[question_idx][0], answers)
        question_idx += 1

app = QApplication([])

#question screen
question_box = QGroupBox("Question")
question = QLabel("This is the question")
button = QPushButton("Answer")
r1 = QRadioButton("Option 1")
r2 = QRadioButton("Option 2")
r3 = QRadioButton("Option 3")
r4 = QRadioButton("Option 4")
button_group = QButtonGroup()
button_group.addButton(r1)
button_group.addButton(r2)
button_group.addButton(r3)
button_group.addButton(r4)

l_answers = QHBoxLayout()
l_answers_top = QVBoxLayout()
l_answers_top.addWidget(r1)
l_answers_top.addWidget(r2)
l_answers_bot = QVBoxLayout()
l_answers_bot.addWidget(r3)
l_answers_bot.addWidget(r4)
l_answers.addLayout(l_answers_top)
l_answers.addLayout(l_answers_bot)

l_box = QVBoxLayout()
l_box.addWidget(question)
l_box.addLayout(l_answers)

question_box.setLayout(l_box)

#result box
result_box = QGroupBox("Results")
result = QLabel("Your score goes here")
l_result_box = QVBoxLayout()
l_result_box.addWidget(result)
result_box.setLayout(l_result_box)
result_box.hide()

#main page
l_main = QVBoxLayout()
l_main.addWidget(result_box)
l_main.addWidget(question_box)
l_main.addWidget(button)

win = QWidget()
win.setWindowTitle('Quiz!!!')
win.resize(400, 300)
win.setLayout(l_main)

button.clicked.connect(next_question)

correct = questions[question_idx][1][0]
answers = questions[question_idx][1]
shuffle(answers)
set_question(questions[question_idx][0], answers)
question_idx += 1


win.show()


app.exec()
