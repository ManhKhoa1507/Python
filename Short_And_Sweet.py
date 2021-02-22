def CheckNumber(number):
    if(number % 2 == 0) :
        return 1 
    else : 
        return 3
def AreNumbersEven(number_list):
    boolean_list = []
    
    for i in number_list :
        if (CheckNumber(i) == 1 ) :
           boolean_list.append(True)
        else :
            boolean_list.append(False)

    return boolean_list

numbers = input()
interger_list = [int(i) for i in numbers.split(' ')]
even_odd_boolean_list = AreNumbersEven(interger_list)
print(even_odd_boolean_list)
