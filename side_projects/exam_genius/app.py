import streamlit as st

from utils import createImage, df, en_createResultDf, tr_createResultDf

last_update = "10.06.2024 17:55"

st.title("Exam Genius📚")

language_on = st.toggle("🇺🇸 EN", key="language_toggle", value=False)

if language_on:
    st.write("### 2024 Spring Semester Final Exam Dates")
    st.write("Below are the final exam dates for the 2024 Spring semester.")
    st.write(
        "Please select the course codes of the courses for which you want to see the exam dates."
    )
    course_list = st.multiselect(
        "Select Courses",
        df["DERS KODU VE ADI"],
        placeholder="Course Code or Name",
    )
    col1, col2 = st.columns(2)
    if len(course_list) > 0 and col1.button("Show Exam Dates"):
        result_df = en_createResultDf(course_list)
        st.dataframe(result_df, hide_index=True)
        createImage(result_df)
        with open("output/examgenius.png", "rb") as file:
            col2.download_button(
                "Download as Image",
                data=file,
                file_name="examgenius.png",
                mime="image/png",
            )
    st.caption(f"Last Update {last_update}")
    st.caption("For feedback: [mustafa@eftekin.dev](mailto:mustafa@eftekin.dev) 💌")

else:
    st.write("### 2024 Bahar Dönemi Final Sınav Tarihleri")
    st.write("Aşağıda 2024 Bahar dönemi için final sınav tarihleri yer almaktadır.")
    st.write("Lütfen sınav tarihlerini görmek istediğiniz ders kodlarını seçin.")
    course_list = st.multiselect(
        "Dersleri Seçin",
        df["DERS KODU VE ADI"],
        placeholder="Ders Kodu veya Adı",
    )
    col1, col2 = st.columns(2)
    if len(course_list) > 0 and col1.button("Sınav Tarihlerini Göster"):
        result_df = tr_createResultDf(course_list)
        st.dataframe(result_df, hide_index=True)
        createImage(result_df)
        with open("output/examgenius.png", "rb") as file:
            col2.download_button(
                "Resim Olarak İndir",
                data=file,
                file_name="examgenius.png",
                mime="image/png",
            )
    st.caption(f"Son Güncelleme {last_update}")
    st.caption(
        "Geri bildirimleriniz için: [mustafa@eftekin.dev](mailto:mustafa@eftekin.dev) 💌"
    )
