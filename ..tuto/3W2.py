hp=100
name = input("이름을 입력하세요 > ")
print(name,"님 반갑습니다.",name,"(HP 100)으로 게임을 시작 합니다.")
print("WARNING WARNING WARNING")
print("옆집 강아지를 만났습니다.")

cho = input("1.싸운다 2.도망간다 >>")
if cho == "1" and"싸운다":
    print("다리를 다쳐 HP:",hp-80,"남았습니다.")
    print("당신 현재 HP:",hp,"입니다")
    print("병원으로 이송됩니다.")
elif cho == "2" and"도망간다":
        print("수치심을 느껴 HP:",hp-50,"남았습니다.")
        print("당신 현재 HP:",hp,"입니다")
        print("집으로 안전히 돌아갑니다.")           
else:
        print("없는 선택이라 HP:",hp-100,"GAME OVER")
    
    