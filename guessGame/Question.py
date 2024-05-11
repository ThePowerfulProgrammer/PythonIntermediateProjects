from data import question_data

'''Model a Question'''

class Question(object):
    
    def __init__(self, text:str, answer:bool) -> None:
        self.text = text
        self.answer = answer
    
# Create a list of Question Objects
question_bank = []
for question in question_data:
    new_question = Question(text=question['text'], answer=question['answer'])
    question_bank.append(new_question)

    
if __name__ == "__main__":
    
    question = Question("2+3=5", True) 
    


