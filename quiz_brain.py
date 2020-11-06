class QuizBrain:

    def __init__(self, qlist):
        self.question_number = 0
        self. question_list = qlist
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}. " + current_question.question + "(True/False): ").capitalize()
        if answer == current_question.answer:
            print("You are correct!")
            self.score += 1
        else:
            print("You are incorrect.")
        print("\n")
