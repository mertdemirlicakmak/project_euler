"""Find the thirteen adjacent digits in the 1000-digit number that 
have the greatest product. What is the value of this product? """


# read file
with open('problem_8_data') as f:
    read_data = f.read()

input_lis = []
for item in read_data:
    if item != '\n':
        input_lis.append(int(item))

mult = 1
temp_mult = 1
counter = 0

for i in range(0, 987):
    temp_mult = 1
    chunk = input_lis[i: i + 13]
    if 0 in chunk:
        i += 12
        continue
    for num in chunk:
        temp_mult *= num
        counter += 1
    if temp_mult > mult:
        mult = temp_mult

print(mult, counter)
