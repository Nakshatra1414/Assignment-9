
Purpose of the Program

The purpose of this program is to analyze chart performance data from the Spotify 2023 dataset and identify the top 5 most-charted songs across four major music platforms:

Spotify Charts

Apple Charts

Deezer Charts

Shazam Charts

The program is designed to allow practice using core Python data structures such as lists, dictionaries, and tuples, while avoiding all import statements. Students manually process the CSV file and implement their own sorting logic, reinforcing understanding of loops, data parsing, and sorting algorithms.


What the Program Does
Input

The program takes one input:

A CSV file containing the Spotify 2023 dataset
Example:

C:\Users\khush\Downloads\spotify-2023.csv


This dataset includes columns such as:

track_name

in_spotify_charts

in_apple_charts

in_deezer_charts

in_shazam_charts

Processing

The program performs the following actions:

Reads the CSV file manually using basic file operations.
(No CSV imports are used.)

Splits lines using .split(",").

Identifies important columns by name.

Builds lists of tuples for each platform, where each tuple contains:

(track_name, chart_value)


Converts empty or missing numbers to 0.

Sorts each list using a beginner-friendly bubble sort implemented manually.

Extracts the top 5 highest-charting songs for each platform.

Stores the final results in a dictionary.

Output

The program returns a dictionary containing four keys:

{
  "spotify": [...top 5 songs...],
  "apple": [...top 5 songs...],
  "deezer": [...top 5 songs...],
  "shazam": [...top 5 songs...]
}


Each list contains 5 tuples, where each tuple holds:

(song_name, chart_number)


Example output:

{
  'spotify': [('Blinding Lights', 102), ('Anti-Hero', 95), ...],
  'apple': [('Calm Down', 88), ...],
  'deezer': [('Heat Waves', 50), ...],
  'shazam': [('Another Love', 120), ...]
}

How to Use the Program

Download the spotify-2023.csv file and place it in your computer’s Downloads folder.

Update the file path in the function call:

result = top_5_chart_songs(
    r"C:\Users\khush\Downloads\spotify-2023.csv"
)


Run the Python script.

After execution, the dictionary containing the top 5 songs for each chart category is printed to the console.

You may further process, print, or save this dictionary based on assignment requirements.