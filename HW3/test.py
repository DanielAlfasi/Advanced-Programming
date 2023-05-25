def reverse(word):
    rWord = word[::-1]
    return rWord


def is_palindrome(word):
    if word == reverse(word):
        return 1
    else:
        return 0


def find_largest_palindrome():
    a = 999
    b = 999
    max = 0
    while a > 99:
        while b > 99:
            product = a * b
            if is_palindrome(str(product)):
                if max < product:
                    max = product
            b = b - 1
        a = a - 1
    num1 = str(product)
    num2 = num1[::2]
    print(num1, ' , ', num2)


def validate_israeli_id(id_number):
    count = 0
    sum = 0
    temp = 0
    for d in id_number:
        if count % 2 == 0:
            temp = int(d) * 1
        else:
            temp = int(d) * 2
        if temp >= 10:
            temp = int(temp % 10) + int(temp / 10)
        sum += temp
        count = count + 1
    if sum % 10 == 0:
        print('valid')
    else:
        print('invalid')


def evaluate_formula(formula):
    stacko = []
    stackn = []
    sum = 0
    consecutive = 0
    checker = False
    operation = ['+', '-', '/', '*']
    for c in formula:
        if c in operation:
            stacko.append(c)
            consecutive = consecutive + 1
        elif c != ' ':
            stackn.append(int(c))
            consecutive = 0
        if consecutive == 2:
            checker = True

    while len(stacko) > 0:
        o = stacko.pop()
        n1 = stackn.pop()
        n2 = stackn.pop()
        n3 = 0
        if o == '+':
            sum = n1 + n2
        elif o == '-':
            sum = n1 - n2
        elif o == '/':
            sum = n2 / n1
        else:
            sum = n1 * n2
        stackn.append(sum)
        if len(stackn) - 1 == len(stacko) and checker:
            n3 = stackn.pop()
            checker = False

    if o == '+':
        sum = sum + n3
    elif o == '-':
        sum = sum - n3
    elif o == '/':
        sum = sum / n3
    else:
        sum = sum * n3
    print(sum)


def evaluate_formula(formula):
    stack1 = formula.split()
    stack2 = []
    operations = ['+', '-', '/', '*']
    while len(stack1) >= 1:
        temp = stack1.pop()
        if temp in operations:
            a = stack2.pop()
            b = stack2.pop()
            if temp == '+':
                stack1.append(float(a) + float(b))
            elif temp == '-':
                stack1.append(float(a) - float(b))
            elif temp == '/':
                stack1.append(float(a) / float(b))
            elif temp == '*':
                stack1.append(float(a) * float(b))
        else:
            stack2.append(temp)
    print(temp)


def evaluate_formulasahar(formula):
    list_formula = formula.split()
    numbers_list = []
    while len(list_formula) >= 1:
        if list_formula.pop().isnumeric():
            numbers_list.append(int(i))
        else:
            if i == "+":
                if len(numbers_list) >= 2:
                    a = numbers_list.pop()
                    b = numbers_list.pop()
                    numbers_list.append(a + b)
            if i == "-":
                if len(numbers_list) >= 2:
                    a = numbers_list.pop()
                    b = numbers_list.pop()
                    numbers_list.append(a - b)
            if i == "*":
                if len(numbers_list) >= 2:
                    a = numbers_list.pop()
                    b = numbers_list.pop()
                    numbers_list.append(a * b)
            if i == "/":
                if len(numbers_list) >= 2:
                    a = numbers_list.pop()
                    b = numbers_list.pop()
                    numbers_list.append(a / b)
    print(numbers_list[0])


def printer():
    formula = ' + * 5 - 9 3 + 5 / 10 2 '
    print(formula.split())
    evaluate_formulasahar(formula)


printer()
