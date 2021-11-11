
class KB:

    def __init__(self):
        self.premise = [""]
        self.conclusion = ""
        self.count = 0
inferred = {}
agenda = [""]
knowledgeBase = []

def userInput():
    'takes in the user input and saves it to the knowledge base and agenda'

    while True:

        print("Please input knowledge base:(type 'exit' if you want to stop)")
        userInputtedData = input()

        if userInputtedData == 'exit':
            return 0

        elif len(userInputtedData) == 1:
            agenda.append(userInputtedData)

        elif userInputtedData.find('^') == -1: #not found

            newKB = KB()
            newData = userInputtedData.split('=>')
            newKB.count = 1
            newKB.premise.append(newData[0])
            newKB.conclusion = newData[1]

            knowledgeBase.append(newKB)

        else:

            newKB = KB()
            newData = userInputtedData.split('=>')

            newKB.conclusion = newData[1]
            premise = newData[0].split('^')

            newKB.count = len(premise)

            for i in range(len(premise)):
                newKB.premise.append(premise[i])

            knowledgeBase.append(newKB)


userInput()
print(knowledgeBase)