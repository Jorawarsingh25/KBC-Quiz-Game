questions=[
    ["what is rose coulur?", "red","yellow","green","pink",1],
    ["what is bhagwat geeta main roll?", "ram","arjun","krishna","bramha",3 ],
    ["where is new ram murti establish city?","delhi","mathura","amritsar","ayodhya",4],
    ["Name of prime minister in India","mohan bhagwat","amit shah","narendra modi","none",3],
    ["who is the father of the nation of india?","mahatma ghandi","Godse","rajeev gandhi","pranav mukhrji",1],
    ["who was the first prime minister of india","s.vallabh bhai patel","pandit jawahar lal neharu","subhash chandra boss","ravindra nath tagour",2],
    ["who is Sachin Tandulkar?","footballer","kabaddi plyaer","cricketer","none",3],
    [ "what is capital city of India?","jaipur","udaipur","new delhi","ghaziyabad",3],
    [ "which is the national sport in india?","cricket","football","kabaddi","hockey",4],
    ["who is the current home minister in india?","amit shah","anurag thakur","jp nadda","none",1],
    ["who is the chief of RBI governor?","shri shaktikanta das","rajeev manhotra","rahul kumar","none",1],
    ["who is the known as 'iron man' in india?","krishna","sardar vallavh bhai patel","narendra modi","none",2],
    ["where is ram mandir located?","agra","jaipur","ajmer","ayodhya",4],
    ["which indian state has the smallest coastline?","up","mp","goa","rajasthan",3],
]
levels=[1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,]
money=0

for i in range(len(questions)):
    question = questions[i]

    print(f"\n\nQuestion for RS.{levels[i]}")
    print(f"{question[0]}?")
    print(f"a. {question[1]}                    b. {question[2]}")
    print(f"c. {question[3]}                    d. {question[4]}")

    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))

    if reply == 0:
        money = levels[i - 1]
        break
        
    if reply == question[-1]:
        print(f"Correct answer, you have won RS.{levels[i]}")
        
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
        else:
            money += levels[i]
            print(f"Your current total is  RS.{money}")
    else:
        print("Wrong Answer")

print(f"Your take-home money is {money}")