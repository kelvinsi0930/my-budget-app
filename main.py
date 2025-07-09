# 這是我的第一個專案

balance = 0
records = []

while True:
    action = input("輸入類型（收入/支出/結束）：")
    if action == "結束":
        break
    amount = int(input("金額："))
    if action == "收入":
        balance += amount
    elif action == "支出":
        balance -= amount
    records.append((action, amount))
    print(f"目前結餘：{balance}")

print("記錄如下：")
for r in records:
    print(r)
