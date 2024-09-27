link = 'https://leetcode.com/problems/valid-parentheses/description/'

def isValid(s):
    stack = [] #stack to push brackets on
    dicts = {
        '(':')',
        '{':'}',
        '[':']'
    } #dictionary to initialize brackets

    for brackets in s:
        if brackets in dicts:
            stack.append(dicts)# push to stacks
        elif len(stack) ==0 or bracket!= dicts[stack.pop()]: #compare brackets from dict to stack if not equal return false
            return False
    return len(stack)==0   # len stack ==0 means all brackets match ==True     
