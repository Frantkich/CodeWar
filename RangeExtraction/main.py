def check(number_range):
    if len(number_range) == 1:
        return f",{number_range[0]}"
    elif len(number_range) == 2:
        return f",{number_range[0]},{number_range[1]}"
    else:
        return f",{number_range[0]}-{number_range[-1]}"

def main(args):
    number_m1 = args[0]
    solution = ""
    number_range = [number_m1]
    for number in args[1:]:
        if number == number_m1 + 1:
            number_range.append(number)
        else:
            solution += check(number_range)
            number_range = [number]
        number_m1 = number
    solution += check(number_range)
    return solution[1:]


data_formated = main([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
solution =           '-6,-3-1,3-5,7-11,14,15,17-20'
if data_formated == solution:
    print("YAY")
else:
    print(data_formated)
    print(solution)


# [-3,-2,-1,2,10,15,16,18,19,20]
# '-3--1,2,10,15,16,18-20'