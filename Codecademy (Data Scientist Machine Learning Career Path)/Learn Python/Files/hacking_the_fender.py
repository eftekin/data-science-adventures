import csv

compromised_users = []
slash_null_sig = "U  G O T  H A C K E D  =  S L A S H  N U L L"

with open("passwords.csv") as passwords_file:
    password_csv = csv.DictReader(passwords_file)
    for password_row in password_csv:
        compromised_users.append(password_row["Username"])

with open("compromised_users.txt", "w") as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user)

import json

with open("boss_message.json", "w") as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)

with open("new_passwords.csv", "w") as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)
