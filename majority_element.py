n = int(input("enter the number of elements: "))
input_string = input("enter the array: ")
let_arr = []
input_string = input_string.strip('[]')
elements = input_string.split(',')
for element in elements:
    let_arr.append(int(element.strip()))

dict_a = {}
for i in let_arr:
    if i in dict_a:
        dict_a[i] += 1
    else:
        dict_a[i] = 1

for key, value in dict_a.items():
    if value > n / 2:
        print(f"The majority element is: {key}")
        break
    else:
        print("No majority element found")