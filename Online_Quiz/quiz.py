class Quiz:

    def __init__(self):

        self.filename = "quiz.txt"

        self.questions = {
              1: {
                "question": "What is 5 + 5?",
                "options": ["5", "10", "15", "20"],
                "answer": "B"
            },

            2: {
                "question": "What is the capital of India?",
                "options": ["Mumbai", "Delhi", "Pune", "Nashik"],
                "answer": "B"
            },

            3: {
                "question": "Which planet is called the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Venus"],
                "answer": "B"
            },

            4: {
                "question": "What is 20 - 5?",
                "options": ["10", "15", "20", "25"],
                "answer": "B"
            },

            5: {
                "question": "Which language are we learning?",
                "options": ["Java", "C++", "Python", "PHP"],
                "answer": "C"
            }
        }

#MENU

    def menu(self):

        while True:

            print("\n==========ONLINE QUIZ===============")

            print("1. Start Quiz")
            print("2. View Result")
            print("3. EXIT")

            choice = input("Enter Choice: ")

            if choice == "1":
                 self.start_quiz()

            elif choice == "2":
                self.view_result()

            elif choice == "3":

                print("Thank You!")

                break
            else:

                print("Invalid Choice")

#Start Quiz

    def start_quiz(self):
        score = 0
        letters = ["A","B","C","D"]

        print("=============Quiz Started=================")

        for question_id in self.questions:

            print("\nQuestion",question_id)

            print(self.questions[question_id]["question"])

            #show Options

            for i in range(4):
                print(letters[i],".", self.questions[question_id]["options"][i])

            #take Answer

            answer = input("Enter Answer (A/B/C/D):").upper()

            #Check Answer

            if answer == self.questions[question_id]["answer"]:

                print("Correct Answer")
                score +=1

            else:

                print("Wrong Answer!")

                print("Correct Answer:",self.questions[question_id]["answer"])


        #Result

        total = len(self.questions)

        percentage = (score / total ) * 100

        print("\n=========RESULT==============")

        print("Total questions:", total)
         
        print("Correct Answer   :", score)

        print("Wrong Answer :", total - score)

        print(f"Percentage :{percentage:.2f}%")

        if percentage >= 40:
            print("Result  : PASS")

        else:

            print("Result  : FAIL")

        self.save_result(score, percentage)


    #SAVE RESULT

    def save_result(self,score, percentage):

        file = open(self.filename,"a")

        file.write(
            f"Score:{score}/{len(self.questions)} |"
            f"Percentage: {percentage:.2f}%\n"
        )

        file.close()

        print("Result save successfully.")


    #VIEW RESULT

    def view_result(self):

        print("\n=============previous result================")

        file = open(self.filename,"r")

        for line in file:
            print(line.strip())

        file.close()


#Main Program


q1 = Quiz()
q1.menu()
