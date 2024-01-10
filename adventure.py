def checkString(string1, string2):
    split1 = string1.lower().split(' ') 
    split2 = string2.lower().split(' ')
    matched = 0
    for word in split1:
        for word2 in split2: 
            if word == word2:
                matched += 1
    return matched

name = input("What is your name?")
quests = [
    {
        "question": """As you enter the dimly lit cavern, and at its center lies a gleaming treasure chest, 
securely locked and shrouded in an air of anticipation. Will you shake the chest or venture deeper inside the cavern?""",
        "answers": [
        {
            "string": "shake the chest", 
            "response": "It sounds like something small, but you also hear some angry growling noises coming from within...",
            "next": 1
        },
        {
            "string": "venture deeper",
            "response": "You walk deeper inside the cavern and ignore the treasure chest.",
            "next": 2
        },
        ],
    }
]

index = 0
while True:
    quest = quests[index]
    answer1 = input(quest["question"])

    option1 = checkString(answer1, quest["answers"][0]["string"])
    option2 = checkString(answer1, quest["answers"][1]["string"])


    if option1 > option2 and option1 >= 1:
        print(quest["answers"][0]["response"])
        index = quest["answers"][0]["next"]
    elif option2 > option1 and option2 >= 1:
        print(quest["answers"][1]["response"])
        index = quest["answers"][1]["next"]
    else:
        print("Please write your answer again")




