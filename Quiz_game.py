import requests
import random
def menu():
    print("""Choose the subject code
          1:Mathematics
          2:Computer
          3:General Knowledge""")
    k=int(input())
    if k==1:
        fetch_data(19)
    elif k==2:
        fetch_data(18)
    else:
        fetch_data(9)
def fetch_data(subject_code):
    url="https://opentdb.com/api.php?amount=10&category={}&type=multiple".format(subject_code)
    data=requests.get(url)
    extract_question(data.json())
def extract_question(data):
    questions=[]
    correct_answers=[]
    all_options=[]
    for i in data['results']:
        questions.append(i['question'])
        correct_answers.append(i['correct_answer'])
        single_option=[]
        single_option.append(i['correct_answer'])
        single_option.extend(i['incorrect_answers'])
        random.shuffle(single_option)
        all_options.append(single_option)
    start_test(questions,all_options,correct_answers)
def start_test(questions,all_options,correct_answers):
    user_ans=[]
    k=0
    for i in questions:
        print('*'*100)
        print(i)
        print('*'*100)
        for j in all_options[k]:
            print(j)
        k=k+1
        print('_'*50)
        print("Enter your answer")
        answer=input()
        user_ans.append(answer)
    analyse_result(user_ans,correct_answers)
def analyse_result(user_ans,correct_answers):
    d={'correct':0,'incorrect':0}
    for i in range(len(user_ans)):
        if correct_answers[i]==user_ans[i]:
            d['correct']+=1
        else:
            d['incorrect']+=1
    score=d['correct']*5
    print("Correct Answers Given:",d['correct'])
    print("Incorrect Answers Given:",d['incorrect'])
    print("Your Score is",score)
    print("Correct Answers Are:")
    print("_"*50)
    for i in correct_answers:
        print(i)
menu()
