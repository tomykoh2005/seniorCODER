import time
import json
Time = 1
playerDict = []

class Server:
    
    def infoGet(self):
        q1 = str(input("이름이 뭔가요?: "))
        newPlayer = {"name": q1, "level": 1, "money": 30000}
        playerDict.append(newPlayer)
        print("저장되었습니다.\n\n")
        time.sleep(Time)
        print(f"""===============================
회원님의 정보는 다음과 같습니다.
이름: {playerDict[-1]["name"]}
레벨: {playerDict[-1]["level"]}
현금: {playerDict[-1]["money"]}
===============================""")
        with open ("userData.txt", "a", encoding = "utf-8") as file:
            file.write(f"{newPlayer['name']}, {newPlayer['level']}, {newPlayer['money']}\n")
            
#=======================================cutting==========================================

try:
    with open("userData.txt", "r", encoding = "utf-8") as file:
        for line in file:
            if line.strip():
                name, level, money = line.strip().split(", ")
                playerDict.append({
                    "name": name,
                    "level": int(level),
                    "money": int(money)
                })
except FileNotFoundError:
    pass

query = str(input("====이름이 뭔가요?===="))
isFound = False

for player in playerDict:
    if player["name"] == query:
        print("====당신의 정보입니다====")
        print("\n\n")
        print(f"""=================
이름: {player["name"]}
레벨: {player["level"]}
현금: {player["money"]}
=================""")
        isFound = True
        break

if not isFound:
    print("""회원님의 정보는 없습니다.
새로 만들겠습니다.""")
    time.sleep(Time)
    main = Server()
    main.infoGet()
