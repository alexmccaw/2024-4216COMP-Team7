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

def createDualLineGraphOnSubplot(ax, title, xData, yData1, yData2, xLabel, yLabel1, yLabel2):
    ax.set_title(title)
    ax.plot(sorted(xData), sorted(yData1), 'b', linewidth = '1')
    ax.set_ylabel(yLabel1, color = 'b')
    ax1=ax.twinx()
    ax1.plot(sorted(xData), sorted(yData2), 'r', linewidth = '1')
    ax1.set_ylabel(yLabel2, color = 'r')
    ax.set_xlabel(xLabel)

def createLineGraphOnSubplot(ax, title, xData, yData, xLabel, yLabel):
    ax.set_title(title)
    ax.plot(sorted(xData), sorted(yData), 'b', linewidth = '2')
    ax.set_ylabel(yLabel, color = 'b')
    ax.set_xlabel(xLabel)

#Example of how to use functions
#bpmData = mapToInteger(extractColumn(14))
#streamsData = mapToInteger(extractColumn(8))
#createLineGraph("Graph of BPM against Streams", "Example", bpmData, streamsData, "BPM", "Streams")
    
def displayAlexAnalysis():
    #Data processing using functions
    bpmData = mapToInteger(extractColumn(14))
    streamsData = mapToInteger(extractColumn(8))
    spotifyChartsData = mapToInteger(extractColumn(7))
    appleMusicChartsData = mapToInteger(extractColumn(10))
    
    
    #Plotting of figure with multiple axes, in this case, 3x1 so 3 graphs can be shown
    fig, axs = plt.subplots(1, 2)

    #Plotting individual graphs: 
    createLineGraphOnSubplot(axs[0], "Graph of BPM against Streams", bpmData, streamsData, "BPM", "Streams")
    createDualLineGraphOnSubplot(axs[1], "Graph of BPM against Chart Data", bpmData, spotifyChartsData,
                                 appleMusicChartsData, "BPM", "In Spotify Charts", "In Apple Music Charts")
    #createLineGraphOnSubplot(axs[2], "Graph of BPM against Streams", bpmData, streamsData, "BPM", "Streams")
    plt.tight_layout()
    plt.show()

def displayLivAnalysis():
    #Data processing using functions
    streamsData = mapToInteger(extractColumn(8))
    spotifyPlaylistData = mapToInteger(extractColumn(6))
    appleMusicPlaylistData = mapToInteger(extractColumn(9))
    shazamChartsData = mapToInteger(extractColumn(13))
    spotifyChartsData = mapToInteger(extractColumn(7))
    appleMusicChartsData = mapToInteger(extractColumn(10))

    #Plotting of figure with multiple axes, in this case, 2x3 so 6 graphs can be shown
    fig, axs = plt.subplots(2, 3)

    #Plotting individual graphs: 

    createDualLineGraphOnSubplot(axs[0][0], "Streams in Spotify and Apple Playlists", streamsData, 
                                 spotifyPlaylistData, appleMusicPlaylistData,
                                 "Streams", "Spotify", "Apple")

    createDualLineGraphOnSubplot(axs[0][1],"Streams in Spotify Playlists and Shazam Charts", streamsData, 
                                 spotifyPlaylistData, shazamChartsData, "Streams", "Spotify Playlist", 
                                 "Shazam Charts")

    createDualLineGraphOnSubplot(axs[0][2], "Streams in Spotify Charts and Shazam Charts",  
                                 streamsData, spotifyChartsData, shazamChartsData, "Streams", "Spotify Charts", "Shazam Charts")

    createDualLineGraphOnSubplot(axs[1][0],"Streams in Apple Playlists and the Spotify Charts", streamsData,
                          appleMusicChartsData, spotifyChartsData, "Streams", "Apple Music Charts", "Spotify Charts")

    createDualLineGraphOnSubplot(axs[1][1], "Streams in the Shazam Charts and Apple Music Charts", 
                                 streamsData, shazamChartsData, appleMusicChartsData, "Streams", "Shazam Charts", "Apple Music Charts")

    createDualLineGraphOnSubplot(axs[1][2], "Streams in the Shazam Charts and the Apple Music Playlists", 
                                 streamsData, shazamChartsData, appleMusicPlaylistData, "Streams", "Shazam Charts", "Apple Music Playlist")

    plt.tight_layout()
    plt.show()

def displayJakeAnalysis():
    # Extracting data for artist count and streams
    artistCountData = extractColumn(2)
    streamsData = mapToInteger(extractColumn(8))

    # Creating a bar chart
    createBarChart("Artists Count's Affect on Streams", "Example", artistCountData,
                   streamsData, "Artist Count", "Streams(million)")

