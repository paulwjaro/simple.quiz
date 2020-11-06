from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in range(0, len(question_data["results"])):
    question_bank.append(Question(question_data["results"][questions]["category"],
                                  question_data["results"][questions]["question"],
                                  question_data["results"][questions]["correct_answer"]))

quiz = QuizBrain(question_bank)

for questions in question_bank:
    quiz.next_question()

if quiz.score >= 8:
    print(f"Congratulations! You got {quiz.score} out of {len(question_bank)}")
elif quiz.score >= 4 & quiz.score < 8:
    print(f"Not too bad! You got {quiz.score} out of {len(question_bank)}")
else:
    print(f"You should really study more... You got {quiz.score} out of {len(question_bank)}")
