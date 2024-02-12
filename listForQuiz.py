#
#from logging import lastResort


list1 = ["1","2","3"]
list2 = ["4", "5", "6"]
list3 = ["7", "8", "9"]
list4 = ["10","11", "12"]
print(list1)


a = "a"
b= "b"
c = "c"
d = "d"

dict1 = {"Question" : [[list1, list2], [list3, list4]]} #a dictionary with a key of questions(and answers), the values is a list of lists of lists

dict1 = {"Question" : [[a, b], [c, d]]} # a dictionary with a key of questions and answers, the values is a list of list

# dict1 = {"Question": [["a", "b"], ["c", "d"]]}
value_b = dict1["Question"][0][1]
print(f"The value of 'b' is: {value_b}")

#ok so based on that, I can make it a tuple
dict2 = {"Question": (("a", "b"), ("c", "d"))}
#value_a = dict2["Question":[0][0]] Wrong, not a list
value_a = dict2["Question"][0][0] #this is the correct way for this
print(f"the value of a in the touple dict is: {value_b}")

HydrographQandA = {
    "QuestionAndAnswers": (("precipitation start time", "when it starts"),("precipitation end time","when it ends"  ),("total precipitation", "total amount of precip between start time and end time"),("stream response begins", "starts at base flow"),("base flow", "base flow is the amount at which cubic feet a second before the storm increase happens. "), 
("peak flow", "peak flow is the highest point that the cfs is durring the storm"), ("stream response ends- strait line method", "to get this, draw a strait line from beginning of base flow to end where the graph meets this line"), ("Lag time", "lag time is the precip start - stream response begins"),("Rise time", "Time Stream response begins - Time peak flow occures") )
}

#just grab the second item in each inner list from a loop and put it in a seperate list for answer sheet

HydrographsQandA = {
    "QuestionAndAnswers":((b,a),),
    "Answers" : (a,b)

}






def question_type_1(question:str, answer:str,all_answers: list)->bool:
    """Summary:
    Asks a question in which the answer is always a

    Args:
        question:str 
        answer : str 
        all_answers : a list of all the answers copyied into a varible from a specific dictionary via copy.deepcopy

    Returns 
        True if answer correct, False if gotten wrong

    """
    list_of_wrong_answers = i for ... get code lastResor
    wrong_answer1 = random(list_of_wrong_answers)
    list_of_wrong_answers = i for
    wrong_answer2 = random(list_of_wrong_answers)
    list_of_wrong_answers = i for
    wrong_answer3 = random(list_of_wrong_answers))
    print(question)
    print(f'a.) {a})
    print(f"b.) {random())
