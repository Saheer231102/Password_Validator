import regex as re

def printStrongNess(inn):
    n = len(inn)
    marks = 0

    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False

    for i in inn: 
        if (re.search("([a-z])", i)):
            hasLower = True
            marks +=1
        elif (re.search("([A-Z])", i)):
            hasUpper = True
            marks +=1
        elif(re.search("([0-9])", i)):
            hasDigit = True
            marks +=1
        elif (re.search("[@_!#$%^&*()<>?/|}{~:]", i)):
            specialChar = True
            marks +=2
        else:
            continue

    # Strength of the password 

    if(marks>=16 and n>=8 ):
        print("Strong")
    elif (marks<16 and marks>=7 and n<8 and n>=6):
        print("Moderate")
    else:
        print("Weak")

def main():
    inn = input("Enter your password: ")
    printStrongNess(inn)

main()
