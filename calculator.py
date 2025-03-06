def check_error(arr):
    logicalcount = 0
    operatorcount = 0
    numbers_count = 0
    for l in range(0, len(arr)):
        if arr[l] == "==" or arr[l] == ">=" or arr[l] == "<=" or arr[l] == "<" or arr[l] == ">":
            logicalcount += 1
        # Space Error
        if arr[l].isnumeric():
            numbers_count += 1
        if arr[l].isnumeric() and l < len(arr) - 1:
            if arr[l + 1].isnumeric():
                return "Error"
        if l == len(arr) - 1:
            if arr[l] == "**" or arr[l] == "//" or arr[l] == ">" or arr[l] == "<" or arr[l] == ">=" or arr[l] == "<=" or \
                    arr[l] == "*" or arr[l] == "-" or arr[l] == "+" or arr[l] == "/" or arr[l] == "%" or arr[l] == "==":
                return "Error"
        if arr[l] == "**" or arr[l] == "//" or arr[l] == "*" or arr[l] == "-" or arr[l] == "+" or arr[l] == "/" or arr[
            l] == "%" or arr[l] == ">" or arr[l] == "<" or arr[l] == ">=" or arr[l] == "<=" or arr[l] == "==":
            operatorcount += 1
    if logicalcount > 1:
        return "Error"
    if operatorcount >= numbers_count:
        return "Error"


def solve(stack):
    # because no overflow occurred and python hasn't given up. Python will extend the precision until either the
    # calculation succeeds or the machine runs out of memory.
    x = len(stack) - 1
    # Exponential Superiority Right to left
    try:
        while x >= 0:
            if stack[x] == "**":
                # pop the operator
                stack.pop(x)
                right = stack.pop(x)
                left = stack.pop(x - 1)
                outcome = int(left) ** int(right)
                stack.insert(x - 1, str(outcome))
                x = len(stack) - 1
            x = x - 1
        # Multiplication, Division, Remainder , Integer division Left to Right
        x = 0
        while x < len(stack):
            try:
                if stack[x] == "*":
                    stack.pop(x)
                    right = stack.pop(x)
                    left = stack.pop(x - 1)
                    outcome = int(left) * int(right)
                    stack.insert(x - 1, str(outcome))
                    x = 0
                elif stack[x] == "/":
                    stack.pop(x)
                    right = stack.pop(x)
                    left = stack.pop(x - 1)
                    outcome = int(left) / int(right)
                    stack.insert(x - 1, str(outcome))
                    x = 0
                elif stack[x] == "//":
                    stack.pop(x)
                    right = stack.pop(x)
                    left = stack.pop(x - 1)
                    outcome = int(left) // int(right)
                    stack.insert(x - 1, str(outcome))
                    x = 0
                elif stack[x] == "%":
                    stack.pop(x)
                    right = stack.pop(x)
                    left = stack.pop(x - 1)
                    outcome = float(left) % float(right)
                    stack.insert(x - 1, str(outcome))
                    x = 0
            except ZeroDivisionError:
                return "Error"
            x += 1
        x = 0
        # Addition, Subtraction
        while x < len(stack):
            if stack[x] == "+":
                stack.pop(x)
                right = stack.pop(x)
                left = stack.pop(x - 1)
                outcome = float(left) + float(right)
                stack.insert(x - 1, str(outcome))
                x = 0
            elif stack[x] == "-":
                stack.pop(x)
                right = stack.pop(x)
                left = stack.pop(x - 1)
                outcome = float(left) - float(right)
                stack.insert(x - 1, str(outcome))
                x = 0
            x += 1
        # Boolean Operators Eqn solver
        x = 0
        while x < len(stack):
            if stack[x] == ">":
                stack.pop(x)
                right = stack.pop(x)
                left = stack.pop(x - 1)
                outcome = float(left) > float(right)
                stack.insert(x - 1, str(outcome))
                x = 0
            elif stack[x] == "<":
                stack.pop(x)
                right = stack.pop(x)
                left = stack.pop(x - 1)
                outcome = float(left) < float(right)
                stack.insert(x - 1, str(outcome))
                x = 0
            elif stack[x] == "<=":
                stack.pop(x)
                right = stack.pop(x)
                left = stack.pop(x - 1)
                outcome = float(left) <= float(right)
                stack.insert(x - 1, str(outcome))
                x = 0
            elif stack[x] == ">=":
                stack.pop(x)
                right = stack.pop(x)
                left = stack.pop(x - 1)
                outcome = float(left) >= float(right)
                stack.insert(x - 1, str(outcome))
                x = 0
            elif stack[x] == "==":
                stack.pop(x)
                right = stack.pop(x)
                left = stack.pop(x - 1)
                outcome = float(left) == float(right)
                stack.insert(x - 1, str(outcome))
                x = 0
            elif stack[x] == "!=":
                stack.pop(x)
                right = stack.pop(x)
                left = stack.pop(x - 1)
                outcome = float(left) == float(right)
                stack.insert(x - 1, str(outcome))
                x = 0
            x += 1
    except OverflowError:
        return "Error"
    except FloatingPointError:
        return "Error"
    except ArithmeticError:
        return "Error"
    outcome = stack.pop()
    return outcome


