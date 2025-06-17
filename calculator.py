#Taking input of number
num1= float(input("Give a number: "))
num2= float(input("Give next number: "))

#selecting the operation

op = input("Give operation: ")
if op == "+":
      answer = num1 + num2
      print("The answer is: ", answer)
elif op == "-":
     answer = num1 - num2
     print("The answer is: ", answer)
elif op == "*":
         answer = num1 * num2
         print("The answer is: ", answer)
elif op == "/":
        answer = num1 / num2
        print("The answer is: ", answer)
elif op == "%":
         answer = num1 % num2
         print("The answer is: ", answer)
elif op == "**":
         answer = num1 ** num2
         print("The answer is: ", answer)
elif op == "//":
         answer = num1 // num2
         print("The answer is: ", answer)
else : print("Invalid operation")
