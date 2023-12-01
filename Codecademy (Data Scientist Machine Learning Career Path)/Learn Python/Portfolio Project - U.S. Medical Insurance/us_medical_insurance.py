import csv

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

with open("insurance.csv") as insurance_csv:
    insurance_dict = csv.DictReader(insurance_csv)
    for row in insurance_dict:
        ages.append(row["age"])
        sexes.append(row["sex"])
        bmis.append(row["bmi"])
        num_children.append(row["children"])
        smoker_statuses.append(row["smoker"])
        regions.append(row["region"])
        insurance_charges.append(row["charges"])


def analyze_ages():
    total_age = 0
    for age in ages:
        total_age += int(age)
    average_age = total_age / len(ages)

    return "Average Patient Age is " + str(round(average_age, 2))


def analyze_sexes():
    female_count = 0
    male_count = 0

    for sex in sexes:
        if sex == "female":
            female_count += 1
        elif sex == "male":
            male_count += 1
    print("Count for female: " + str(female_count))
    print("Count for male: " + str(male_count))


def analyze_charges():
    total_charge = 0

    for charge in insurance_charges:
        total_charge += float(charge)
        average_charge = total_charge / len(insurance_charges)

    return "Average charge is " + str(round(average_charge, 2))


print(analyze_ages())
analyze_sexes()
print(analyze_charges())
