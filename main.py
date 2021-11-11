
class KB:

    def __init__(self):
        self.premise = []
        self.conclusion = ""
        self.count = 0
inferred = {}
agenda = []
knowledgeBase = []

def userInput():
    'takes in the user input and saves it to the knowledge base and agenda'

    while True:

        print("Please input knowledge base:(type 'exit' if you want to stop)")
        userInputtedData = input()

        if userInputtedData == 'exit':
            print("stopped")
            return 0

        elif len(userInputtedData) == 1:
            inferred[userInputtedData] = False
            agenda.append(userInputtedData)
            printstring = "Agenda[" + str(len(agenda)-1) +"]:" + userInputtedData
            print(printstring)

        elif userInputtedData.find('^') == -1: #not found

            newKB = KB()
            newData = userInputtedData.split('=>')
            newKB.count = 1

            inferred[newData[0]] = False
            newKB.premise.append(newData[0])

            inferred[newData[1]] = False
            newKB.conclusion = newData[1]

            knowledgeBase.append(newKB)

            printstring = "KB[" + str(len(knowledgeBase)) + "].premise[0]:" +str(newData[0]) + ", KB[" \
                             "" + str(len(knowledgeBase)) +"].conclusion:" + str(newData[1]) + ", " \
                             "count: 1"
            print(printstring)

        else:

            newKB = KB()
            newData = userInputtedData.split('=>')

            inferred[newData[1]] = False
            newKB.conclusion = newData[1]
            premise = newData[0].split('^')

            newKB.count = len(premise)

            
            for i in range(len(premise)):
                inferred[premise[i]] = False
                newKB.premise.append(premise[i])

            knowledgeBase.append(newKB)

def forwardChain():
    'implimentation of the forward chaining algorithm'

    print("What is your query?")

    queryInput = input()

    while len(agenda) != 0:
        p = agenda.pop(0)

        if p == queryInput:
            return True

        if not inferred[p]:
            inferred[p] = True

        for i in range(len(knowledgeBase)):

            if knowledgeBase[i].premise.count(p) > 0:

                knowledgeBase[i].count -= 1

                if knowledgeBase[i].count == 0:
                    agenda.append(knowledgeBase[i].conclusion)

    return False



userInput()

print(forwardChain())