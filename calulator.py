numA = float(input("Enter the first number: "))
numB = float (input("Enter the second number: "))
operation = input("Enter the operation(+,/,* ,-): ")
if operation == '+':
  result =numA + numB
  PRINT(f"{numA} + {numB} = {result}")
elif operation == '-':
  result =numA -numB
  print(f"{numA} - {numB} ={result}")
elif operation == '*':
  result = numA*numB
  print(f"{numA}*{numB} ={result}")
elif operation == '/':
  if numB !=0:
    result =numA/numB
    print(f"{numA}/{numB} ={result}")
  else:
    print("ERROR")
else:
  print("inavlid operarion")
  
      
