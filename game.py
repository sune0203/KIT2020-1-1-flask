def set_charact(name):
    character = {
        "name": name,
        "level": 1,
        "hp": 100,
        "items":["체력포션", "마나포션", "뇌물"],
        "skill":["주먹질","도발","발차기"]
    }
    print("{0}님 반갑습니다. (HP {1})으로 게임을 시작 합니다".format(character["name"], character["hp"]))
    return character

def save_game(filename, charact):
    f = open("save.txt", "w", encoding="utf-8")
    for key in charact:
        print("%s:%s" % (key, charact[key]))
        f.write("%s:%s\n" % (key, charact[key]))
    f.close()