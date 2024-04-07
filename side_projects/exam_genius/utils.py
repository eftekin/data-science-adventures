import datetime

import pandas as pd
import requests
from unidecode import unidecode

url = "https://halic.edu.tr/tr/s-duyurular/Documents/2024/01/02/2023-2024-guz-donemi-final-sinav-programi-all-list.xlsx"
midterm_xls = requests.get(url)

df = pd.read_excel(midterm_xls.content)

exam_date_column = "SINAV GÜNÜ"
exam_time_column = "BAŞLANGIÇ SAATİ"
course_code_column = "DERS KODU"
course_name_column = "DERS ADI"
classroom_code_column = "DERSLİK KODLARI"


df[course_code_column] = df[course_code_column].apply(lambda x: x.split(";")[0])
df[course_name_column] = df[course_name_column].apply(lambda x: x.split(";")[0])
df[classroom_code_column] = df[classroom_code_column].apply(lambda x: str(x))
df[classroom_code_column] = df[classroom_code_column].apply(
    lambda x: x.replace(";", ",")
)
df[course_code_column] = df[course_code_column].apply(lambda y: unidecode(y).lower())

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

course_list = []


def tr_getExamDate(course_code):
    course_code = unidecode(course_code).lower()

    date = df[df[course_code_column] == course_code][exam_date_column].values[0]
    week_day = date.split(" ")[1]
    date_full = datetime.datetime.strptime(date.split(" ")[0], "%Y-%m-%d").strftime(
        "%d/%m/%Y"
    )
    date = date_full + " " + week_day
    time = df[df[course_code_column] == course_code][exam_time_column].values[0]
    return str(date) + " " + str(time)


def en_getExamDate(course_code):
    course_code = unidecode(course_code).lower()

    date = df[df[course_code_column] == course_code][exam_date_column].values[0]
    date_en = datetime.datetime.strptime(date.split(" ")[0], "%Y-%m-%d").strftime(
        "%d/%m/%Y %A"
    )
    date = date_en

    time = df[df[course_code_column] == course_code][exam_time_column].values[0]
    return date + " " + time


def getCourseName(course_code):
    course_code = unidecode(course_code).lower()
    name = df[df[course_code_column] == course_code][course_name_column].values[0]
    return name


def getClassroom(course_code):
    course_code = unidecode(course_code).lower()
    classroom = df[df[course_code_column] == course_code][classroom_code_column].values[
        0
    ]
    classroom = classroom.split(",")[:5]
    classroom = ",".join(str(element) for element in classroom)
    return classroom


def en_createResultDf(course_list):
    result_df_en = pd.DataFrame(
        [],
        columns=["Course Name", "Exam Date", "Classroom Codes"],
    )
    for course in course_list:
        list_row = [getCourseName(course), en_getExamDate(course), getClassroom(course)]
        result_df_en.loc[len(result_df_en)] = list_row
    result_df_en = result_df_en.sort_values("Exam Date")
    return result_df_en


def tr_createResultDf(course_list):
    result_df_tr = pd.DataFrame(
        [],
        columns=["Ders Adı", "Sınav Tarihi", "Sınıf"],
    )
    for course in course_list:
        list_row = [getCourseName(course), tr_getExamDate(course), getClassroom(course)]
        result_df_tr.loc[len(result_df_tr)] = list_row
    result_df_tr = result_df_tr.sort_values("Sınav Tarihi")
    return result_df_tr
