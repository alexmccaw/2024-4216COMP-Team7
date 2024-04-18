--- Shannon's Visualisation ---
To run my visualisation, run the dataFunctions.py file in the Python terminal and then select the fourth button, "Analysis of how Release Dates affect Streams".

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
    createLineGraphOnSubplot(axs[1][0], "Release Month for Danceability", releaseMonthData, danceabilityData, "Release Month", "Danceability")
    createLineGraphOnSubplot(axs[2][0], "Release Day for Danceability", releaseDayData, danceabilityData, "Release Day", "Danceability")
    createLineGraphOnSubplot(axs[0][1], "Release Year for Valence", releaseYearData, valenceData, "Release Year", "Valence")
    createLineGraphOnSubplot(axs[1][1], "Release Month for Valence", releaseMonthData, valenceData, "Release Month", "Valence")
    createLineGraphOnSubplot(axs[2][1], "Release Day for Valence", releaseDayData, valenceData, "Release Day", "Valence")
    createLineGraphOnSubplot(axs[0][2], "Release Year for Energy", releaseYearData, energyData, "Release Year", "Energy")
    createLineGraphOnSubplot(axs[1][2], "Release Month for Energy", releaseMonthData, energyData, "Release Month", "Energy")
    createLineGraphOnSubplot(axs[2][2], "Release Day for Energy", releaseDayData, energyData, "Release Day", "Energy")

    plt.tight_layout()
    plt.show()


