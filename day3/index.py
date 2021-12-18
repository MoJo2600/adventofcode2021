from data import input

# a
pos = [0] * 12
for num in input:
    for i in range(0, 12):
        if num & (1 << 11-i):
            pos[i] = pos[i] +1

print(','.join(str(x) for x in pos))

gamma_rate = 0b0
num_items = len(input)
for i in range(0, 11):
    if pos[i] > num_items/2:
        gamma_rate |= (1 << 11-i)

# inverse gamma_rate to get epsilon
epsilon_rate = gamma_rate ^ (2 ** 12 -1)
print(f'{gamma_rate*epsilon_rate}')
print(f'gamma_rate:       {bin(gamma_rate)}')
print(f'epsilon_rate:     {bin(epsilon_rate)}')

# b
oxygen_generator_rating = 0b0
co2_scrubber_rating = 0b0

out = input
mask = (1 << 11)
for i in range(12):
    ones = len(list(filter(lambda reading: reading & mask, out)))
    more_ones = ones >= (len(out)/2)
    if more_ones:
        out = list(
            filter(lambda reading: not reading & mask, out)
        )
    else:
        out = list(
            filter(lambda reading: not reading & mask == 0, out)
        )
    
    if len(out) == 1:
        print(f'found oxygen_generator_rating: {bin(out[0])} - {out[0]}')
        oxygen_generator_rating = out[0]
        break

    mask >>= 1

out = input
mask = (1 << 11)
for i in range(12):
    ones = len(list(filter(lambda reading: reading & mask, out)))
    more_ones = ones >= (len(out)/2)
    if more_ones:
        out = list(
            filter(lambda reading: not reading & mask == 0, out)
        )
    else:
        out = list(
            filter(lambda reading: not reading & mask, out)
        )
    
    if len(out) == 1:
        print(f'found co2_scrubber_rating: {bin(out[0])} - {out[0]}')
        co2_scrubber_rating = out[0]
        break

    mask >>= 1


print(f'oxygen_generator_rating: {oxygen_generator_rating}')
print(f'co2_scrubber_rating: {co2_scrubber_rating}')
print(f'Result: {oxygen_generator_rating*co2_scrubber_rating}')