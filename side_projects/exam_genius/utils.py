# Import the necessary libraries
import datetime

import pandas as pd
import plotly.figure_factory as ff
import requests
from unidecode import unidecode


# Define the function to format date strings
def format_date(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str.split(" ")[0], "%Y-%m-%d")
    except ValueError:
        try:
            date_obj = datetime.datetime.strptime(date_str.split(" ")[0], "%d.%m.%Y")
        except ValueError:
            return "Invalid date format"

    formatted_date = date_obj.strftime("%d/%m/%Y")
    return formatted_date


# Read the Excel file into a DataFrame
url = "https://halic.edu.tr/tr/s-duyurular/Documents/2024/06/10/2023-2024-bahar-donemi-final-sinavlari-tum-liste.xlsx"
midterm_xls = requests.get(url)

df = pd.read_excel(midterm_xls.content)
# Define column names for clarity
exam_date_column = "SINAV GÜNÜ"
exam_time_column = "BAŞLANGIÇ SAATİ"
course_code_column = "DERS KODU"
course_name_column = "DERS ADI"
course_code_and_name_column = "DERS KODU VE ADI"
classroom_code_column = "DERSLİK KODLARI"

# Clean up the data in the DataFrame
df[course_code_column] = df[course_code_column].apply(lambda x: x.split(";")[0])
df[course_name_column] = df[course_name_column].apply(lambda x: x.split(";")[0])
df[classroom_code_column] = df[classroom_code_column].apply(lambda x: str(x))
df[classroom_code_column] = df[classroom_code_column].apply(
    lambda x: x.replace(";", ",")
)
df[course_code_column] = df[course_code_column].apply(lambda y: unidecode(y).lower())

# Select relevant columns and group the data
df = df[
    [
        exam_date_column,
        exam_time_column,
        course_code_column,
        course_name_column,
        classroom_code_column,
    ]
]

df = (
    df.groupby(course_code_column)
    .agg(
        {
            exam_date_column: "first",
            exam_time_column: "first",
            course_name_column: "first",
            classroom_code_column: ", ".join,
        }
    )
    .reset_index()
)

df = df[
    [
        exam_date_column,
        exam_time_column,
        course_code_column,
        course_name_column,
        classroom_code_column,
    ]
].sort_values(by=exam_date_column)

# Add a column for course code and name
df[course_code_and_name_column] = (
    df[course_code_column].str.upper() + " (" + df[course_name_column] + ")"
)

course_list = []


# Retrieve and format the exam date and time in Turkish
def tr_getExamDate(course_code):
    date = df[df[course_code_and_name_column] == course_code][exam_date_column].values[
        0
    ]
    week_day = date.split(" ")[1]
    date_full = format_date(date)
    date = date_full + " " + week_day
    time = df[df[course_code_and_name_column] == course_code][exam_time_column].values[
        0
    ]
    if isinstance(time, str):
        try:
            time_obj = datetime.datetime.strptime(time, "%H:%M:%S").time()
        except ValueError:
            time_obj = datetime.datetime.strptime(time, "%H:%M").time()
    else:
        time_obj = time
    time_str = time_obj.strftime("%H:%M")
    return str(date) + " " + time_str


# Retrieve and format the exam date and time in English
def en_getExamDate(course_code):
    date = df[df[course_code_and_name_column] == course_code][exam_date_column].values[
        0
    ]
    date_formatted = format_date(date.split(" ")[0])
    date_en = (
        date_formatted
        + " "
        + datetime.datetime.strptime(date_formatted, "%d/%m/%Y").strftime("%A")
    )
    time = df[df[course_code_and_name_column] == course_code][exam_time_column].values[
        0
    ]
    if isinstance(time, str):
        try:
            time_obj = datetime.datetime.strptime(time, "%H:%M:%S").time()
        except ValueError:
            time_obj = datetime.datetime.strptime(time, "%H:%M").time()
    else:
        time_obj = time
    time_str = time_obj.strftime("%H:%M")
    return date_en + " " + time_str


# Retrieve the course name
def getCourseName(course_code):
    name = df[df[course_code_and_name_column] == course_code][
        course_name_column
    ].values[0]
    return name


# Retrieve and format the classroom information
def getClassroom(course_code):
    classroom = df[df[course_code_and_name_column] == course_code][
        classroom_code_column
    ].values[0]
    if len(classroom.split(",")) > 5:
        classroom = classroom.split(",")[:5]
        classroom = ",".join(str(element) for element in classroom) + "..."
    return classroom


# Create a DataFrame in English
def en_createResultDf(course_list):
    result_df_en = pd.DataFrame(
        [], columns=["Course Name", "Exam Date", "Classroom Codes"]
    )
    for course in course_list:
        list_row = [getCourseName(course), en_getExamDate(course), getClassroom(course)]
        result_df_en.loc[len(result_df_en)] = list_row
    result_df_en = result_df_en.sort_values("Exam Date")
    return result_df_en


# Create a DataFrame in Turkish
def tr_createResultDf(course_list):
    result_df_tr = pd.DataFrame([], columns=["Ders Adı", "Sınav Tarihi", "Sınıf"])
    for course in course_list:
        list_row = [getCourseName(course), tr_getExamDate(course), getClassroom(course)]
        result_df_tr.loc[len(result_df_tr)] = list_row
    result_df_tr = result_df_tr.sort_values("Sınav Tarihi")
    return result_df_tr


# Create an image of the result DataFrame
def createImage(df):
    course_list = list(df.iloc[:, 0])
    scale = 21
    width = max([len(course_name) * scale for course_name in course_list])
    fig = ff.create_table(df)
    if width > 800:
        fig.layout.width = width
    else:
        fig.layout.width = 800
    fig.update_layout(autosize=True)
    fig.write_image("output/examgenius.png", scale=2)
