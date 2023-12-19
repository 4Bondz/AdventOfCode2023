class ParsingEngine:

    def setParsingState(self, v):
        self.parsingState = v
        if v == "A" or v == "R":
            self.doneParsing = True

    def debug(self):
        pass


    def __init__(self):
        self.rules = {}
        self.parsingState = None
        self.doneParsing = False
        self.operatorMap = {"<": lambda x, y: x < y, ">": lambda x, y: x > y}

    def addRule(self, ruleString):
        ruleID, rest = ruleString.split("{")
        self.rules[ruleID] = []
        rest = rest.strip("}")
        tests = rest.split(",")

        for test in tests:
            if "<" in test or ">" in test:
                condition, effect = test.split(":")
                parameter = condition[0]
                operator = condition[1]
                value = int(condition[2:])
                self.rules[ruleID].append({"parameter": parameter,
                                           "operatorFunc": self.operatorMap[operator],
                                           "value": value,
                                           "effect": effect,
                                           "operator": operator})
            else:
                effect = test
                self.rules[ruleID].append({"parameter": 'x',
                                           "operatorFunc": lambda x, y: True,
                                           "value": 0,
                                           "effect": effect,
                                           "operator": "-"})

    def classify(self, objectString):
        objectString = objectString.strip("{").strip("}")
        objectParamList = objectString.split(",")
        objectParams = {}
        for paramString in objectParamList:
            parameter = paramString[0]
            value = paramString[2:]
            objectParams[parameter] = value

        currentRuleKey = 'in'
        print(objectString)
        while True:
            if currentRuleKey == "A" or currentRuleKey == "R":
                print(currentRuleKey)
                return currentRuleKey, sum(int(x) for x in objectParams.values())
            rules = self.rules[currentRuleKey]
            for rule in rules:
                valueUnderTest = int(objectParams[rule['parameter']])
                result = rule['operatorFunc'](valueUnderTest, rule['value'])
                if result:
                    #print(objectParams[rule['parameter']], rule['operator'], rule['value'], currentRuleKey, rule)
                    self.setParsingState(rule['effect'])
                    currentRuleKey = rule['effect']
                    break
                else:
                    #print("NOT", objectParams[rule['parameter']], rule['operator'], rule['value'], currentRuleKey, rule)
                    continue



def main():
    with open("./day19input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    splitI = 0
    for i, line in enumerate(lines):
        if line == "":
            splitI = i

    toParse = lines[0:splitI]
    toClassify = lines[splitI + 1:]

    engine = ParsingEngine()

    for rule in toParse:
        engine.addRule(rule)

    acceptedObjects = []
    total = 0
    for object in toClassify:
        objectClassification, xValue = engine.classify(object)
        if objectClassification == "A":
            acceptedObjects.append(object)
            total += int(xValue)

    print(acceptedObjects)
    print(total)

if __name__ == "__main__":
    main()

# 75039 too low
# 336710 too low
# 346230