def match_delimiters(input):

    s = []
    lefty = "({["
    righty = ")}]"

    for i in input:
        if i in lefty:
            s.append(i)
        elif i in righty:
            if (len(s)== 0):
                return False
            if (righty.index(i) != lefty.index(s.pop())):
                return False

        else:
            return Error("unknown symbol")

    return not(len(s))

print(match_delimiters("[{}{{(])}}]"))