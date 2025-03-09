companies = {}

while True:
    user = input()

    if user == "End":
        break

    company, user_id = user.split(" -> ")

    if company not in companies.keys():
        companies[company] = []

    if user_id not in companies[company]:
        companies[company].append(user_id)

for company, employees in companies.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")