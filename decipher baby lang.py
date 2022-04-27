##Warren Clark 340 Kim
def decipher(babyExp):
    # replacing baby word with corresponding character.
    srcCode = ""
    srcCode = babyExp.replace("pee", "+")
    srcCode = srcCode.replace("gah", "-")
    srcCode = srcCode.replace("milk", "*")
    srcCode = srcCode.replace("heh", "/")
    srcCode = srcCode.replace("mama", "(")
    srcCode = srcCode.replace("dada", ")")
    srcCode = srcCode.replace("baaaaaaaaa", "9")
    srcCode = srcCode.replace("baaaaaaaa", "8")
    srcCode = srcCode.replace("baaaaaaa", "7")
    srcCode = srcCode.replace("baaaaaa", "6")
    srcCode = srcCode.replace("baaaaa", "5")
    srcCode = srcCode.replace("baaaa", "4")
    srcCode = srcCode.replace("baaa", "3")
    srcCode = srcCode.replace("baa", "2")
    srcCode = srcCode.replace("ba", "1")
    srcCode = srcCode.replace("b", "0")
    srcCode = srcCode.replace(" ", "")
    return srcCode
