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

result_count = len(input)
test = 0b0
test2 = 0b0
skip = 0b111111111111
skip2 = 0b111111111111
out = input
out2 = input
for i in range (0,12):
    bit_value_at_position = 1 if gamma_rate & (1 << 12-i) else 0
    test |= (bit_value_at_position << 12-i)
    skip &= ~(1 << 12-i) | test
    out = list(filter(lambda reading: reading >= test and reading <= skip, out))
    if len(out) == 1:
        print(f'found oxygen_generator_rating: {bin(out[0])} - {out[0]}')
        oxygen_generator_rating = out[0]

    bit_value_at_position = 1 if epsilon_rate & (1 << 12-i) else 0




    test2 |= (bit_value_at_position << 12-i)
    skip2 &= ~(1 << 12-i) | test2
    out2 = list(filter(lambda reading: reading <= test2 and reading >= skip2, out2))
    if len(out2) == 1:
        print(f'found co2_scrubber_rating: {bin(out2[0])} - {out2[0]}')
        co2_scrubber_rating = out2[0]

print(f'oxygen_generator_rating: {oxygen_generator_rating}')
print(f'co2_scrubber_rating: {oxygen_generator_rating}')

print(f'Result: {oxygen_generator_rating*oxygen_generator_rating}')