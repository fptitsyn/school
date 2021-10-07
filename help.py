# I write in python because there is no java ide :(

array = input("Input multiple numbers and press enter: ").split()

for j in range(len(array)):
    array[j] = int(array[j])

for i in range(len(array)):
    if array[i] == 0:
        array.pop(i)
        array.append(0)

print(array)
