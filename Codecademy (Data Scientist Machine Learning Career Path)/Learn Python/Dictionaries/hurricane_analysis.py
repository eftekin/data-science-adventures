# names of hurricanes
names = [
    "Cuba I",
    "San Felipe II Okeechobee",
    "Bahamas",
    "Cuba II",
    "CubaBrownsville",
    "Tampico",
    "Labor Day",
    "New England",
    "Carol",
    "Janet",
    "Carla",
    "Hattie",
    "Beulah",
    "Camille",
    "Edith",
    "Anita",
    "David",
    "Allen",
    "Gilbert",
    "Hugo",
    "Andrew",
    "Mitch",
    "Isabel",
    "Ivan",
    "Emily",
    "Katrina",
    "Rita",
    "Wilma",
    "Dean",
    "Felix",
    "Matthew",
    "Irma",
    "Maria",
    "Michael",
]

# months of hurricanes
months = [
    "October",
    "September",
    "September",
    "November",
    "August",
    "September",
    "September",
    "September",
    "September",
    "September",
    "September",
    "October",
    "September",
    "August",
    "September",
    "September",
    "August",
    "August",
    "September",
    "September",
    "August",
    "October",
    "September",
    "September",
    "July",
    "August",
    "September",
    "October",
    "August",
    "September",
    "October",
    "September",
    "September",
    "October",
]

# years of hurricanes
years = [
    1924,
    1928,
    1932,
    1932,
    1933,
    1933,
    1935,
    1938,
    1953,
    1955,
    1961,
    1961,
    1967,
    1969,
    1971,
    1977,
    1979,
    1980,
    1988,
    1989,
    1992,
    1998,
    2003,
    2004,
    2005,
    2005,
    2005,
    2005,
    2007,
    2007,
    2016,
    2017,
    2017,
    2018,
]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [
    165,
    160,
    160,
    175,
    160,
    160,
    185,
    160,
    160,
    175,
    175,
    160,
    160,
    175,
    160,
    175,
    175,
    190,
    185,
    160,
    175,
    180,
    165,
    165,
    160,
    175,
    180,
    185,
    175,
    175,
    165,
    180,
    175,
    160,
]

# areas affected by each hurricane
areas_affected = [
    ["Central America", "Mexico", "Cuba", "Florida", "The Bahamas"],
    ["Lesser Antilles", "The Bahamas", "United States East Coast", "Atlantic Canada"],
    ["The Bahamas", "Northeastern United States"],
    ["Lesser Antilles", "Jamaica", "Cayman Islands", "Cuba", "The Bahamas", "Bermuda"],
    ["The Bahamas", "Cuba", "Florida", "Texas", "Tamaulipas"],
    ["Jamaica", "Yucatn Peninsula"],
    ["The Bahamas", "Florida", "Georgia", "The Carolinas", "Virginia"],
    ["Southeastern United States", "Northeastern United States", "Southwestern Quebec"],
    ["Bermuda", "New England", "Atlantic Canada"],
    ["Lesser Antilles", "Central America"],
    ["Texas", "Louisiana", "Midwestern United States"],
    ["Central America"],
    ["The Caribbean", "Mexico", "Texas"],
    ["Cuba", "United States Gulf Coast"],
    ["The Caribbean", "Central America", "Mexico", "United States Gulf Coast"],
    ["Mexico"],
    ["The Caribbean", "United States East coast"],
    ["The Caribbean", "Yucatn Peninsula", "Mexico", "South Texas"],
    ["Jamaica", "Venezuela", "Central America", "Hispaniola", "Mexico"],
    ["The Caribbean", "United States East Coast"],
    ["The Bahamas", "Florida", "United States Gulf Coast"],
    ["Central America", "Yucatn Peninsula", "South Florida"],
    ["Greater Antilles", "Bahamas", "Eastern United States", "Ontario"],
    ["The Caribbean", "Venezuela", "United States Gulf Coast"],
    ["Windward Islands", "Jamaica", "Mexico", "Texas"],
    ["Bahamas", "United States Gulf Coast"],
    ["Cuba", "United States Gulf Coast"],
    ["Greater Antilles", "Central America", "Florida"],
    ["The Caribbean", "Central America"],
    ["Nicaragua", "Honduras"],
    [
        "Antilles",
        "Venezuela",
        "Colombia",
        "United States East Coast",
        "Atlantic Canada",
    ],
    [
        "Cape Verde",
        "The Caribbean",
        "British Virgin Islands",
        "U.S. Virgin Islands",
        "Cuba",
        "Florida",
    ],
    [
        "Lesser Antilles",
        "Virgin Islands",
        "Puerto Rico",
        "Dominican Republic",
        "Turks and Caicos Islands",
    ],
    ["Central America", "United States Gulf Coast (especially Florida Panhandle)"],
]

