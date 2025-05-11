with open("./movedump", "r", encoding="utf8") as f:
    for i in f.readlines():
        i = i.replace("\t", ",")
        if len(i.split(","))>=6:
            splitted = i.split(",")
            splitted[0] = "'" + splitted[0] + "'"
            splitted[3] = "'" + splitted[3] + "'"
            splitted[5] = "'" + splitted[5] + "'"
            i = ','.join(splitted)
        i = i.replace("\n", "")
        i = 'INSERT INTO main."Move" (name, pp, priority, category, power, type, accuracy) VALUES (' + i + ');'
        print(i)