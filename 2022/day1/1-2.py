from path import Path

input_path = Path(__file__) / '..' / 'input-1.txt'
input_path = input_path.abspath()

elf_num = 1
big_elf = 0
total_calories = -1
elf_calorie_totals = []
def check_elf_supply(item_list):
    return sum(item_list)

with open(input_path, 'r') as infile:
    current_elf_supply = []
    for line in infile:
        if line in ['\n', '\r\n']:
            current_total = check_elf_supply(current_elf_supply)
            elf_calorie_totals.append(current_total)
            current_elf_supply = []
        else:
            # print(f'Elf {elf_num} added {int(line)} calories')
            current_elf_supply.append(int(line))

elf_calorie_totals.sort()
print(f'Largest elf total = {elf_calorie_totals[-1]}')
top_3 = sum(elf_calorie_totals[-3:])
print(f'Total of top 3: {top_3}')
