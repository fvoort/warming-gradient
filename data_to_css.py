import csv
import sys

# Ensure that all arguments are provided 
if len(sys.argv) < 5: 
  print("Error: insufficient arguments. Usage: python3 data_to_css.py <path-to/data.csv> <anomaly start year> <anomaly end year> <standard deviation>") 
  sys.exit(1)

# Retrieve the source data file and reference period
source_data = sys.argv[1]
source_reference_period = [sys.argv[2], sys.argv[3]]
deviation = float(sys.argv[4])

# Baseline periods
REFERENCE_PERIOD = ['1961', '2010'] # Period used to define midpoint (where blue changes to red)
STANDARD_DEVIATION_PERIOD = ['1901', '2000'] # Period used to scale color intensity

# Function to find average anomaly for period
def calculate_average(source, period):
    values = []
    found_start = False

    # Loop over anomalies
    with open(source, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # Skip first row
        for row in reader:
            year = row[0].strip()
            if year == period[0]:
                found_start = True  # Start collecting
            if found_start:
                values.append(float(row[1]))
            if year == period[1]:
                break  # Stop after reaching the end year

    return sum(values) / len(values)

# Function to find midpoint, returns a value
def find_midpoint(source, start, avg):
    midpoint = ''
    found_start = False

    # Loop over data
    with open(source, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # Skip first row
        for row in reader:
            year = row[0].strip()
            data = float(row[1].strip())
            if year == start:
                found_start = True
            if found_start and data >= avg:
                midpoint = data
                break # Stop after finding the midpoint

    return midpoint

# Function to find range
def find_range(source, period):
    min_value = float('inf')
    max_value = float('-inf')
    found_start = False
    
    with open(source, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip first row
        for row in reader:
            year = row[0].strip()
            data = float(row[1].strip())
            if year == period[0]:
                found_start = True
            if found_start:
                min_value = min(min_value, data)
                max_value = max(max_value, data)
            if year == period[1]:
                break  # Stop after reaching the end year
                
    return max_value - min_value

# Function to generate an array of colors based on temperature
def generate_colors(source, midpoint, range, blue_colors, red_colors):
    colors = []

    # Loop over data
    with open(source, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # Skip first row
        line_count = sum(1 for _ in csvfile)
        line_deviation = deviation / (line_count / 2)

        csvfile.seek(0) # Return to first line of file
        next(reader) # Skip first row

        for row in reader:
            data = float(row[1].strip())

            distance_from_average = abs(data - average)

            steps = int(distance_from_average / line_deviation)

            if data < midpoint:
                color_index = min(steps, len(blue_colors) - 1)
                colors.append(blue_colors[-(color_index + 1)])
            else:
                color_index = min(steps, len(red_colors) - 1)
                colors.append(red_colors[(color_index)])
    
    return colors

# Function to generate a CSS file with linear gradients using the given colors
def generate_css(colors):
    n = len(colors) # Amount of colors
    step = 100 / n # Calculate width of each stripe

    # Build warming-stripes gradient
    position = 0 #
    stops = []
    for i in range(n):
        color = colors[i]
        next_pos = position + step
        stops.append(f"{color} {position:.2f}%")
        stops.append(f"{color} {next_pos:.2f}%")
        position = next_pos

    # Join all colors into a comma-separated string for CSS
    warming_gradient = ", ".join(colors)
    warming_stripes = ", ".join(stops)

    # Create CSS gradients
    gradient = f"""
.warming-gradient {{
    background: linear-gradient(to right, {warming_gradient});
}}

.warming-stripes {{
    background: linear-gradient(to right,  {warming_stripes})
}}
"""

    # Write to a CSS file
    with open('warming-gradient.css', "w") as f:
        f.write(gradient)

# Calculate period averages
source_avg = calculate_average(source_data, source_reference_period)
reference_avg = calculate_average(source_data, REFERENCE_PERIOD)
deviation_avg = calculate_average(source_data, STANDARD_DEVIATION_PERIOD)


# Example data
numbers = [2, 4, 6, 8, 50]

# Step 1: Calculate the mean
mean = sum(numbers) / len(numbers)
print("Mean:", mean)

# Step 2: Calculate differences from the mean
differences = [x - mean for x in numbers]
print("Differences from mean:", differences)

# Step 3: Square each difference
squared_differences = [d**2 for d in differences]
print("Squared differences:", squared_differences)

# Step 4: Calculate the average of the squared differences (variance)
variance = sum(squared_differences) / len(numbers)
print("Variance:", variance)


# Colors (from light to dark)
BLUE_COLORS = [
    '#deebf7',
    '#c6dbef',
    '#9ecae1',
    '#6baed6',
    '#4292c6',
    '#2171b5',
    '#08519c',
    '#08306b',
    '#06244C'
]

RED_COLORS = [
    '#fee0d2', 
    '#fcbba1', 
    '#fc9272',
    '#fb6a4a',
    '#ef3b2c', 
    '#cb181d', 
    '#a50f15', 
    '#67000d', 
    '#440007'
]

midpoint = find_midpoint(source_data, REFERENCE_PERIOD[0], reference_avg)
range = find_range(source_data, STANDARD_DEVIATION_PERIOD)
colors = generate_colors(source_data, midpoint, deviation_avg, BLUE_COLORS, RED_COLORS)

generate_css(colors)