N = input("Enter anynumber between 0 and 50: ")
S = input("Choose a day from the list - Mon,Tue,Wed,Thur,Fri,Sat,Sun: ")
days_list = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
K = days_list.index(S)
i = K + int(N)%7
print(N+" days after " + S + " is: "+ days_list[i])
