# # QUIZ APP
#TEKRAR ÇÖZ
#  '''DOCSTRING    : soruları göster, şıkları göster , input olarak yanıtı al,
# doğruluğunu kontrol et,  skor hesapla, hangi soruda olduğunu takip et         '''
# #if else blokları ne kadar azsa kod o kadar kaliteli

# #Question
# class Question:
#     def __init__(self,text,choices,answer):
#         self.text=text
#         self.choices=choices
#         self.answer=answer
#     def checkAnswers(self, answer):
#         return self.answer==answer  #--true döner
#         # if(choice==self.answer):
#         #     print("Answer is correct: +10")
#         # else:
#         #     print("Answer is not correct: -10")



# # print(q1.checkAnswers("python"))
# # print(q2.checkAnswers("C#"))


# #Quiz
# # class Quiz(Question):
# class Quiz:
#     def __init__(self,questions):
#         self.questions=questions
#         self.score=0
#         self.questionIndex=0
    
#     def getQuestion(self):
#         return self.questions[self.questionIndex]
#     def displayQuestion(self):
#         question=self.getQuestion()
#         print(f'Question {self.questionIndex+1}:{question.text}')
        
#         for q in question.choices:
#             print('-'+q)
#         answer=input('answer: ')
#         if(question.checkAnswer(answer)):
#             print("Answer is correct: +10")
#             self.score+=10
#         else:
#             print("Answer is not correct: -10")

#         self.questionIndex+=1

# q1=Question("Which one is an artificial intelligence program language?", ['C#',"python","C++","flutter"],"python")
# q2=Question("Which one is more closer to machine  language?", ['C#',"python","C++","flutter"],"C++")
# q3=Question("Which one is an android program language?", ['C#',"python","C++","flutter"],"flutter")
# questions=[q1,q2,q3]

# quiz=Quiz(questions)
# question=quiz.getQuestion()
# print(question.text,question.choices)
# quiz.displayQuestion()

# QUIZ APP
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.text}')
        
        for q in question.choices:
            print('- ' + q)
        
        answer = input('Answer: ')
        
        if question.checkAnswer(answer):
            print("Answer is correct: +10")
            self.score += 10
        else:
            print("Answer is not correct: -10")
        
        self.questionIndex += 1

q1 = Question("Which one is an artificial intelligence programming language?", ['C#', "python", "C++", "flutter"], "python")
q2 = Question("Which one is more closely related to machine language?", ['C#', "python", "C++", "flutter"], "C++")
q3 = Question("Which one is an android programming language?", ['C#', "python", "C++", "flutter"], "flutter")
questions = [q1, q2, q3]

quiz = Quiz(questions)

while quiz.questionIndex < len(questions):
    quiz.displayQuestion()

print(f"Quiz completed. Your score is: {quiz.score}")
