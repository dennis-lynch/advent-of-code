from path import Path

input_path = Path(__file__) / '..' / 'input-1.txt'
input_path = input_path.abspath()

elf_num = 1
big_elf = 0
total_calories = -1
def check_elf_supply(item_list):
    return sum(item_list)

with open(input_path, 'r') as infile:
    current_elf_supply = []
    for line in infile:
        if line in ['\n', '\r\n']:
            current_total = check_elf_supply(current_elf_supply)
            if current_total > total_calories:
                total_calories = current_total
                big_elf = elf_num
            current_elf_supply = []
            elf_num += 1
            # break
        else:
            # print(f'Elf {elf_num} added {int(line)} calories')
            current_elf_supply.append(int(line))


print(f'Largest elf total = {total_calories} by elf number {big_elf}')