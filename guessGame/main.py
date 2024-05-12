from quizBrain import QuizBrain
from Question import Question,question_bank




QuizBrain = QuizBrain(questions_list=question_bank)

score = 0
while True:
    index = QuizBrain.question_number
    answer = input(f"Q.{index+1}: {QuizBrain.questions_list[index].text}. (True\False)?: ")
    if(QuizBrain.check_answer(answer)):
        score += 1
        QuizBrain.next_question()
        if (QuizBrain.is_game_over()):
            print("You WONNN!!!!")
            print(f"Final Score: {score}")
            break            
    else:
        print(f"You Lose!, the right answer was {QuizBrain.questions_list[index].answer}")
        print(f"Final Score: {score}")
        break


