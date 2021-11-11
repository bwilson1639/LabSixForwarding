
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

            printstring = "KB[" + str(len(knowledgeBase) -1) + "].premise[0]:" +str(newData[0]) + ", KB[" \
                             "" + str(len(knowledgeBase) -1) +"].conclusion:" + str(newData[1]) + ", " \
                             "count: 1"
            print(printstring)

        else:

            newKB = KB()
            newData = userInputtedData.split('=>')

            inferred[newData[1]] = False
            newKB.conclusion = newData[1]
            premise = newData[0].split('^')

            newKB.count = len(premise)

            printstring = ""
            for i in range(len(premise)):
                inferred[premise[i]] = False
                newKB.premise.append(premise[i])

                printstring = printstring + "KB[" + str(len(knowledgeBase) -1 ) + "].premise[" + str(i) + "]:" \
                                     + str(premise[i]) + ", "

            knowledgeBase.append(newKB)

            printstring = printstring + "KB[" + str(len(knowledgeBase) -1) + "].conclusion:" + str(newData[1]) + ", " \
                            "count: " + str(len(premise))
            print(printstring)

def forwardChain():
    'implimentation of the forward chaining algorithm'

    print("What is your query?")

    queryInput = input()

    print("=============")
    print("Forward chaining algorithm starts")
    print("=============")


    while len(agenda) != 0:
        p = agenda.pop(0)

        printstring = "***** Current agenda:" + str(p) +" *****"
        print(printstring)

        if p == queryInput:
            print("Goal Achieved")
            printstring = "The query " + str(p) + " is true based on the knowledge."
            print(printstring)
            print("---- The End -----")
            return True

        if not inferred[p]:
            inferred[p] = True

        for i in range(len(knowledgeBase)):


            if knowledgeBase[i].premise.count(p) > 0:

                if len(knowledgeBase[i].premise) > 1:
                    printstring = str(knowledgeBase[i].premise[0]) + "^" + str(knowledgeBase[i].premise[1]) + "=>" \
                                    "" + str(knowledgeBase[i].conclusion) + ", count:" +str(knowledgeBase[i].count)
                    print(printstring)
                    printstring = "Premise " + str(p) + " matched agenda"
                    print(printstring)
                else:
                    printstring = str(knowledgeBase[i].premise[0]) +  "=>" \
                                "" + str(knowledgeBase[i].conclusion) + ", count:" + str(knowledgeBase[i].count)
                    print(printstring)
                    printstring = "Premise " + str(p) + " matched agenda"
                    print(printstring)

                knowledgeBase[i].count -= 1

                if knowledgeBase[i].count == 0:

                    printstring = "Count is reduced to 0 ==> Agenda " + str(knowledgeBase[i].conclusion) + " is created"
                    agenda.append(knowledgeBase[i].conclusion)
                else:

                    printstring = "Count is reduced to " + str(knowledgeBase[i].count)
                    print(printstring)
    return False



userInput()

print(forwardChain())