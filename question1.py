def get_product(N, S):
    num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    z = int(N)*num_dict[S]
    return z
    
N = input("Enter any number between 1 and 5: ")
S = input("Enter the number in words: (ex.1 as one): ")


product = get_product(N, S)
print("The product of " + N + " and " +S + " is: ", product)
