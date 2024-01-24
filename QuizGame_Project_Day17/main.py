from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# Creating question bank from data.py 
# each question as a separate Question() object
question_bank = []

for item in question_data:
    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_question():
    new_quiz.next_question()

new_quiz.print_final_score()

