import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('All the Drama')
df = pd.read_csv('code/mdl_final.csv')

######### PICK YOUR SHOW #######################################################
st.header('What Drama Should I Watch?')
#select a genre
unique_genres = set()
for genres in df['genres']:
    split_genres = genres.split(',')
    for genre in split_genres:
        unique_genres.add(genre)
selected_genre = st.selectbox('What genre are you interested in?', sorted(list(unique_genres)))

# select max episode length
min_episode_length = st.slider('Select minimum number of episodes you want in the series:',
                                       min_value=0, max_value=df['episodes'].max(),
                                       value=16)     #df['episodes'].min())

# input minimum rating (out of 10) (user inputs a float between 0 and 10)
min_score = st.slider('Select the minimum rating (out of 10) you want:', min_value=0.0, max_value=10.0, value=8.0)

# Filtering the dataframe based on user inputs
st.text("These are the top 10 shows that match your input:")
filtered_df = df[
    (df['genres'].str.contains(selected_genre, case=False)) &
    (df['episodes'] >= min_episode_length) &
    (df['viewer_score'] >= min_score)
].head(10)

# Display the filtered results
if not filtered_df.empty:
    display_df = filtered_df[['title','episodes','viewer_score','network']]
    display_df = display_df.rename(columns={'title': 'Show Title', 'episodes': '# of Episodes',
                                            'viewer_score':'Score', 'network':'Streaming Options'})

    st.dataframe(display_df, hide_index=True)
else:
    st.write('No titles found matching the selected criteria.')


##### Show top 5 movies in any selected year ###########################################
st.header('Show the Top 5 Dramas in Any Selected Year')
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


##### average score diff streaming ###########################################

# Create Streamlit app
st.title('How Do Scores Compare Between Genres?')
genre_columns = df.columns[9:40]

# Select two genres using Streamlit sidebar
selected_genres = st.multiselect('Select Two Genres:', sorted(genre_columns))
# Filtering data for selected genres
selected_genres_data = df[df[selected_genres].any(axis=1)]

# Plotting histograms side by side
if len(selected_genres) == 2 and not selected_genres_data.empty:
    st.subheader(f'Score Distribution for {selected_genres[0]} and {selected_genres[1]} Dramas')

    fig, axs = plt.subplots(1, 2, figsize=(12, 6), sharey=True) # set up figure

    min_score = selected_genres_data['viewer_score'].min() #get min
    max_score = selected_genres_data['viewer_score'].max() # get the max score for the x-axis limits

    for i, genre in enumerate(selected_genres):
        scores = selected_genres_data[selected_genres_data[genre] == 1]['viewer_score']
        sns.histplot(scores, bins=20, color='forestgreen', edgecolor='black', ax=axs[i],
                     stat='probability') #do proportion instead of frequency
        axs[i].set_xlabel('Viewer Score')
        axs[i].set_ylabel('Frequency')
        axs[i].set_title(f'{genre} Dramas')
        axs[i].set_xlim(min_score-0.05, max_score+0.05)
    st.pyplot(fig)

elif len(selected_genres) != 2:
    st.warning("Please select exactly two genres.")
else:
    st.warning("No data available for the selected genres.")