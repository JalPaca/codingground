

linepos = 0
lineno = 0
bufsize = 0
lineBuf = '\0'
tokenString= '\0'

def getNextChar():
    global lineBuf, lineno, linepos , bufsize
    if(linepos >= bufsize):
        lineBuf = str(s.split('\n', 1)[lineno])
        lineno += 1
        bufsize = len(lineBuf)
    out = lineBuf[linepos]
    linepos += 1
    return out  
        
def getToken():
    global tokenString
    state = 1
    currentToken = -1
    while state == 1 or state == 2:
        c = getNextChar()
        if c.isalpha():
            currentToken = 1
            tokenString += c
            state = 2
        else:
            state = 3
    return currentToken
            
s = """x := 5;
ab := 10 + 2;
{comentario}"""

print(getToken())