# Check for empty spaces between numbers
def empty_spaces(s):
    s = s.strip()
    arr = s.split(" ")
    for x in range(0, len(arr)):
        if x < len(arr) - 1:
            if arr[x].isnumeric() and arr[x + 1].isnumeric():
                return True


if __name__ == '__main__':
    # Read the files and ready them
    FileFound = False
    try:
        file1 = open('input.txt', 'r')
        FileFound = True
    except FileNotFoundError:
        print("File was not Found!")
    if FileFound:
        file2 = open('2021510018_EnesCan_Bilgic.txt', 'w+')
        Lines = file1.readlines()
        count = 0
        for line in Lines:
            count += 1
            # Remove White space
            if line == "\n":
                file2.write("\n")
            else:
                stack = []
                ERRORFlAG = False
                EmptySpace = empty_spaces(line)
                line = line.strip()
                line = line.replace(" ", "")
                i = 0

                try:
                    # Iterate over each character in the line
                    while i < len(line):
                        # Check if character is a number
                        if line[i].isnumeric():
                            # Check if the character after the number is a number to combine them to make one big number
                            if i > 0:
                                previous = stack.pop()
                                if previous.isnumeric():
                                    new_string_number = str(previous) + str(line[i])
                                    stack.append(str(new_string_number))
                                else:
                                    stack.append(previous)
                                    stack.append(str(line[i]))
                            else:
                                stack.append(str(line[i]))
                        # Check if character is Operator (Sub,Mult,Div,Add)
                        elif line[i] == "+" or line[i] == "-" or line[i] == "/" or line[i] == "*" or line[i] == "%":
                            stack.append(str(line[i]))
                            if line[i + 1] == "*":
                                stack.pop()
                                stack.append("**")
                                i += 1
                            elif line[i + 1] == "/":
                                stack.pop()
                                stack.append("//")
                                i += 1
                            elif not line[i + 1].isnumeric():
                                ERRORFlAG = True
                                break
                        # Check if character is logical operator
                        elif line[i] == ">" or line[i] == "<" or line[i] == "=":
                            stack.append(line[i])
                            if line[i + 1] == "=":
                                stack.pop()
                                newop = str(line[i]) + str(line[i + 1])
                                stack.append(newop)
                                i += 1
                            elif line[i + 1] != "=" and line[i + 1].isnumeric() == False:
                                ERRORFlAG = True
                                break
                        # Check if character is Logical operator not Equal
                        elif line[i] == "!":
                            stack.append(line[i])
                            if line[i + 1] == "=":
                                stack.pop()
                                newop = str(line[i]) + str(line[i + 1])
                                stack.append(newop)
                                i += 1
                            else:
                                ERRORFlAG = True
                                break
                        # Reject any character that is not character or in the list of operators
                        else:
                            ERRORFlAG = True
                            break
                        i += 1
                # Index Error That will be caught meaning that one of the Values is incorrect
                except IndexError:
                    ERRORFlAG = True
                # Check the error detectors for errors
                if ERRORFlAG or EmptySpace or (check_error(stack) == "Error"):
                    file2.write("ERROR\n")
                # Otherwise, solve the stack
                else:
                    result = solve(stack)
                    # Any mathematical Errors detected
                    if result == "Error":
                        file2.write("ERROR\n")
                    # Print the result of the mathematical or logical eqn
                    else:
                        file2.write(str(result).upper() + "\n")