import re
with open("raw_data.txt", "r") as data:
    lines = data.readlines()
    print(lines)
    new_list = []
    for line in lines:
        new_line = re.sub(r'[0-9]+', '', line)
        new_list.append(new_line)
with open("filtered_data.txt", "w") as filtered_data:
    for line in new_list:
        filtered_data.writelines(line)