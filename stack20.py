def valid_parentheses(instr,dic):
    lst = []    

    if (instr[0] == ")") or (instr[0] == "}") or (instr[0] == "]"):
        return False

    for i in instr:
        if i in dic.keys():
            lst.append(i)
        elif i in dic.values():
            if len(lst) == 0:
                return False
            elif len(lst) != 0:             
                if (lst[-1] , i) in list(dic.items()):
                    lst.pop()
                elif (lst[-1] , i) not in list(dic.items()):
                    return False
    # print(lst)
    if len(lst) == 0:
        return True
    else:
        return False



if __name__ == "__main__":
    dic = {"{":"}","[":"]","(":")"}
    input_str = str(input()) 
    print(valid_parentheses(input_str,dic))
