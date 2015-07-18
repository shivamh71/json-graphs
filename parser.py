# Node class
class Node:
    def __init__(self,label,childArray,parent):
        self.childArray = childArray
        self.label = label
        self.parent = parent

    def toJSON(self):
        if(len(self.childArray)==0):
            return self.label
        else:
            result = {}
            result[self.label] = []
            for child in self.childArray:
                result[self.label] += [child.toJSON()]
            return result

# GLobal variables
stack = []
curIndex = 0

def countTabs(line):
    result = 0
    line = list(line)
    # print line
    for i in range(len(line)):
        if(line[i]==' '):
            result += 1
        else:
            return result/4

def pushInStack(node):
    global stack
    global curIndex
    if(len(stack)!=0):
        stack[-1].childArray += [node]
        curIndex += 1
    stack += [node]

def popFromStack():
    global stack
    global curIndex
    if(len(stack) > 0):
        stack = stack[:-1]
        curIndex -= 1

def makeTree(fileName):
    global stack
    global curIndex
    fin = open(fileName,"r")
    lines = fin.readlines()
    for line in lines:
        tabCount = countTabs(line)
        print tabCount, curIndex
        if(tabCount == curIndex):
            popFromStack()
            pushInStack(Node(line.strip(),[],None))
        elif(tabCount == curIndex + 1):
            pushInStack(Node(line.strip(),[],stack[-1]))
            curIndex = tabCount
        elif(tabCount < curIndex):
            while(curIndex >= tabCount):
                popFromStack()
            pushInStack(Node(line.strip(),[],stack[-1]))
            curIndex = tabCount
    return stack[0]

rootNode = makeTree("input.txt")
print rootNode.toJSON()
