def get_day(N, K):
    i = (K + int(N))%7
    return i

N = input("Enter anynumber between 0 and 50: ")
S = input("Choose a day from the list - Mon,Tue,Wed,Thur,Fri,Sat,Sun: ")
days_list = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
K = days_list.index(S)

day_num = get_day(N, K)
print(N+" days after " + S + " is: "+ days_list[day_num])
