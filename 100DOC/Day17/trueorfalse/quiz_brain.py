class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0




    def next_question(self):
        new_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q{self.question_number}: {new_question.question} (True/False)')


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def check_answer(self,user_answer):
        actual_answer = self.question_list[self.question_number].answer
        if actual_answer == user_answer:
            self.score   += 1
        else:
            print('You got it wrong')
        print(f'The correct answer is {actual_answer}')
        print(f'Your current score is,{self.score}/{self.question_number}')


