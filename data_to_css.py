import sys

# Ensure that all arguments are provided 
if len(sys.argv) < 4: 
  print("Error: insufficient arguments. Usage: python3 data_to_css.py <path-to/data.csv> <anomaly start year> <anomaly end year>") 
  sys.exit(1)

# Retrieve the source data file and reference period
source_data = sys.argv[1]
source_reference_period = [sys.argv[2], sys.argv[3]]

# Baseline periods
REFERENCE_PERIOD = ['1961', '2010'] # Reference period used to define where blue changes to red
STANDARD_DEVIATION_PERIOD = ['1901', '2000'] # Period used to scale color intensity

# Colors (from coldest to hottest)
COLORS = [
    '#06244C',
    '#08306b',
    '#08519c',
    '#2171b5',
    '#4292c6',
    '#6baed6',
    '#9ecae1',
    '#c6dbef',
    '#deebf7',
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

# Average temperate in 1961-2010 is boundary between blue and red colors
# Color intensity (how blue or how red) depends on how far the temperature is from the 1961-2010 average

# Loop over source anomalies
    # Calculate average

# Loop over destination anomalies
    # Calculate average

# Calculate difference between periods (source_average - destination_average)

# Loop over data
    # Adjust all anomalies by difference
    # Save adjusted anomalies to array