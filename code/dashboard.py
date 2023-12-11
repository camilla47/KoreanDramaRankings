import streamlit as st
import pandas as pd

st.title('All the Drama')
df = pd.read_csv('mdl_final.csv')




##### Show top 5 movies in any selected year #########
years = sorted(df['year'].unique())
# Fetch unique years and sort them in ascending order
selected_year = st.selectbox('Select a year', sorted(df['year'].unique(), reverse=True))
year_df = df[df['year'] == selected_year]

# Sorting and selecting top 5 names for the selected year
top_names = year_df.sort_values(by='viewer_score', ascending=False).head(5)[['title', 'viewer_score']]
top_names.reset_index(drop=True, inplace=True)
top_names = top_names.rename(columns={'title': 'Show Title', 'viewer_score': 'Score (out of 10)'})

# Display the top shows for the selected year
st.write(f"Top Shows in {selected_year}")
st.dataframe(top_names)


