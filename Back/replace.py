import re

with open('./StatsPoke2.sql', encoding="utf8") as f:
    result = []
    for line in f.readlines():
        lineFormatted = ','.join(["'" + element + "'" for element in line.split('\t')])
        print(lineFormatted)
        result.append("(" + lineFormatted + "),")
    result = '\n'.join(result)
    with open('./result2.txt', "w", encoding="utf8") as f:
        f.write(result)