def StringReverse(str, starting, ending):
    res = ""
    for i in range(ending-1,starting-1, -1):
        res += str[i]
    return res


s = "University of Engineering and Technology Lahore"
print(StringReverse(s, 41, 47))