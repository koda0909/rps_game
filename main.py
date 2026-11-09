# 가위 바위 보 게임 (3판 2선승제)
import random

# 번호와 손 저장한 딕셔너리
HANDS = {1:"가위", 2:"바위", 3:"보"}
# 게임의 종료 조건
GOAL_WINS = 2

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

# 플레이어 번호 입력
def ask_number():
    while True:
        print("1.가위 / 2. 바위 / 3. 보")
        answer = input('번호를 선택하세요. : ').strip()

        if answer in ("1", "2", "3"):
            return int(answer)

        print("1, 2, 3 중에서 입력하세요.")

# 승패 판정
# 1 - 1 / 2 - 2 / 3 - 3 무승부 조건 판정
# 1 - 3 / 2 - 1 / 3 - 2 플레이어 승리 조건
# 무승부 / 승리 / 패배
def check_result(user_number, computer_nummber):
    # 무승부 조건
    if user_number == computer_nummber:
        return "무승부"

    # 플레이어 승리 조건
    if user_number == 1 and computer_nummber == 3: return "승리" # 가위 / 보
    if user_number == 2 and computer_nummber == 1: return "승리" # 바위 / 가위
    if user_number == 2 and computer_nummber == 2: return "승리" # 보 / 바위

    return "패배"

# 한판의 게임 결과 출력
def show_result(name, user_number, computer_number, result):
    print("\n[게임 결과]")
    print(f"{name}: {HANDS[user_number]} vs 컴퓨터: {HANDS[computer_number]}}}")
    print(f"=>{result}")

# 현재 스코어 표시
def show_score(name, my_wins, computer_wins):
    print(f"\n현재 스코어 {name} {my_wins} : {computer_wins} 컴퓨터\n") # 게스트 1 : 0 컴퓨터

# 최종 결과
def show_final_result(name, my_wins, computer_wins):
    print("-"*40)
    print(f"[최종 결과] {name} {my_wins} : {computer_wins} 컴퓨터")
    if my_wins > computer_wins:
        print(f"==> {name} 최종승리!")
    else:
        print("==> 컴퓨터 승리!")

# 승패 판정 목록
def show_records(recodes):
    print("\n[판별 승패 목록]")
    # "1 판 : 가위 vs 바위 => 패배"
    # "2 판 : 바위 vs 보 => 패배"
    # "3 판 : 보 vs 가위 => 패배"
    for number, record in enumerate(recodes, start=1):
        print(f"{number}판 : {record}")

# 게임 재시작 여부
def ask_play_again():
    while True:
        answer = input("\n다시 도전 (yes/no) : ").strip().lower()
        if answer == "yes" or answer == "y":
            return True
        if answer == "no" or answer == "n":
            return False

        print("yes 또는 no를 입력하세요")

# 게임 루프 (3판 2선승제)
def play_game(name):
    my_wins = 0
    computer_wins = 0
    records = [] # 승패 기록할 리스트
    # 둘 다 2승이 안됬을 떄 다음 판을 진행
    while my_wins < GOAL_WINS and computer_wins < GOAL_WINS:
        user_number = ask_number()
        computer_number = random.randint(1, 3) # 1, 2, 3
        # 승패 판정
        result = check_result( user_number , computer_number)

        if result == "승리":
            my_wins += 1
        elif result == "패배":
            computer_wins += 1

        # 승패 결과 목록에 저장
        records.append(f"{HANDS[user_number]} vs {HANDS[computer_number]} => {result}")

        show_result(name, user_number, computer_number, result)
        show_score(name, my_wins, computer_wins)

    show_final_result(name, my_wins, computer_wins)
    show_records(records)
    # 플레이어가 승리하면 True
    return my_wins == GOAL_WINS


# 게임의 전체 루프
def main():
    show_title()
    name = ask_name()
    # 연승 기록을 위한 변수
    co_wins = 0

    while True:
        my_won = play_game(name)
        if my_won:
            co_wins += 1    # 연승기록 누적
        else:
            co_wins = 0     # 연승기록 초기화

        if co_wins > 0:
            print(f"\n현재연승: {co_wins}연승")

        if not ask_play_again():
            break

    print("게임을 종료합니다")



# 게임 시작
main()

