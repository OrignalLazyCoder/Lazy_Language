import sys
sys.path.insert(0, 'Interpreter')

import Interpreter
import sys

compileFile = False

def getFileText(name):
    nameArray = name.split('.')
    if nameArray[len(nameArray) - 1] != 'lca':
        print('INVALID FILE EXTENTION')
        return None
    f = open(name, 'r')
    text = f.read()
    return text

while True and not compileFile:
    if len(sys.argv) < 2:
        text = input('lazy > ').upper()
        if text.strip() == "quit()": break
        if text.strip() == "": continue
    else:
        compileFile = True
        text = getFileText(sys.argv[1])
    if text != None:
        result, error = Interpreter.run('<stdin>', text)

        if error:
            print(error.as_string())
