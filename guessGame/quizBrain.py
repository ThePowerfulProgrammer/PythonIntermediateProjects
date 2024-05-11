'''Model the game'''

class QuizBrain(object):
    
    def __init__(self, questions_list:list) -> None:
        self.question_number = 0 # Always start at qquestion 0
        self.questions_list = questions_list # A list of Question objects in a list
        
    def next_question(self):
        if (self.question_number < len(self.questions_list)):
            self.question_number += 1
        else:
            return self.question_number