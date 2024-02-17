#Generic test scripts for study quizes
#Author: Frank R. Leotta III
#date: 2/16/2024

#Discription: This is a generic test script that can be used to create questions for a quiz.  It will be randomized
            # so that the answers are not always in the same order, and even the order of the questions will be randomized.


#status: working on it periodically

#issues: Walter will not turn true, endless loop.


import random
import time
from copy import deepcopy



# touple = ((question, answer,), (question, answer,), (question, answer,), (question, answer,), (question, answer,)) ect...

#turn a touple into a list
def touple_to_list(touple): #untested
    """Summery: This function will turn a touple into a list"""
    new_list = []
    for i in range(len(touple)):
        new_list.append(touple[i])
    return new_list

#format:
#question 1 = newlist[0][0] with the first index being the location of the list in the list and the second index being the question
#answer 1 = newlist[0][1] with the first index being the location of the list in the list and the second index being the answer


#steps:
# add question , answer to list with hashtag # note stating the number in the list
#assighn varible to question, numbering as such
#assign varible to answer, numbering as such
#now you have all the questions and answers in a list, and you can use the varibles to call them
#you can now use the ask question funtions

questions_and_answers_example = (("What is 1+1?", "2"), ("What is 2+2?", "4"), ("What is 3+3?", "6"), ("What is 4+4?", "8"))
answer_list_example = ["2", "4", "6", "8"]

question_1_example = questions_and_answers_example[0][0]
answer_1_example = questions_and_answers_example[0][1]



def answer_a_question(question, answer:str, answer_list:list)->bool:
    """Summery: This function will ask a question, and the correct answer will always be A out of a, b c, and d"""
    wrong_answer_list = deepcopy(answer_list)
    wrong_answer_list.remove(answer)#removes the correct answer from the list
    random.shuffle(wrong_answer_list)
    print(f"what is {question}:")
    print(f"A) {answer}")
    print(f"B) {wrong_answer_list[0]}")
    print(f"C) {wrong_answer_list[1]}")
    print(f"D) {wrong_answer_list[2]}")
    walter = False
    while walter == False:
        user_answer = input("Enter the letter of your answer: ")
        if user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d" and user_answer != "A" and user_answer != "B" and user_answer != "C" and user_answer != "D":
            print("Invalid answer")
            walter = False
        elif user_answer == "a" or user_answer == "b" or user_answer == "c" or user_answer == "d":
            walter = True
        elif user_answer == "A" or user_answer == "B" or user_answer == "C" or user_answer == "D":
            walter = True
        else:
            walter = False
    if user_answer.lower() == "a":
        print("Correct!")
        return True
    elif user_answer.lower() == "b" or user_answer.lower() == "c" or user_answer.lower() == "d":
        print("Incorrect!")
        print("The correct answer was A.)", answer)
        return False
    else:
        print("Error, marking it as Incorrect!")
        print("The correct answer was A.)", answer)
        return False
    

def answer_b_question(question, answer:str, answer_list:list)->bool:
    """Summery: This function will ask a question, and the correct answer will always be B out of a, b c, and d"""
    wrong_answer_list = deepcopy(answer_list)
    wrong_answer_list.remove(answer)#removes the correct answer from the list
    random.shuffle(wrong_answer_list)
    print(f"what is {question}:")
    print(f"A) {wrong_answer_list[0]}")
    print(f"B) {answer}")
    print(f"C) {wrong_answer_list[1]}")
    print(f"D) {wrong_answer_list[2]}")
    walter = False
    while walter == False:
        user_answer = input("Enter the letter of your answer: ")
        if user_answer != "a" or user_answer != "b" or user_answer != "c" or user_answer != "d" or user_answer != "A" or user_answer != "B" or user_answer != "C" or user_answer != "D":
            print("Invalid answer")
            walter = False
        elif user_answer == "a" or user_answer == "b" or user_answer == "c" or user_answer == "d":
            walter = True
        elif user_answer == "A" or user_answer == "B" or user_answer == "C" or user_answer == "D":
            walter = True
        else:
            walter = False
    if user_answer.lower() == "b":
        print("Correct!")
        return True
    elif user_answer.lower() == "a" or user_answer.lower() == "c" or user_answer.lower() == "d":
        print("Incorrect!")
        print("The correct answer was B.)", answer)
        return False
    else:
        print("Error, marking it as Incorrect!")
        print("The correct answer was B.)", answer)
        return False
    