# damages (USD($)) of hurricanes
damages = [
    "Damages not recorded",
    "100M",
    "Damages not recorded",
    "40M",
    "27.9M",
    "5M",
    "Damages not recorded",
    "306M",
    "2M",
    "65.8M",
    "326M",
    "60.3M",
    "208M",
    "1.42B",
    "25.4M",
    "Damages not recorded",
    "1.54B",
    "1.24B",
    "7.1B",
    "10B",
    "26.5B",
    "6.2B",
    "5.37B",
    "23.3B",
    "1.01B",
    "125B",
    "12B",
    "29.4B",
    "1.76B",
    "720M",
    "15.1B",
    "64.8B",
    "91.6B",
    "25.1B",
]

# deaths for each hurricane
deaths = [
    90,
    4000,
    16,
    3103,
    179,
    184,
    408,
    682,
    5,
    1023,
    43,
    319,
    688,
    259,
    37,
    11,
    2068,
    269,
    318,
    107,
    65,
    19325,
    51,
    124,
    17,
    1836,
    125,
    87,
    45,
    133,
    603,
    138,
    3057,
    74,
]

# Update Recorded Damages
conversion = {"M": 1000000, "B": 1000000000}

updated_damages = []

for damage in damages:
    if damage[-1] == "M":
        updated_damages.append(float(damage[:-1]) * conversion["M"])
    elif damage[-1] == "B":
        updated_damages.append(float(damage[:-1]) * conversion["B"])
    else:
        updated_damages.append(damage)

# test function by updating damages
# print(updated_damages)


# 2
# Create a Table
def get_hurricanes(
    names, months, years, max_sustained_winds, areas_affected, damages, deaths
):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damage": damages[i],
            "Deaths": deaths[i],
        }
    return hurricanes


hurricanes = get_hurricanes(
    names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths
)
# print(hurricanes)

# Table by years
hurricanesYears = []

for name, month, year, max_wind, area, damage, death in zip(
    names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths
):
    dict = {
        year: {
            "Name": name,
            "Month": month,
            "Year": year,
            "Max_sustained_wind": max_wind,
            "Area_affected": area,
            "Damage": damage,
            "Deaths": death,
        }
    }
    hurricanesYears.append(dict)
# print(hurricanesYears)

# count areas
countArea = {}
for area in areas_affected:
    for i in area:
        if i not in countArea:
            countArea[i] = 1
        else:
            countArea[i] += 1
# print(countArea)


# find the area affected by the most
def affected_max(countArea):
    maxArea = ""
    maxCount = 0

    for area in countArea:
        if countArea[area] > maxCount:
            maxArea = area
            maxCount = countArea[area]
    return maxArea, maxCount


maxArea, maxCount = affected_max(countArea)
# print(maxArea, maxCount)


# find the hurricane that caused the greatest number of deaths
def death_max(hurricanes):
    maxDeath = ""
    maxDeathCount = 0
    for hurricane in hurricanes:
        if hurricanes[hurricane]["Deaths"] > maxDeathCount:
            maxDeath = hurricanes[hurricane]["Name"]
            maxDeathCount = hurricanes[hurricane]["Deaths"]
    return maxDeath, maxDeathCount


maxDeath, maxDeathCount = death_max(hurricanes)
# print(maxDeath, maxDeathCount)


# function that rates hurricanes on a mortality scale
def mortality(hurricanes):
    mortality_rates = {0: [], 1: [], 2: [], 3: [], 4: []}

    for hurricane in hurricanes:
        rate = 0
        deaths = hurricanes[hurricane]["Deaths"]

        if deaths < 100:
            rate = 0
        elif deaths < 500:
            rate = 1
        elif deaths < 1000:
            rate = 2
        elif deaths < 10000:
            rate = 3
        else:
            rate = 4

        mortality_rates[rate].append(hurricanes[hurricane])
    return mortality_rates


# print(mortality(hurricanes))


# find the hurricane that caused the greatest damage
def damageMax(hurricanes):
    maxDamage = ""
    maxDamageCost = 0.0
    for hurricane in hurricanes:
        if (
            hurricanes[hurricane]["Damage"] != "Damages not recorded"
            and float(hurricanes[hurricane]["Damage"]) > maxDamageCost
        ):
            maxDamage = hurricanes[hurricane]["Name"]
            maxDamageCost = float(hurricanes[hurricane]["Damage"])
    return maxDamage, maxDamageCost


maxDamage, maxDamageCost = damageMax(hurricanes)
# print(maxDamage, maxDamageCost)


damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}


def damageScale(hurricanes):
    damageRates = {0: [], 1: [], 2: [], 3: [], 4: []}

    for hurricane in hurricanes:
        rate = 0
        damage = hurricanes[hurricane]["Damage"]

        if damage == "Damages not recorded":
            continue
        elif damage < damage_scale[1]:
            rate = 0
        elif damage < damage_scale[2] and damage >= damage_scale[1]:
            rate = 1
        elif damage < damage_scale[3] and damage >= damage_scale[2]:
            rate = 2
        elif damage < damage_scale[4] and damage >= damage_scale[3]:
            rate = 3
        else:
            rate = 4
        damageRates[rate].append(hurricanes[hurricane])
    return damageRates


# print(damageScale(hurricanes))
