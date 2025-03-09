submissions = {}
languages = {}

while True:
    submission = input()

    if submission == "exam finished":
        break

    submission = submission.split("-")
    name = submission[0]
    language = submission[1]

    if language == "banned":
        del submissions[name]
        continue

    if language in languages.keys():
        languages[language] += 1
    else:
        languages[language] = 1

    points = int(submission[2])

    if name not in submissions.keys():
        submissions[name] = points
    else:
        if submissions[name] < points:
            submissions[name] = points

print("Results:")
for key, value in submissions.items():
    print(f"{key} | {value}")

print("Submissions:")
for key, value in languages.items():
    print(f"{key} - {value}")
