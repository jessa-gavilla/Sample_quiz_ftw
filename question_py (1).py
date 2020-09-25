# -*- coding: utf-8 -*-
"""Question.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HqEfS87qrywTZMWg35JtDDbi0n-45R9a
"""

print("Can you understand millennials?")

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
question_prompts = [
     "What does 'periodt' mean?\n(a) End of a sentence\n(b) A normal lifecycle that has been extended\n(c) A more extreme or intense version of 'period'",'\n'
     "What does 'snatched' mean?\n(a) Something that was taken away\n(b) Something you say when someone is wearing something fashionable\n(c) The person who is 'the one that got away - TOTGA'",'\n'
    "What does 'shade' mean?\n(a) A place to stay away from the sun\n(b) A creepy person you don't like\n(c) A situation where someone illustrated sneaky actions toward someone or something",'\n'
    "What does 'Sksksksk' mean?\n(a) A person you are gossiping about\n(b) A versatile filler expression of excitement\n(c) A thing you really wanted to buy",'\n'
    "What does 'yeet' mean?\n(a) A situation you want to avoid\n(b) Discarding things quickly\n(c) A more extreme or intense version of 'period'",'\n'
    "What does 'tea' mean?\n(a) Your new eye candy\n(b) Your favorite drink\n(c) The latest gossip",'\n'
    "What does 'lit' mean?\n(a) Something amazing, exciting, high-energy, or great\n(b) To light something up in a big way\n(c) To always overshadow people with your presence",'\n'
    "What does 'salty' mean?\n(a) Garnishing a dish with too much salt\n(b) To be annoyed, upset, or bitter, usually about something minor\n(c) To always be great at the things you do",'\n'
    "What does 'shookt' mean?\n(a) Angry, frustrated, irritated\n(b) Shocked, surprised, or scared\n(c) Happy, festive, celebratory",'\n'
    "What does 'slay' mean?\n(a) to do really well or succeed at something\n(b) To overkill the enemy in a game\n(c) To kill people with kindness",'\n'
]
name = input("Please enter your name: ").title()
questions = [
     Question(question_prompts[0], "c"),
     Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "a"),
]
def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     if (score == 10):
      print("\n{0}, you scored {1} out of {2}. Wow a true millennial!".format(name, score, len(questions)))
     elif (score == 9):
       print("\n{0}, you scored {1} out of {2}. Good job!".format(name, score, len(questions)))
     elif (score>=7):
      print("\n{0}, you scored {1} out of {2}. Just a little more practice".format(name, score, len(questions)))
     else:
       print("\n{0}, you scored {1} out of {2}. Try harder!".format(name, score, len(questions)))
run_quiz(questions)