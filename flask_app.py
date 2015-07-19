## Parser code

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

# GLobal variables and Imports
stack = []
curIndex = 0
spaceCount = 2
import json

def countTabs(line):
    result = 0
    line = list(line)
    for i in range(len(line)):
        if(line[i]==' '):
            result += 1
        else:
            return result/spaceCount + 1

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
    stack = []
    curIndex = 0
    pushInStack(Node("pseudoRootNode",[],None))
    fin = open(fileName,"r")
    fin.seek(0)
    lines = fin.readlines()
    fin.close();
    for line in lines:
        tabCount = countTabs(line)
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
    return json.dumps(stack[0].toJSON())

## Flask code
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")
@app.route("/d3")
def d3():
    return render_template("graph.html")
@app.route("/convert", methods=["POST"])
def convert():
    data = request.form['data']
    print data
    fout = open('data.txt', 'w')
    fout.write(data)
    fout.close()
    result = makeTree("data.txt")
    print result
    return result

app.run()
