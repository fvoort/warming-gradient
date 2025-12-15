import csv
import sys
import math

# Ensure that all arguments are provided 
if len(sys.argv) < 2: 
  print("Error: insufficient arguments. Usage: python3 data_to_files.py <path-to/data.csv> [standard multiples]") 
  sys.exit(1)

# Retrieve the source data file
source_data = sys.argv[1]

# If provided, retrieve standard multiples
if len(sys.argv) >= 3:
    std_multiples = float(sys.argv[2])
    use_fixed_scale = False
else:
    std_multiples = 0.9 # Default for global
    use_fixed_scale = True

# Baseline periods
REFERENCE_PERIOD = ['1961', '2010'] # Period used to define midpoint (where blue changes to red)
STANDARD_DEVIATION_PERIOD = ['1901', '2000'] # Period used to scale color intensity

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

# Function to get data for a period
def get_data_for_period(source, start_year, end_year):
    data = []
    with open(source, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip first row
        for row in reader:
            year = row[0].strip()
            value = row[1].strip()
            if start_year <= year <= end_year and value:
                data.append(float(value))
    return data

# Calculate baseline
baseline_data = get_data_for_period(source_data, REFERENCE_PERIOD[0], REFERENCE_PERIOD[1])
baseline = sum(baseline_data) / len(baseline_data)

# If not using fixed scale, calculate standard deviation
if not use_fixed_scale:
    std_data = get_data_for_period(source_data, STANDARD_DEVIATION_PERIOD[0], STANDARD_DEVIATION_PERIOD[1])
    std_mean = sum(std_data) / len(std_data)
    squared_diffs = [(x - std_mean)**2 for x in std_data]
    std_dev = math.sqrt(sum(squared_diffs) / len(std_data))

# Assign colors for each year
colors = []
with open(source_data, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip first row
    for row in reader:
        year = row[0].strip()
        value = row[1].strip()

        if not value:
            colors.append('#7f7f7f')  # Missing data
            continue

        temp = float(value)
        diff = temp - baseline

        # Determine scale
        if use_fixed_scale:
            scale = std_multiples
        else:
            scale = std_dev * std_multiples

        # Normalize to standard deviations
        normalized = max(-1, min(1, diff / scale))

        # Map normalized value to blue/red color arrays
        if normalized < 0:
            index = int(-normalized * (len(BLUE_COLORS) - 1))
            colors.append(BLUE_COLORS[index])
        else:
            index = int(normalized * (len(RED_COLORS) - 1))
            colors.append(RED_COLORS[index])

def generate_files(colors):
    n = len(colors)
    step = 100 / n  # Width of each stripe

    # Build gradient
    stops = []
    position = 0
    for color in colors:
        next_pos = position + step
        stops.append(f"{color} {position:.2f}%")
        stops.append(f"{color} {next_pos:.2f}%")
        position = next_pos

    gradient = ", ".join(stops)

    # Write to CSS file
    css = generate_css(gradient)
    with open('warming-gradient.css', 'w') as f:
        f.write(css)

    # Write to SVG files
    gradient_svg = generate_svg(gradient)[0]
    with open('warming-gradient.svg', 'w') as f:
        f.write(gradient_svg)

# Generate CSS with linear gradients
def generate_css(gradient):
    gradient_css = f""":root {{
        --warming-gradient: linear-gradient(
            to right, 
            {gradient}
        );
    }}

.warming-gradient {{
    background: var(--warming-gradient);
}}
"""
    return gradient_css

# Generate SVG
def generate_svg(gradient):
    gradient_svg = f"""<svg fill="none" viewBox="0 0 2560 1280" width="2560" height="1280" xmlns="http://www.w3.org/2000/svg">
    <foreignObject width="100%" height="100%">
        <div xmlns="http://www.w3.org/1999/xhtml">
            <style>
                .warming-gradient {{
                    width: 100%;
                    height: 1280px;
                    background: linear-gradient(to right, {gradient});
                }}
            </style>
            <div class="warming-gradient"></div>
        </div>
    </foreignObject>
</svg>
"""
    return [gradient_svg]

# Generate the CSS and SVG files
generate_files(colors)
