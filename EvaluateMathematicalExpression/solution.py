import re

def str2int(exp):
    if   exp == '0': return 0
    elif exp == '1': return 1
    elif exp == '2': return 2
    elif exp == '3': return 3
    elif exp == '4': return 4
    elif exp == '5': return 5
    elif exp == '6': return 6
    elif exp == '7': return 7
    elif exp == '8': return 8
    elif exp == '9': return 9
    else: return -1
    
def arithmetics(exp):
    total=0
    for p, el in enumerate(exp):
        if not(total):
            total=el
            continue
        if el == '+':
            total += exp[p+1]
        if el == '-':
            total -= exp[p+1]
        if el == '/':
            total /= exp[p+1]
        if el == '*':
            total *= exp[p+1]
    return total

def calc(expression):
    return splitBasic(expression.replace(' ', ''))
    # subExp=[]
    # p = expression.find('(')
    # while expression.find('(')+1:
    #     start=expression.find('(')+1
    #     end=expression.find(')', start)
    #     subExp.append(expression[start:end])
    #     expression=expression[:start-1] + expression[end+1:]
    # return subExp

def splitBasic(expression):
    splitExp=[]
    number=''
    for el in expression:
        if re.findall("[0-9]", el):
            number = number+el
        else:
            if number: 
                splitExp.append(number)
                number=''
            splitExp.append(el)
    splitExp.append(number)
    return eval(splitExp)

def eval(expression):
    for pos, element in enumerate(expression):
        number=0
        size = len(element)
        for p, el in enumerate(element):
            n=str2int(el)
            if n != -1:
                number+=n*10**abs(p-size+1)
            else:
                number=el
        expression[pos]=number
    return arithmetics(expression)

print(calc("123 + 2 -30 /2"))