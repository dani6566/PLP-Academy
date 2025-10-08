import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def load_data():
    df = pd.read_csv('./Data/metadata.csv')
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].fillna('').apply(lambda x: len(x.split()))
    return df

df = load_data()



st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata")

# Year filter
year_range = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
filtered_df = df[df['year'].between(year_range[0], year_range[1])]

# Show sample data
st.subheader("Sample Data")
st.dataframe(filtered_df.head())

# Publications by year
st.subheader("Publications by Year")
df_filtered = df[(df['year'] >= 2000) & (df['year'] <= 2020)]
year_counts = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
st.pyplot(fig)


