class school:
    def __init__(self,ques):
        self.questions = ques

    def get_answer(self,ans):
        self.answer=ans

    def corrections(self):
        self.final = {self.questions[i]:self.answer[i] for i in range(len(self.questions))}


class teacher:
    def corrections(self,final,quest):
        mark=[]
        for i,j in final.items():
            print("question:\t"+i+"\nanswer"+j)
            mark.append(float(input()))
        self.final_mark = {quest[i]:mark[i] for i in range(len(quest))}



class student:
    def start_exam(self,ques):
        self.answer=[]
        for i in ques:
            print(i)
            self.answer.append(input())

Velammal = school(['What is Python','What is DS'])
Preethi = student()
Vaishu = teacher()

Preethi.start_exam(Velammal.questions)
Velammal.get_answer(Preethi.answer)
Velammal.corrections()
Velammal.final
Vaishu.corrections(Velammal.final,Velammal.questions)
Vaishu.final_mark