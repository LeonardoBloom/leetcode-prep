def decodeString(s):
        
        stack = []          # stack
        curNum = 0          # tracks current digit
        curString = ''      # tracks current string

        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num* curString
            elif c.isdigit(): # gets digit
                curNum = curNum*10 + int(c) # if before []
            else:
                curString += c  # get the string

        return curString
