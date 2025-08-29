history_file="history.txt"
def show_history():
    file=open(history_file,"r")
    lines=file.readlines()
    if len(lines)==0:
        print(" No History Found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
def clear_history():
    file=open(history_file,"w")
    file.close()
    print("History Cleared")
def save_to_history(eq,res):
    file=open(history_file,"a")
    file.write(eq + '=' + str(res) +"\n")
    file.close()
def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("Error")
        return
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])

    if op=="+":
        result=num1+num2
    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op=="/":
        if (num2==0):
            print("Error hhh")
            return
        else:
            result=num1/num2
    else:
        print("no more operators allowed")
        return
    if int(result)==result:
        result=int(result)
    print("Result:",result)
    save_to_history(user_input,result)
def main():
    print("Simple caluclator")
    while True:
        user_input=input("Enter +,-,*,/ ")
        if(user_input=="exit"):
            print("Thank you")
            break
        elif user_input=="history":
            show_history()
        elif user_input=="clear":
            clear_history()
        else:
            calculate(user_input)
main()