def displayShannonAnalysis():
    releaseYearData = mapToInteger(extractColumn(3))
    releaseMonthData = mapToInteger(extractColumn(4))
    releaseDayData = mapToInteger(extractColumn(5))
    danceabilityData = mapToInteger(extractColumn(17))
    valenceData = mapToInteger(extractColumn(18))
    energyData = mapToInteger(extractColumn(19))

    #Plotting of figure with multiple axes, in this case, a 3x3 figure so 9 graphs can be shown
    fig, axs = plt.subplots(3, 3)

    #Plotting individual graphs: 

    createLineGraphOnSubplot(axs[0][0], "Release Year for Danceability", releaseYearData, danceabilityData, "Release Year", "Danceability")
    createLineGraphOnSubplot(axs[1][0], "Release Month for Danceability", releaseMonthData, danceabilityData, "Release Year", "Danceability")
    createLineGraphOnSubplot(axs[2][0], "Release Day for Danceability", releaseDayData, danceabilityData, "Release Year", "Danceability")
    createLineGraphOnSubplot(axs[0][1], "Release Year for Valence", releaseYearData, valenceData, "Release Year", "Valence")
    createLineGraphOnSubplot(axs[1][1], "Release Month for Valence", releaseMonthData, valenceData, "Release Year", "Valence")
    createLineGraphOnSubplot(axs[2][1], "Release Day for Valence", releaseDayData, valenceData, "Release Year", "Valence")
    createLineGraphOnSubplot(axs[0][2], "Release Year for Energy", releaseYearData, energyData, "Release Year", "Energy")
    createLineGraphOnSubplot(axs[1][2], "Release Month for Energy", releaseMonthData, energyData, "Release Year", "Energy")
    createLineGraphOnSubplot(axs[2][2], "Release Day for Energy", releaseDayData, energyData, "Release Year", "Energy")

    plt.tight_layout()
    plt.show()

def displayShaunaAnalysis():
    artistNameData = extractColumn(1)
    spotifyPlaylistData = mapToInteger(extractColumn(6))
    spotifyChartsData = mapToInteger(extractColumn(7))
    applePlaylistData = mapToInteger(extractColumn(9))
    appleChartsData = mapToInteger(extractColumn(10))
    shazamChartsData = mapToInteger(extractColumn(13))

    #Plotting of figure with multiple axes, in this case, 1x5 so 5 graphs can be shown
    fig, axs = plt.subplots(1,5)

    #Plotting individual graphs: 

    createLineGraphOnSubplot(axs[0],"Artist Name In Spotify Playlists", artistNameData, spotifyPlaylistData, "Artist Name", "Spotify Playlist")
    createLineGraphOnSubplot(axs[1], "Artist Name in Spotify Charts", artistNameData, spotifyChartsData, "Artist Name", "Spotify Charts")
    createLineGraphOnSubplot(axs[2], "Artist Name in Apple Playlist", artistNameData, applePlaylistData, "Artist Name", "Apple Playlist")
    createLineGraphOnSubplot(axs[3], "Artist Name in Apple Charts", artistNameData, appleChartsData, "Artist Name", "Apple Charts")
    createLineGraphOnSubplot(axs[4], "Artist Name in Shazam Charts", artistNameData, shazamChartsData, "Artist Name", "Shazam Charts")
    plt.tight_layout()
    plt.show()

def displayRomaAnalysis():
    keyData = (extractColumn(15))
    streamsData = mapToInteger(extractColumn(8))

    createBarChart("Graph of Key's Effect on Streams", "How does Key affect popularity of a song?",
                   keyData, sorted(streamsData), "Key", "Streams")

def displaySushilAnalysis():
    
    # Extracting data for keys and streams
    artistData = mapToInteger(extractColumn(17))
    streamsData = mapToInteger(extractColumn(8))

    # Creating a bar chart
    createBarChart("Danceability Affect on Streams", "Example", artistData, streamsData, "Danceability(%)", "Streams(million)")

     # Extracting data for keys and streams
    valenceData = mapToInteger(extractColumn(18))
    streamsData = mapToInteger(extractColumn(8))

    # Creating a bar chart
    createBarChart("Valence Affect on Streams", "Example", valenceData, streamsData, "valence(%)", "Streams(million)") # Extracting data for keys and streams
    energyData = mapToInteger(extractColumn(19))
    streamsData = mapToInteger(extractColumn(8))

    # Creating a bar chart
    createBarChart("Energy Affect on Streams", "Example", energyData, streamsData, "Energy(%)", "Streams(million)")

#--- CODE YOUR INDIVIDUAL WORK IN THIS SPACE ---

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

# GUI setup
root = tk.Tk()
root.title("Graph Menu")
root.configure(bg="green")

title_font = font.Font(family="Helvetica", size=24, weight="bold")
title_label = tk.Label(root, text="Spotify Data Analysis", fg="black", bg="green", font=title_font)
title_label.pack(pady=10)

subtitle_font = font.Font(family="Helvetica", size=14)
subtitle_label = tk.Label(root, text="Select an option to display analysis: ", fg="black", bg="green", font=subtitle_font)
subtitle_label.pack(pady=5)


# List of option names
option_names = ["Analysis of BPM against and Chart Data", "Analysis of Streams across different Charts", 
                "Analysis of Artist Count's affect on Streams", "Analysis of how Release Dates affect Streams",
                "Analysis of how specific Artists affect popularity across Playlists and Charts",
                "Analysis of how the Key affects how streamed songs are", 
                "Analysis of how Danceability, Valence and Energy affect total streams"]

# Labels and buttons for options
label_font = font.Font(family="Helvetica", size=12)
for i, option_name in enumerate(option_names, start=1):
    button = tk.Button(root, text=option_name, command=lambda opt=i: button_clicked(opt),
                       bg="grey", font=label_font, width = '70', height = '2')
    button.config(fg="black")  # Set button text color to green
    button.pack(pady=5)

# Exit button
exit_button_font = font.Font(family="Helvetica", size=12)
exit_button = tk.Button(root, text="Exit Program"
                        , command=root.quit, bg = "grey", font = exit_button_font, width = '20')
exit_button.config(fg = "green")
exit_button.pack(pady=5)

root.attributes('-fullscreen', True)
root.mainloop()
