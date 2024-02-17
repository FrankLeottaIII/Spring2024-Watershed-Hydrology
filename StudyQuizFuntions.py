#Generic test scripts for study quizes
#Author: Frank R. Leotta III
#date: 2/16/2024

#Discription: This is a generic test script that can be used to create questions for a quiz.  It will be randomized
            # so that the answers are not always in the same order, and even the order of the questions will be randomized.


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

def answer_a_question(question, answer:str, answer_list:list)->bool:
    """Summery: This function will ask a question, and the correct answer will always be A out of a, b c, and d"""
    wrong_answer_list = deepcopy(answer_list)
    wrong_answer_list.remove(answer)
    random.shuffle(wrong_answer_list)
    print(f"what is {question}:")
    print(f"A) {answer}")
    print(f"B) {wrong_answer_list[0]}")
    print(f"C) {wrong_answer_list[1]}")
    print(f"D) {wrong_answer_list[2]}")
    walter = False
    while walter == False:
        user_answer = input("Enter the letter of your answer: ")
        if user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d":
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
        return False
    else:
        print("Error, marking it as Incorrect!")
        return False
    

def answer_b_question():
    """Summery: This function will ask a question, and the correct answer will always be B out of a, b c, and d"""
    