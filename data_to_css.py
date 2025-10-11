import sys

# Ensure that all arguments are provided 
if len(sys.argv) < 4: 
  print("Error: insufficient arguments. Usage: python3 data_to_css.py <path/to/data.csv> <anomaly start year> <anomaly end year>") 
  sys.exit(1)

# Retrieve the data file and source anomaly range from sys.argv
source_data = sys.argv[1]
source_anomalies = [sys.argv[2], sys.argv[3]]

# Convert anomalies to be relative to 1961–2010
DESTINATION_ANOMALIES = ['1961', '2010']

# Loop over source anomalies
    # Calculate average

# Loop over destination anomalies
    # Calculate average

# Calculate difference between periods (source_average - destination_average)

# Loop over data
    # Adjust all anomalies by difference
    # Save adjusted anomalies to array