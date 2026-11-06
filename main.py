# 가위 바위 보 게임 (3판 2선승제)
import random

# 번호와 손 저장한 딕셔너리
HANDS = {1:"가위", 2:"바위", 3:"보"}

# 게임 타이틀 출력
def show_title():
    print("="*40)
    print("가위/바위/보 게임")
    print("="*40)

# 플레이어 이름 입력
def ask_name():
    name = input("플레이어 이름을 입력하세요. ").strip()
    if name == "":
        name = "게스트"

    return name


# 게임의 전체 루프
def main():
    show_title()
    name = ask_name()
    
    computer_number = random.randint(1, 3) # 1, 2, 3
    print(f"{name}님, 컴퓨터는 {HANDS[computer_number]}를 냈습니다.")

# 게임 시작
main()

