from data import input;

increased = 0
for i in range(1, len(input)):
    if input[i] > input[i-1]:
        increased = increased + 1

print(f'a) increased: {increased}')

increased = 0
last_sum = -1
for i in range(0, len(input)): 
    batch = sum(input[i:i+3])
    if batch > last_sum:
        if last_sum != -1:
            increased = increased +1
    last_sum = batch

print(f'b) increased: {increased}')
