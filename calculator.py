op=input("ENTER THE OPERATOR :")
a=float(input("ENTER THE 1ST DIGIT : "))
b=float(input("ENTER THE 2ND DIGIT : "))
if op in ("+","-","*","/","%","//","**"):
    match op:
        case "+":
            print("THE ADDITION OF",a ,"AND",b, "IS :",a+b)
        case "-":
            print("THE SUBTRACTION OF",a ,"AND",b, "IS :",a-b)
        case "*":
            print("THE MULTIPLICATION OF",a ,"AND",b ,"IS :",a*b)
        case "/":
            print("THE QUOTIENT IN DIVISION OF",a, "AND",b, "IS :",a/b)
        case "% ":
            print("THE REMINDER IN DIVISION OF",a, "AND",b ,"IS :",a%b)
        case "//":
            print("THE FLOOR DIVISION OF",a ,"AND",b, "IS :",a//b)
        case "**":
            print("THE EXPONENTIAL OF",a, "AND",b ,"IS :",a**b)
else:
    print("INVALID OPERATOR! PLEASE ENTER THE VALID OPERATOR.")