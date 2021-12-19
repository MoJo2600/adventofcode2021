f = open("day4/input.txt","r")

lines = f.readlines()

hits = [int(v) for v in lines[0].split(',')]
print(hits)

fields = []
current_field = []

new_field = False
field_line = 0
for line in lines[1:]:
    line = line.strip()
    if line == '':
        if (field_line == 5):
            fields.append(current_field)
            field_line = 0
        current_field = []
    else:
        current_field.append([int(v) for v in line.split()])
        field_line = field_line + 1

# a) and b)

result_table = [[[0,0,0,0,0], [0,0,0,0,0], [], False, 0] for i in range(len(fields))]
winner_field = None
last_winner_field = None
for hit in hits:
    for field in range(len(fields)):
        for row in range(5):
            for column in range(5):
                if not result_table[field][3]: # field is still in the game
                    if fields[field][row][column] == hit:
                        result_table[field][0][row] += 1
                        result_table[field][1][column] += 1

                        if result_table[field][0][row] == 5 or result_table[field][1][column] == 5:
                            result_table[field][3] = True # won!
                            result_table[field][4] = hit  # win number
                            if winner_field is None:
                                winner_field = field
                        result_table[field][2].append(hit)
                        last_winner_field = field

def get_field_sum(field, result_field):
    winning_sum = 0
    for row in range(5):
        for column in range(5):
            if not field[row][column] in result_field[2]:
                winning_sum += field[row][column]
                print(field[row][column])
    return winning_sum * result_field[4]

sum1 = get_field_sum(fields[winner_field], result_table[winner_field])
print(f'first winner: {winner_field}, win number {result_table[winner_field][4]}, sum = {sum1}')
sum2 = get_field_sum(fields[last_winner_field], result_table[last_winner_field])
print(f'last winner: {last_winner_field}, win number {result_table[last_winner_field][4]}, sum = {sum2}')


