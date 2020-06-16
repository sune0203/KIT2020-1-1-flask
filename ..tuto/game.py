import random
def game(num, character):
    if num == 1:
        while(True):
            try:
                print("1. 스킬 2. 아이템")
                num = int(input("선택 :"))
                break
            except:
                print("숫자만 입력 하세요")
        if num == 1:
            print(random.choice(character["skill"]))
            print("패기의 감탄하여 스카웃")
        elif num ==2:
            print(random.choice(character["items"]))
            print("버텼다.")
    elif num ==2:
        print("도망가다 조폭에게 맞아서 GAME OVER")
    else:
        print("입력을 잘못 했습니다.")

def charact(name):
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
        print("%s:%s" % (key, character[key]))
        f.write("%s:%s\n" % (key, character[key]))
    f.close()

name = input("이름을 입렵하세요 : ")

#캐릭터 설정 함수
character = charact(name)

# 캐릭터 정보 파일에 저장
save_game("save.txt", character)

print("길을 가다가 조폭을 만났습니다.")
while(True):
    try:
        print("1. 싸운다 2. 도망간다")
        num = int(input("선택 :"))
        break
    except:
        print("숫자만 입력 하세요")

game(num, character)
