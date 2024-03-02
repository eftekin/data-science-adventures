from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_list = r.generate_users(10)
# print(some_list)

name = r.get_full_name()

# for user in some_list:
#     print(user.get_full_name(), " ", user.get_email())

# for user in some_list:
#     print(user.get_full_name(), " ", user.get_picture())


def get_users():
    users = []
    for user in RandomUser.generate_users(10):
        users.append({"Name": user.get_full_name(), "Gender": user.get_gender(), "City": user.get_city(
        ), "State": user.get_state(), "Email": user.get_email(), "DOB": user.get_dob(), "Picture": user.get_picture()})

    return pd.DataFrame(users)


print(get_users())
