# Exception = events detected during  execution
#             that interrupt the flow of a program


try:
    num1 = int(input('Enter a number to divide: '))
    num2 = int(input('Enter a number to dicide by: '))
    result = num1 / num2
except ZeroDivisionError:
    print("You can't divided the number by ZERO")
except ValueError as e:
    print('You can only put NUMBERS')
    print(e)
except Exception:
    print('Something went wrong!!')
else:
    print(result)
finally:
    print('This is always execute')


