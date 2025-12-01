def top_5_chart_songs(input_file):
    # Read all lines manually
    with open(input_file, "r", encoding="latin-1") as f:
        lines = f.readlines()

    # Split header
    header = lines[0].strip().split(",")

    # Find column indexes
    track_index = header.index("track_name")
    spotify_index = header.index("in_spotify_charts")
    apple_index = header.index("in_apple_charts")
    deezer_index = header.index("in_deezer_charts")
    shazam_index = header.index("in_shazam_charts")

    # Lists to store (track_name, chart_value)
    spotify_list = []
    apple_list = []
    deezer_list = []
    shazam_list = []

    # Process every row
    for line in lines[1:]:
        row = line.strip().split(",")

        # Skip broken rows
        if len(row) <= shazam_index:
            continue

        track = row[track_index].strip()

        # Convert chart numbers to integers (empty = 0)
        def to_num(val):
            return int(val) if val.isdigit() else 0

        spotify_list.append((track, to_num(row[spotify_index])))
        apple_list.append((track, to_num(row[apple_index])))
        deezer_list.append((track, to_num(row[deezer_index])))
        shazam_list.append((track, to_num(row[shazam_index])))

    # Sort each list (bubble sort for beginners, NO imports)
    def bubble_sort_desc(lst):
        lst = lst[:]  # copy the list
        n = len(lst)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lst[j][1] < lst[j + 1][1]:  # compare values
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst

    # Sort all lists descending
    spotify_sorted = bubble_sort_desc(spotify_list)
    apple_sorted = bubble_sort_desc(apple_list)
    deezer_sorted = bubble_sort_desc(deezer_list)
    shazam_sorted = bubble_sort_desc(shazam_list)

    # Create dictionary of top 5 for each
    top_5 = {
        "spotify": spotify_sorted[:5],
        "apple": apple_sorted[:5],
        "deezer": deezer_sorted[:5],
        "shazam": shazam_sorted[:5]
    }

    return top_5


# ---- RUN THE FUNCTION ----
result = top_5_chart_songs(
    r"C:\Users\khush\Downloads\spotify-2023.csv"
)

print(result)
