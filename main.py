from quiz_brain import QuizBrain
from ui import QuizInterface
from questiondb import QuestionBank


question_bank = QuestionBank()
quiz = QuizBrain(question_bank.questions)
quiz_ui = QuizInterface(quiz)


# TODO:
#  1) Create new class QuestionBank in questiondb.py, constructing the question bank, based on the
#     question bank constructor above (move it from main.py), so that the data.py file is no more necessary,
#     and the unnecessary code is moved away from the main.py module to questiondb.py - DONE!
#  2) Move the methods for checking and getting the answers to the QuizBrain - DONE! Only display methods
#     left in the UI module!
#  3) Make the QuizBrain launch the UI (?) - NOT EASY TO DO, THOUGH - "circular import" ERROR
