import re

with open('./output2.txt', encoding="utf8") as f:
    result = []
    for line in f.readlines():
        lineFormatted = ','.join(["'" + element + "'" for element in line.split('\t')])
        print(lineFormatted)
        result.append("(" + lineFormatted + "),")
    result = '\n'.join(result)
    with open('./result.txt', "w", encoding="utf8") as f:
        f.write(result)