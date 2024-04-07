import streamlit as st

from utils import df, en_createResultDf, tr_createResultDf

st.title("Exam Genius📚")

language_on = st.toggle("🇺🇸 EN", key="language_toggle", value=False)

if language_on:
    st.write("### 2023 Fall Semester Final Exam Dates")
    st.write("Below are the final exam dates for the 2023 Fall semester.")
    st.write(
        "Please select the course codes of the courses for which you want to see the exam dates."
    )
    course_list = st.multiselect(
        "Select Courses", df["DERS KODU"].str.upper(), placeholder="Course Code"
    )  # Ders kodlarını büyük harfe dönüştür
    col1, col2 = st.columns(2)
    if len(course_list) > 0 and col1.button("Show Exam Dates"):
        result_df = en_createResultDf(course_list)
        st.dataframe(result_df, hide_index=True)
        # col2.download_button("Download Calendar", "main.py")

else:
    st.write("### 2023 Güz Dönemi Final Sınav Tarihleri")
    st.write("Aşağıda 2023 Güz dönemi için final sınav tarihleri yer almaktadır.")
    st.write("Lütfen sınav tarihlerini görmek istediğiniz ders kodlarını seçin.")
    course_list = st.multiselect(
        "Dersleri Seçin", df["DERS KODU"].str.upper(), placeholder="Ders Kodu"
    )
    col1, col2 = st.columns(2)
    if len(course_list) > 0 and col1.button("Sınav Tarihlerini Göster"):
        result_df = tr_createResultDf(course_list)
        st.dataframe(result_df, hide_index=True)
        # col2.download_button("Takvimi İndir", "main.py")
