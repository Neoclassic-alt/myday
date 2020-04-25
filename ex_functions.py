import re
from collections import Counter # подсчёт встречаемости слов
import _operator
from datetime import datetime

# Регулярные выражения - это очень мощная сила.
# Но с великой силой приходит и великая ответственность. (с)

# Для имён вроде "recordXXX.txt" довольно простая регулярка:
# record\d+\.txt

pattern = r"\d+"

def sorting(key):
    return int(re.search(pattern, key).group())

class tagsProcessing():
    def __init__(self):
        f = open("files/tags.txt", "r")
        self.tags = f.read()
        f.close()
        self.tags = self.tags.split("\n")
        self.n_tags = []
        for i in self.tags:
            self.n_tags.extend(i.split(","))
        self.n_tags = list(map(lambda x: x.strip().lower(), self.n_tags))
        while self.n_tags.count("@") > 0:
            self.n_tags.remove("@")
        while self.n_tags.count("") > 0:
            self.n_tags.remove("")
        self.s_tags = Counter(self.n_tags)

    def printTags(self):
        s_arr = []
        self.sortedTags = []
        si_tags = list(self.s_tags.items())
        si_tags.sort(key=_operator.itemgetter(1))
        si_tags.reverse()
        for i in si_tags:
            s_arr.append("{0} ({1})".format(i[0], i[1]))
            self.sortedTags.append(i[0])
        return s_arr

    def selectPosts(self, nums):
        # примеры: 12; запись12, 12; 12, 11efe; 1111, 12, thewor. Надо найти 12.
        self.selectedPostsNumber = set()

        for i in nums: # Держится на честном слове. Руками не трогать!
            t = self.sortedTags[i]
            pattern = r"\b%s\b" % t # \b - граница слова
            for tag in self.tags:
                c = re.search(pattern, tag)
                if c != None:
                    self.selectedPostsNumber.add(self.tags.index(tag))

        return self.selectedPostsNumber

    # self.tags - теги одной записи группируются под одной строкой,
    # self.n_tags - теги (не уникальные) расположены отдельно в массиве,
    # self.s_tags - словарь встречаемости тегов
    # self.sortedTags - отсортированные теги

def getNowTime():
    return datetime.today().strftime("%d.%m.%Y, %H:%M")

if __name__ == '__main__':
    #print(re.search(pattern, "record22.txt").group())
    #print(re.search(pattern, "record1.txt").group())
    #tagsProcessing()
    #months = {January: "Январь", February: "Февраль", March: "Март", April: "Апрель", May: "Май"}
    pass