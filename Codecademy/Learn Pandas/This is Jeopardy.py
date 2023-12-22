import pandas as pd

pd.set_option("display.max_colwidth", None)

jeopardy_data = pd.read_csv("./csv/jeopardy.csv")
print(jeopardy_data.columns)

jeopardy_data = jeopardy_data.rename(
    columns={
        " Air Date": "Air Date",
        " Round": "Round",
        " Category": "Category",
        " Value": "Value",
        " Question": "Question",
        " Answer": "Answer",
    }
)
print(jeopardy_data.columns)
print(jeopardy_data.Question)


# Filtering a dataset by a list of words
def filter_data(data, words):
    # Lowercases all words in the list of words as well as the questions. Returns true if all of the words in the list appear in the question.
    filter = lambda x: all(word in x for word in words)
    # Applies the lambda function to the Question column and returns the rows where the function returned True
    return data.loc[data.Question.apply(filter)]


filtered = filter_data(jeopardy_data, ["King", "England"])
print(filtered["Question"])


# A function to find the unique answers of a set of data
def get_answer_counts(data):
    return data["Answer"].value_counts()


print(get_answer_counts(filtered))
