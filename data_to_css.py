import csv
import sys

# Ensure that all arguments are provided 
if len(sys.argv) < 4: 
  print("Error: insufficient arguments. Usage: python3 data_to_css.py <path-to/data.csv> <anomaly start year> <anomaly end year>") 
  sys.exit(1)

# Retrieve the source data file and reference period
source_data = sys.argv[1]
source_reference_period = [sys.argv[2], sys.argv[3]]

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
        for row in reader:
            year = row[0].strip()
            if year == period[0]:
                found_start = True  # start collecting
            if found_start:
                values.append(float(row[1]))
            if year == period[1]:
                break  # stop after reaching the end year

    return sum(values) / len(values)

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

# Calculate difference between source and reference period averages
source_avg = calculate_average(source_data, source_reference_period)
reference_avg = calculate_average(source_data, REFERENCE_PERIOD)
deviation_diff = source_avg - reference_avg

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

generate_css(RED_COLORS) # DELETE LATER: Testing function with all colors

# Average temperate in 1961-2010 is boundary between blue and red colors
# Color intensity (how blue or how red) depends on how far the temperature is from the 1901-2000 average

# Loop over data
    # Adjust all anomalies by difference
    # Save adjusted anomalies to array