#COMP 340 HW 5 WARREN
import lexer


srcCode = "((12+3*5)+5/4)"
tokSeq = lexer.tokenize(srcCode)


for i in tokSeq:
    print (i.type, i.value)