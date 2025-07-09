# 這是我的第一個專案

balance = 0
records = []

while True:
    action = input("輸入類型（income/expense/end）：")
    if action == "end":
        break
    amount = int(input("金額："))
    if action == "income":
        balance += amount
    elif action == "expense":
        balance -= amount
    records.append((action, amount))
    print(f"目前結餘：{balance}")

print("記錄如下：")
for r in records:
    print(r)
