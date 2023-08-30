def _get_distances():
    with open("data/distances.csv", "r") as f:
        data = f.readlines()

    # Skip the header (first row)
    data = data[1:]

    # Split lines by comma and strip newline characters
    distances = [line.strip().split(",") for line in data]

    # Convert string values to appropriate type (assuming float here, adjust as needed)
    for i in range(len(distances)):
        for j in range(len(distances[i])):
            try:
                distances[i][j] = float(distances[i][j])
            except ValueError:
                pass  # Keeps non-numeric values as strings

    return distances
