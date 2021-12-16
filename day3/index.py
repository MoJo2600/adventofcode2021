from data import input

# a
pos = [0] * 12
for num in input:
    for i in range(0, 12):
        if num & (1 << 11-i):
            pos[i] = pos[i] +1

gamma_rate = 0b0
num_items = len(input)
for i in range(0, len(pos)-1):
    if pos[i] > num_items/2:
        gamma_rate |= (1 << len(pos)-1-i)

epsilon_rate = gamma_rate ^ (2 ** 12 -1)
print(f'{gamma_rate*epsilon_rate}')
print(f'gamma_rate:       {bin(gamma_rate)}')
print(f'epsilon_rate:     {bin(epsilon_rate)}')


# string verify
epsilon_rate_str = ''.join(['1' if pos[i] < num_items/2 else '0' for i in range(0, len(pos))]) 
gamma_rate_str = ''.join(['1' if pos[i] > num_items/2 else '0' for i in range(0, len(pos))]) 
print(f'gamma_rate_str:   {gamma_rate_str}')
print(f'epsilon_rate_str: {epsilon_rate_str}')

print(f'{int(gamma_rate_str, 2)*int(epsilon_rate_str, 2)}')

# print(f'{0010100011000
# 1101011100111')

#for exponent in range (11,0):
#    out = filter(lambda list_element: int(list_element, 2) < 2**(exponent+1) and int(list_element,2) >= 2**exponent, input)
#    print(list(out))




# out = filter(lambda val: val > 2**11, input)
# print(list(out))

# out = filter(lambda val: val < 2**11 and val >= 2**10, input)
# print(list(out))

# out = filter(lambda val: val < 2**10 and val >= 2**9, input)
# print(list(out))