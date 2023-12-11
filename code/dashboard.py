import streamlit as st
import pandas as pd

st.title('All the Drama')
df = pd.read_csv('code/mdl_final.csv')

st.header('What Drama Should I Watch?')
#select a genre
unique_genres = set()
for genres in df['genres']:
    split_genres = genres.split(',')
    for genre in split_genres:
        unique_genres.add(genre)
selected_genre = st.selectbox('Select a genre', sorted(list(unique_genres)))

# select max episode length
max_episode_length = st.slider('Select maximum episode length',
                                       min_value=0, max_value=df['episodes'].max(),
                                       value=df['episodes'].max())

# input minimum rating (out of 10) (user inputs a float between 0 and 10)
min_score = st.slider('Input minimum rating (out of 10)', min_value=0.0, max_value=10.0, value=0.0)

# Filtering the dataframe based on user inputs
## select all rows where the selected genre contains a 1
filtered_df = df[(df['genres'] == selected_genre) & (df['episodes'] <= max_episode_length) & (df['viewer_score'] >= min_score)]

# Display the filtered results
if not filtered_df.empty:
    st.write(filtered_df[['title','network']])
else:
    st.write('No titles found matching the selected criteria.')


##### Show top 5 movies in any selected year #########
st.header('Show Top 5 Dramas in Any Selected Year')
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


