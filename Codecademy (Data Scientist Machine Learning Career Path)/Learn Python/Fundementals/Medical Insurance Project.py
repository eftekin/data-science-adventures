def analyze_smoker(smoker_status):
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")


def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + \
        425*num_of_children + 24000*smoker - 12500
    print("The estimated insurance cost for " + name +
          " is " + str(estimated_cost) + " dollars")
    analyze_smoker(smoker)
    print("")
    return estimated_cost


# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)

# Estimate Maria's insurance cost
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)

# Estimate Mustafa's insurance cost
mustafa_insurance_cost = calculate_insurance_cost("Mustafa", 21, 1, 35, 0, 0)
