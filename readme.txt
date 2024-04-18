--- Shauna's Visualisation ---
To run my visualisation, run the dataFunctions.py file in the Python terminal and then select the fifth button, "Analysis of how specific Artists affect Popularity across Playlists and Charts".

def displayShaunaAnalysis():
    
    #SHAUNA
    # Group by artist(s)_name and count the number of entries in Spotify charts
    df = pd.read_csv('spotify-2023.csv')
    artist_spotify_chart_entries = df.groupby('artist(s)_name')['in_spotify_charts'].sum().sort_values(ascending=False).head(50)

    # Create a horizontal bar plot for the top 50 artist(s) based on the number of entries in Spotify charts
    plt.figure(figsize=(10, 12))
    artist_spotify_chart_entries.plot(kind='barh', color='green')
    plt.title('Top 50 Artist(s) Entries in Spotify Charts')
    plt.xlabel('Number of Entries in Spotify Charts')
    plt.ylabel('Artist(s)')
    plt.tight_layout()
    plt.show()
    # Group by artist(s)_name and count the number of entries in Apple Music charts
    artist_apple_chart_entries = df.groupby('artist(s)_name')['in_apple_charts'].sum().sort_values(ascending=False).head(50)
    # Create a horizontal bar plot for the top 50 artist(s) based on the number of entries in Apple Music charts
    plt.figure(figsize=(10, 12))
    artist_apple_chart_entries.plot(kind='barh', color='Black')
    plt.title('Top 50 Artist(s) Entries in Apple Music Charts')
    plt.xlabel('Number of Entries in Apple Music Charts')
    plt.ylabel('Artist(s)')
    plt.tight_layout()
    plt.show()
    
    # Convert 'in_shazam_charts' column to numeric, replacing non-numeric values with NaN
    df['in_shazam_charts'] = pd.to_numeric(df['in_shazam_charts'], errors='coerce')
    # Group by artist(s)_name and sum the entries in Shazam charts
    artist_shazam_chart_entries = df.groupby('artist(s)_name')['in_shazam_charts'].sum().dropna().sort_values(ascending=False).head(50)
    
    # Create a horizontal bar plot for the top 50 artist(s) based on the number of entries in Shazam charts
    plt.figure(figsize=(10, 12))
    artist_shazam_chart_entries.plot(kind='barh', color='red')  # Change color to Red
    plt.title('Top 50 Artist(s) Entries in Shazam Charts')
    plt.xlabel('Number of Entries in Shazam Charts')
    plt.ylabel('Artist(s)')
    plt.tight_layout()
    plt.show()
