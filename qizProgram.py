quizDic = {
    "Qusestion1":{
        "qsn" : "What is capital of france?\n",
        "ans": "paris",
    },
    
    "Qusestion2":{
        "qsn" : "What is capital of Germany?\n",
        "ans": "Berlin",
    },
    
    "Qusestion3":{
        "qsn" : "What is capital of Italy?\n",
        "ans": "Rome",
    },
    
    "Qusestion4":{
        "qsn" : "What is capital of spain?\n",
        "ans": "Madrid",
    },
    "Qusestion4":{
        "qsn" : "What is capital of Protugal?\n",
        "ans": "Lisbon",
    },
    "Qusestion4":{
        "qsn" : "What is capital of Switzerland?\n",
        "ans": "Bern",
    },
    
    
    "Qusestion4":{
        "qsn" : "What is capital of Austria?\n",
        "ans": "Vienna",
    }
}
score =0

for key,value in quizDic.items():
    print(value['qsn'])
    ans = input("Answer?")
    
    if ans.lower() ==  value['ans'].lower():
        print('correct')
        score +=1
        print('Your score is : '+ str(score))
        print("")
    else:
        print("Wrong")
        print("The answer is :"+ value['ans'])
        print('Your score is : '+ str(score))
        print("")
        print("")
        
print("you got " + str(score) + " out of 7 question correctly")        
print("your percentage is " + str(int(score/7 * 100)) +'%')        
        