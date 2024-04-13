import pandas as pd
import csv
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import font

def extractColumn(columnNumber):       
    # code to read the data
    data = pd.read_csv('spotify-2023.csv', encoding = 'latin1')
    with open ('spotify-2023.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader) # this line skips the header

        #now we can read the data from any column using the columnNumber parameter
        columnData = []
        for row in csv_reader:
            data = row[columnNumber]
            columnData.append(data)
        return columnData

def extractRow(rowNumber): # code to extract a particular row from the data
    data = pd.read_csv('spotify-2023.csv', encoding = 'ISO-8859-1')
    rowData = data.loc[rowNumber]
    return rowData

def removeDuplicates(list): # code to remove any duplicates from the list if needed
    newList = []
    for item in list:
        if item not in newList:
            newList.append(item)
    return newList
            
def mapToInteger(userList):
    mappedList = []
    for item in userList:
        try:
            mappedList.append(int(item))
        except ValueError:
            # If the item cannot be converted to an integer, ignore it
            mappedList.append(-1)
    return mappedList

def createLineGraph(title, subtitle, xData, yData, xLabel, yLabel, ): # code to create a basic graph using user data
    fig, ax = plt.subplots()
    fig.suptitle(title)
    ax.set_title(subtitle)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.plot(sorted(xData), sorted(yData))
    plt.show()


def createScatterGraph(title, subtitle, xData, yData, xLabel, yLabel):
    plt.title(title)
    plt.suptitle(subtitle)
    plt.scatter(xData, yData)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()

def createBarChart(title, subtitle, xData, yData, xLabel, yLabel):
    plt.title(title)
    plt.suptitle(subtitle)
    plt.bar(xData,yData)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()

def createDualLineGraph(title, subtitle, xData, yData1, yData2, xLabel, yLabel1, yLabel2):
    fig, ax = plt.subplots()
    plt.title(title)
    plt.suptitle(subtitle)
    ax.plot(sorted(xData), sorted(yData1), 'b', linewidth = '3')
    ax.set_ylabel(yLabel1, color = 'b')
    ax1=ax.twinx()
    ax1.plot(sorted(xData), sorted(yData2), 'r', linewidth = '3')
    ax1.set_ylabel(yLabel2, color = 'r')
    plt.xlabel(xLabel)
    plt.show()
    
def displayGraphs():
    # create 3x3 grid of Axes in one Figure
        fig, axs = plt.subplots(2, 3)
        axs[0][0].set_title("Plot 1")
        axs[0][1].set_title("Plot 2")
        axs[0][2].set_title("Plot 3")  # Fix the index error here
        axs[1][0].set_title("Plot 4")
        axs[1][1].set_title("Plot 5")
        axs[1][2].set_title("Plot 6")
        plt.tight_layout()
        return fig, axs
        #plt.show()

def displayAlexAnalysis():
    xData = mapToInteger(extractColumn(14))  
    yData = mapToInteger(extractColumn(8))
    createLineGraph("Graph of BPM against Streams", "Example", xData, yData, "BPM", "Streams")
    plt.show()

def displayLivAnalysis():
    streamsData = mapToInteger(extractColumn(8))
    spotifyPlaylistData = mapToInteger(extractColumn(6))
    appleMusicPlaylistData = mapToInteger(extractColumn(9))
    #createDualLineGraph("Streams in Spotify and Apple Playlists", "The number of streams in spotify and Apple Playlists", streamsData, spotifyPlaylistData, appleMusicPlaylistData, "Streams", "Spotify Playlist", "Apple Music Playlist")
    fig, axs = plt.subplots(2, 3)
    axs[0][0].set_title("Streams in Spotify and Apple Playlists")
    axs[0][0].plot(streamsData, spotifyPlaylistData)
    axs[0][0].plot(streamsData, appleMusicPlaylistData)
    axs[0][1].set_title("Plot 2")
    axs[1][0].set_title("Plot 3")
    axs[1][1].set_title("Plot 4")
    axs[0][2].set_title("Plot 5")
    axs[1][2].set_title("Plot 6")
    plt.tight_layout()
    plt.show()

def displayJakeAnalysis():
    x
def displayShannonAnalysis():
    x
def displayShaunaAnalysis():
    x
def displayRomaAnalysis():
    x
def displaySushilAnalysis():
    x

#Example of how to use functions
#bpmData = mapToInteger(extractColumn(14))
#streamsData = mapToInteger(extractColumn(8))
#createLineGraph("Graph of BPM against Streams", "Example", bpmData, streamsData, "BPM", "Streams")

#--- CODE YOUR INDIVIDUAL WORK IN THIS SPACE ---

#artistNameData = extractColumn(1)
#spotifyPlaylistData = mapToInteger(extractColumn(6))
#createLineGraph("Artist Name In Spotify Playlists", "Finding the Artists in the Spotify Playlist", artistNameData, spotifyPlaylistData, "Artist Name", "Spotify Playlist")

#artistNameData = extractColumn(1)
#spotifyChartsData = mapToInteger(extractColumn(7))
#createLineGraph("Artist Name in Spotify Charts", "Finding the Artists in the Spotify Charts", artistNameData, spotifyChartsData, "Artist Name", "Spotify Charts")

#artistNameData = extractColumn(1)
#applePlaylistData = mapToInteger(extractColumn(9))
#createLineGraph("Artist Name in Apple Playlist", "Finding the Artists in the Apple Playlist", artistNameData, applePlaylistData, "Artist Name", "Apple Playlist")

#artistNameData = extractColumn(1)
#appleChartsData = mapToInteger(extractColumn(10))
#createLineGraph("Artist Name in Apple Charts", "Finding the Artist in the Apple Charts", artistNameData, appleChartsData, "Artist Name", "Apple Charts")

#artistNameData = extractColumn(1)
#shazamChartsData = mapToInteger(extractColumn(13))
#createLineGraph("Artist Name in Shazam Charts", "Finding the Artist in the Shazam Charts", artistNameData, shazamChartsData, "Artist Name", "Shazam Charts")

#streamsData = mapToInteger(extractColumn(8))
#spotifyPlaylistData = mapToInteger(extractColumn(6))
#appleMusicPlaylistData = mapToInteger(extractColumn(9))
#createDualLineGraph("Streams in Spotify and Apple Playlists", "The number of streams in spotify and Apple Playlists", streamsData, spotifyPlaylistData, appleMusicPlaylistData, "Streams", "Spotify Playlist", "Apple Music Playlist")

#streamsData = mapToInteger(extractColumn(8))
#spotifyPlaylistData = mapToInteger(extractColumn(6))
#shazamChartsData = mapToInteger(extractColumn(13))
#createDualLineGraph("Streams in Spotify Playlists and Shazam Charts", "The number of streams in Spotify Playlists and the Shazam Charts", streamsData, spotifyPlaylistData, shazamChartsData, "Streams", "Spotify Playlist", "Shazam Charts")

#streamsData = mapToInteger(extractColumn(8))
#spotifyChartsData = mapToInteger(extractColumn(7))
#shazamChartsData = mapToInteger(extractColumn(13))
#createDualLineGraph("Streams in Spotify Charts and Shazam Charts", "The number of streams in Spotify Charts and the Shazam Charts", streamsData, spotifyChartsData, shazamChartsData, "Streams", "Spotify Charts", "Shazam Charts")

#streamsData = mapToInteger(extractColumn(8))
#appleMusicChartsData = mapToInteger(extractColumn(10))
#spotifyChartsData = mapToInteger(extractColumn(7))
#createDualLineGraph("Streams in Apple Playlists and the Spotify Charts", "The number of streams in Apple Music Playlists and the Spotify Charts", streamsData, appleMusicChartsData, spotifyChartsData, "Streams", "Apple Music Charts", "Spotify Charts")

#streamsData = mapToInteger(extractColumn(8))
#shazamChartsData = mapToInteger(extractColumn(13))
#appleMusicChartsData = mapToInteger(extractColumn(10))
#createDualLineGraph("Streams in the Shazam Charts and Apple Music Charts", "The number of streams in Shazam Charts and the Apple Music Charts", streamsData, shazamChartsData, appleMusicChartsData, "Streams", "Shazam Charts", "Apple Music Charts")

#streamsData = mapToInteger(extractColumn(8))
#shazamChartsData = mapToInteger(extractColumn(13))
#appleMusicPlaylistData = mapToInteger(extractColumn(9))
#createDualLineGraph("Streams in the Shazam Charts and the Apple Music Playlists", "The number of streams in Shazam Charts and the Apple Music Playlists", streamsData, shazamChartsData, appleMusicPlaylistData, "Streams", "Shazam Charts", "Apple Music Playlist")
    
#keyData = (extractColumn(15))
#streamsData = mapToInteger(extractColumn(8))
# Zip key and stream data together, sort by keys, then unzip
#sorted_data = sorted(zip(keyData, streamsData), key=lambda x: x[0])
#sorted_keys, sorted_streams = zip(*sorted_data)
#createBarChart("Graph of Key's Affect on Streams", "Example", sorted_keys, sorted_streams, "Key", "Streams")


#releaseYearData = mapToInteger(extractColumn(3))
#danceabilityData = mapToInteger(extractColumn(17))
#createLineGraph("Release Year for Danceability", "Finding the trend for the release year and the danceability", releaseYearData, danceabilityData, "Release Year", "Danceability")

#releaseYearData = mapToInteger(extractColumn(3))
#valenceData = mapToInteger(extractColumn(18))
#createLineGraph("Release Year for Valence", "Finding the trend for the release year and the valnce", releaseYearData, valenceData, "Release Year", "Valence")

#releaseYearData = mapToInteger(extractColumn(3))
#energyData = mapToInteger(extractColumn(19))
#createLineGraph("Release Year for Energy", "Finding the trend for the release year and the Energy", releaseYearData, energyData, "Release Year", "Energy")

#releaseMonthData = mapToInteger(extractColumn(4))
#danceabilityData = mapToInteger(extractColumn(17))
#createLineGraph("Release Month for Danceability", "Finding the trend for the release month and the Danceability", releaseMonthData, danceabilityData, "Release Month", "Danceability")

#releaseMonthData = mapToInteger(extractColumn(4))
#valenceData = mapToInteger(extractColumn(18))
#createLineGraph("Release Month for Valence", "Finding the trend for the release month and the Valence", releaseMonthData, valenceData, "Release Month", "Valence")

#releaseMonthData = mapToInteger(extractColumn(4))
#energyData = mapToInteger(extractColumn(19))
#createLineGraph("Release Month for Energy", "Finding the trend for the release month and the Energy", releaseMonthData, energyData, "Release Month", "Energy")

#releaseDayData = mapToInteger(extractColumn(5))
#danceabilityData = mapToInteger(extractColumn(17))
#createLineGraph("Release Day for Danceability", "Finding the trend for the release day and the Danceability", releaseDayData, danceabilityData, "Release Day", "Danceability")

#releaseDayData = mapToInteger(extractColumn(5))
#valenceData = mapToInteger(extractColumn(18))
#createLineGraph("Release Day for Valence", "Finding the trend for the release Day and the Valence", releaseDayData, valenceData, "Release Day", "Valence")

#releaseDayData = mapToInteger(extractColumn(5))
#energyData = mapToInteger(extractColumn(19))
#createLineGraph("Release day for Energy", "Finding the trend for the release day and the Energy", releaseDayData, energyData, "Release Day", "Energy")

# GRAPHICAL USER INTERFACE 
# GUI menu function is below
def button_clicked(option):
    if option in range(1, 8):
        if option == 1: # e.g. this is ALEX'S ANALYSIS
            displayAlexAnalysis()
        if option == 2:
            displayLivAnalysis()
        if option == 3:
            displayJakeAnalysis()
        if option == 4:
            displayShannonAnalysis()
        if option == 5:
            displayShaunaAnalysis()
        if option == 6:
            displayRomaAnalysis()
        if option == 7:
            displaySushilAnalysis()
           # figures.canvas.manager.window.move(960, 540)
            plt.show()
            #streamsData = mapToInteger(extractColumn(8))
            #spotifyPlaylistData = mapToInteger(extractColumn(6))
            #appleMusicPlaylistData = mapToInteger(extractColumn(9))
            #createDualLineGraph("Streams in Spotify and Apple Playlists", "The number of streams in spotify and Apple Playlists", streamsData, spotifyPlaylistData, appleMusicPlaylistData, "Streams", "Spotify Playlist", "Apple Music Playlist")

            #streamsData = mapToInteger(extractColumn(8))
            #spotifyPlaylistData = mapToInteger(extractColumn(6))
            #shazamChartsData = mapToInteger(extractColumn(13))
            #createDualLineGraph("Streams in Spotify Playlists and Shazam Charts", "The number of streams in Spotify Playlists and the Shazam Charts", streamsData, spotifyPlaylistData, shazamChartsData, "Streams", "Spotify Playlist", "Shazam Charts")

            #streamsData = mapToInteger(extractColumn(8))
            #spotifyChartsData = mapToInteger(extractColumn(7))
            #shazamChartsData = mapToInteger(extractColumn(13))
            #createDualLineGraph("Streams in Spotify Charts and Shazam Charts", "The number of streams in Spotify Charts and the Shazam Charts", streamsData, spotifyChartsData, shazamChartsData, "Streams", "Spotify Charts", "Shazam Charts")

            #streamsData = mapToInteger(extractColumn(8))
            #appleMusicChartsData = mapToInteger(extractColumn(10))
            #spotifyChartsData = mapToInteger(extractColumn(7))
            #createDualLineGraph("Streams in Apple Playlists and the Spotify Charts", "The number of streams in Apple Music Playlists and the Spotify Charts", streamsData, appleMusicChartsData, spotifyChartsData, "Streams", "Apple Music Charts", "Spotify Charts")

            #streamsData = mapToInteger(extractColumn(8))
            #shazamChartsData = mapToInteger(extractColumn(13))
            #appleMusicChartsData = mapToInteger(extractColumn(10))
            #createDualLineGraph("Streams in the Shazam Charts and Apple Music Charts", "The number of streams in Shazam Charts and the Apple Music Charts", streamsData, shazamChartsData, appleMusicChartsData, "Streams", "Shazam Charts", "Apple Music Charts")

            #streamsData = mapToInteger(extractColumn(8))
            #shazamChartsData = mapToInteger(extractColumn(13))
            #appleMusicPlaylistData = mapToInteger(extractColumn(9))
            #createDualLineGraph("Streams in the Shazam Charts and the Apple Music Playlists", "The number of streams in Shazam Charts and the Apple Music Playlists", streamsData, shazamChartsData, appleMusicPlaylistData, "Streams", "Shazam Charts", "Apple Music Playlist")
    

            
    else:
        label.config(text="Invalid option")


# GUI setup
root = tk.Tk()
root.title("Graph Menu")
root.configure(bg="black")

title_font = font.Font(family="Helvetica", size=24, weight="bold")
title_label = tk.Label(root, text="Spotify Data Analysis", fg="green", bg="black", font=title_font)
title_label.pack(pady=10)

subtitle_font = font.Font(family="Helvetica", size=14)
subtitle_label = tk.Label(root, text="Select an option to display a graph", fg="green", bg="black", font=subtitle_font)
subtitle_label.pack(pady=5)

# List of option names
option_names = ["Graph of BPM against Streams", "Liv", "Jake", "Shannon", "Shauna", "Roma", "Sushil"]

# Labels and buttons for options
label_font = font.Font(family="Helvetica", size=12)
for i, option_name in enumerate(option_names, start=1):
    button = tk.Button(root, text=option_name, command=lambda opt=i: button_clicked(opt), bg="grey", font=label_font)
    button.config(fg="green")  # Set button text color to green
    button.pack(pady=5)

# Space for an image
canvas = tk.Canvas(root, width=300, height=200)
canvas.config(bg = 'black')
canvas.pack(pady=10)

# Load and display the image
image_path = "img/Spotify.png" 
image = tk.PhotoImage(file=image_path)
canvas.create_image(0, 0, anchor="nw", image=image)

# Exit button
exit_button_font = font.Font(family="Helvetica", size=12)
exit_button = tk.Button(root, text="Exit", command=root.quit, bg = "grey", font = exit_button_font)
exit_button.config(fg = "green")
exit_button.pack(pady=5)

root.mainloop()
