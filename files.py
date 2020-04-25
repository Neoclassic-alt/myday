import os
import ex_functions

names = [] # исходные имена
labels = [] # заголовки, подвергающиеся сокращению

if os.access("files", os.F_OK) == False:
    os.mkdir("files")
    with open("files/names.txt", "tw", encoding="ANSI") as f:
        f.close()
    with open("files/tags.txt", "tw", encoding="ANSI") as f:
        f.close()
    with open("files/dates.txt", "tw", encoding="ANSI") as f:
        f.close()

if os.access("files/names.txt", os.F_OK) == False:
    with open("files/names.txt", "tw", encoding="ANSI") as f:
        f.close()

if os.access("files/tags.txt", os.F_OK) == False:
    with open("files/tags.txt", "tw", encoding="ANSI") as f:
        f.close()

if os.access("files/dates.txt", os.F_OK) == False:
    with open("files/tags.txt", "tw", encoding="ANSI") as f:
        f.close()

f = open("files/names.txt", "r")

for line in f:
    names.append(line)

t = 0

listfiles = os.listdir("files")

if len(names) <= 34:
    len_names = 29
else:
    len_names = 26

while t < len(names):
    if(names[t][-1] == '\n'):
        names[t] = names[t][:len(names[t])-1]
    if len(names[t]) > len_names:
        labels.append(names[t][:len_names] + "…")
    else:
        labels.append(names[t])
    t = t + 1

f.close()
t = 0

while t < len(listfiles):
    if listfiles[t][:6] != "record":
        listfiles.pop(t)
    else:
        t = t + 1

listfiles.sort(key=ex_functions.sorting)

################# Функции разного рода #################

def nameread(num):
    f = open("files/" + listfiles[num], "r")
    text = f.read()
    f.close()
    return text

def readtags(num):
    f_tags = open("files/tags.txt", "r")
    c = f_tags.readlines()[num] # readlines() возвращает файл в виде строк
    f_tags.close()

    if(c != "@" and c != "@\n" and c != "@ \n"):
        # @ означает незаполненную строку тегов
        return c
    else:
        return ""

def readdate(num):
    f_date = open("files/dates.txt", "r")
    c = f_date.readlines()[num].strip().split("/")
    f_date.close()
    return c

def changename(num, newtext):
    f_names = open("files/names.txt", "w")

    names[num] = newtext

    if len(newtext) < len_names:
        labels[num] = newtext
    else:
        labels[num] = labels[num][:len_names] + "…"

    for l in names:
        f_names.write(l + '\n')

    f_names.close()

def changetext(num, newtext):
    f_text = open("files/" + listfiles[num], "w") # весь файл стирается
    f_text.write(newtext)
    f_text.close()

def changetags(num, newtags):
    f_tags = open("files/tags.txt", "r")
    t = f_tags.readlines()
    f_tags.close()

    if(newtags != ""):
        t[num] = newtags + '\n'
    else:
        t[num] = "@" + '\n'

    f_tags = open("files/tags.txt", "w")

    for tag in t:
        f_tags.write(tag)
    
    f_tags.close()
    
def changedate(num, date):
    f_date = open("files/dates.txt", "r")
    dates = f_date.readlines()
    f_date.close()

    t = dates[num].split("/")
    dates[num] = t[0].strip() + "/" + date + "\n"

    f_date = open("files/dates.txt", "w")
    for dat in dates:
        f_date.write(dat)
    f_date.close()

    t[0] = t[0].strip()
    t.append(date)

    return t

def delete(num):
    os.remove("files/" + listfiles[num])
    listfiles.pop(num)
    names.pop(num)
    labels.pop(num)

    f_name = open("files/names.txt", "r")
    f_names = f_name.readlines()
    f_names.pop(num)
    f_name.close()

    f_name = open("files/names.txt", "w")
    for l in f_names:
        f_name.write(l)
    f_name.close()

    f_tag = open("files/tags.txt", "r")
    f_tags = f_tag.readlines()
    f_tags.pop(num)
    f_tag.close()

    f_tag = open("files/tags.txt", "w")
    for l in f_tags:
        f_tag.write(l)
    f_tag.close()

    f_date = open("files/dates.txt", "r")
    f_dates = f_date.readlines()
    f_dates.pop(num)
    f_date.close()

    f_date = open("files/dates.txt", "w")
    for d in f_dates:
        f_date.write(d)
    f_date.close()

def lastRecordNum():
    if len(listfiles) != 0:
        return ex_functions.sorting(listfiles[-1])
    else:
        return 0

def createNewPost(num, name, text, tags, date):
    # один из приемлемых способов создания файлов
    with open("files/record%d.txt" % num, "tw", encoding="ANSI") as f:
        f.write(text)
        f.close()

    f = open("files/names.txt", "a") # открытие на дозапись
    f.write(name + '\n')
    f.close()

    f = open("files/tags.txt", "a")
    if(tags != ""):
        f.write(tags + '\n')
    else:
        f.write("@\n")
    f.close()

    listfiles.append("record%d.txt" % num)

    names.append(name)

    if len(name) > len_names:
        labels.append(name)
    else:
        labels.append(name[:len_names] + "…")

    f = open("files/dates.txt", "a")
    f.write(date + '\n')
    f.close()

if __name__ == '__main__':
    print(names)
    print(listfiles)
    print(os.access("file.py", os.F_OK))
