class Solution:
    def simplifyPath(self, path):
        if path[0] != "/":
            return "Invalid String"
        else:
            path_list = path.split("/")
            join = "/"
            stack = []
            print(path_list)
            stack.append(path_list[0])
            for i in range(0,len(path_list)):
                print(i)
                if path_list[i] == "." :
                #     # print(path_list)
                #     # del path_list[i]
                #     # stack.pop()
                    # print(stack)
                    print(stack)
                    continue
                elif path_list[i] == ".." and len(stack) !=0:
                    # print(path_list)
                    # del path_list[i]
                    # del path_list[i-1]
                    # stack.pop()
                    stack.pop()
                    print(stack)
                elif path_list[i] != "." and  path_list[i] != ".." and path_list[i] != "":
                    stack.append(path_list[i])

                if len(stack) ==0:
                    # return "/"
                    continue

        if len(stack)==0:
            return "/"
        elif "" not in stack:
            return f"/{join.join(stack)}"
        elif len(stack)==1 and "" in stack:
            return "/"
        else:
            return join.join(stack)



obj = Solution()

print(obj.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"))


# "/home/"
# "/../"
# "/home/../../.."
# "/home//foo/"
# "/a/../../b/../c//.//"
# "/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"