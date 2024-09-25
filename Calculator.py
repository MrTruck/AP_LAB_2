num1 = input('First number:')
def main(): 
    num2 = input('Second number:')
    task = input("""To choose your operation, type:
    + to add
    - to subtract
    / to divide
    * to multiply""")
    if task.upper() == '+':
        output = float(num1)+float(num2)
        print(output) 
    elif task.upper() == '-' :
        output = float(num1) - float(num2)
        print(output)
    elif task.upper() == '/':
        output = float(num1) / float(num2) 
        print(output)
    elif task.upper() == '*':
        output = float(num1)*float(num2)
        print(output)
    else :
        print('Hooyada waas') 
    
    Repeat = input('Would you like to do another operation?(Y/N)').upper()
    if Repeat == 'Y':
        output= num1 
        main()
    else:
        print('bye')
main()