def answer_c_question(question, answer:str, answer_list:list)->bool:
    """Summery: This function will ask a question, and the correct answer will always be C out of a, b c, and d"""
    wrong_answer_list = deepcopy(answer_list)
    wrong_answer_list.remove(answer)
    random.shuffle(wrong_answer_list)
    print(f"what is {question}:")
    print(f"A) {wrong_answer_list[0]}")
    print(f"B) {wrong_answer_list[1]}")
    print(f"C) {answer}")
    print(f"D) {wrong_answer_list[2]}")
    walter = False
    while walter == False:
        user_answer = input("Enter the letter of your answer: ")
        if user_answer != "a" or user_answer != "b" or user_answer != "c" or user_answer != "d" or user_answer != "A" or user_answer != "B" or user_answer != "C" or user_answer != "D":
            print("Invalid answer")
            walter = False
        elif user_answer == "a" or user_answer == "b" or user_answer == "c" or user_answer == "d":
            walter = True
        elif user_answer == "A" or user_answer == "B" or user_answer == "C" or user_answer == "D":
            walter = True
        else:
            walter = False
    if user_answer.lower() == "c":
        print("Correct!")
        return True
    elif user_answer.lower() == "a" or user_answer.lower() == "b" or user_answer.lower() == "d":
        print("Incorrect!")
        print("The correct answer was C.)", answer)
        return False
    else:
        print("Error, marking it as Incorrect!")
        print("The correct answer was C.)", answer)
        return False
    

def answer_d_question(question, answer:str, answer_list:list)->bool:
    """Summery: This function will ask a question, and the correct answer will always be D out of a, b c, and d"""
    wrong_answer_list = deepcopy(answer_list)
    wrong_answer_list.remove(answer)
    random.shuffle(wrong_answer_list)
    print(f"what is {question}:")
    print(f"A) {wrong_answer_list[0]}")
    print(f"B) {wrong_answer_list[1]}")
    print(f"C) {wrong_answer_list[2]}")
    print(f"D) {answer}")
    walter = False
    while walter == False:
        user_answer = input("Enter the letter of your answer: ")
        if user_answer != "a" or user_answer != "b" or user_answer != "c" or user_answer != "d" or user_answer != "A" or user_answer != "B" or user_answer != "C" or user_answer != "D":
            print("Invalid answer")
            walter = False
        elif user_answer == "a" or user_answer == "b" or user_answer == "c" or user_answer == "d":
            walter = True
        elif user_answer == "A" or user_answer == "B" or user_answer == "C" or user_answer == "D":
            walter = True
        else:
            walter = False
    if user_answer.lower() == "d":
        print("Correct!")
        return True
    elif user_answer.lower() == "a" or user_answer.lower() == "b" or user_answer.lower() == "c":
        print("Incorrect!")
        print("The correct answer was D.)", answer)
        return False
    else:
        print("Error, marking it as Incorrect!")
        print("The correct answer was D.)", answer)
        return False
    
    
    #you need to have a score counter, and a question counter

def randomize_questions_and_answers(question, answer:str, answer_list:list)->bool: #untested, especially with the random number and bool return
    """Summery: This function will randomize the questions functions.  This will be used to ranomize what the user picks for the correct answer using all 4 functions in a randomized way.  This will only work on questions that have 4 choices
     
    Args:
        question (str): The question that will be asked
        answer (str): The correct answer
        answer_list (list): A list of all the possible answers

    Returns:
        bool: True if the user got the question right, False if the user got the question wrong
    
    """
    random_number = random.randint(1, 4)
    if random_number == 1:
        return answer_a_question(question, answer, answer_list)
    elif random_number == 2:
        return answer_b_question(question, answer, answer_list)
    elif random_number == 3:
        return answer_c_question(question, answer, answer_list)
    elif random_number == 4:
        return answer_d_question(question, answer, answer_list)
    else:
        print("Error, the random number was not between 1 and 4")
        raise ValueError("Error, the random number was not between 1 and 4")
    
    #######testing
# q1 = randomize_questions_and_answers(question_1_example, answer_1_example, answer_list_example)
# print(q1)
    
q2 = answer_a_question(question_1_example, answer_1_example, answer_list_example)
print(q2)



#remember:

       # if user_answer != "a" or user_answer != "b" or user_answer != "c" or user_answer != "d" or user_answer != "A" or user_answer != "B" or user_answer != "C" or user_answer != "D": This will not work, it will always be true, logical error
        #it should be and, not or.