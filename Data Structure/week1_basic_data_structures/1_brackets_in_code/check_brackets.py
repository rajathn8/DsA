# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            pass

  
# Function to check parentheses 
def parenthesis_checker(myStr,open_list,close_list): 
    stack = []
    for b in enumerate(myStr):
        i = b[1] 
        if i in open_list: 
            # add the parenthesis to the stack
            stack.append(b) 
        elif i in close_list:
            # pop the parenthesis which matches with the position
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1][1])): 
                stack.pop() 
            else:
                # if that said parenthesis is not there inside the stack : ie its not balanced
                #print(myStr.index(i))
                return b[0]+1
    if len(stack) == 0: 
        return "Success"
    else: 
        return stack[0][0]+1


def main():
    
    opening_parent = ["[","{","("] 
    ending_parent = ["]","}",")"] 

    text = input()
    mismatch = parenthesis_checker(text,open_list=opening_parent,close_list=ending_parent)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
