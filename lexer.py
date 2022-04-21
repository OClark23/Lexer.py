class token:
    def __init__(self, type, value):
        self,type = type
        self.value = value

def tokensize(srcCode):
    tokseq = []
    while srcCode !="":
        if char =="+":
            newToken = token("PLUS", char)
            tokseq.append(newToken)
            srcCode = srcCode[1:]
        elif char =="(":
            newToken = token("Left parenthesis", char)
            tokseq.append(newToken)
            srcCode = srcCode[1:]
        elif char ==")":
            newToken = token("Right parenthesis", char)
            tokseq.append(newToken)
            srcCode = srcCode[1:]
        elif char =="/":
            newToken = token("Divsion", char)
            tokseq.append(newToken)
            srcCode = srcCode[1:]
        elif char =="-":
            newToken = token("MINUS", char)
            tokseq.append(newToken)
            srcCode = srcCode[1:]
        elif char =="*":
            newToken = token("MULTIPLY", char)
            tokseq.append(newToken)
            srcCode = srcCode[1:]
        elif char == " ":
            srcCode = srcCode[1:]
            pass    
        elif char.isdigit():
            while char.isdigit():
                numbStr += char
                srcCode= srcCode[1:]
            if srcCode == "":
                char = srcCode
            else:
                char = srcCode[0]
        newToken = token("NUMBER", char)
        tokseq.append(newToken)
    srcCode = srcCode[1:]
    return tokseq