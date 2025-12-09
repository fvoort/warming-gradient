# Warming Gradient

A Python tool for generating CSS gradients visualizing historical temperature data, inspired by Ed Hawkins' Warming Stripes.

![](warming-gradient.svg)
![](warming-stripes.svg)

## Overview

This tool processes historical temperature data and generates visual representations as "Warming Stripes" to show climate change trends over time. Each stripe represents a year, with colors indicating temperature relative to a baseline period.

## Usage

### Using the CSS

Link the generated [`warming-gradient.css`](warming-gradient.css) file in your HTML and add a class to use it as a `background-color`.

```html
<div class="warming-gradient"></div>
<div class="warming-stripes"></div>
```

### Basic usage

```bash
python3 data_to_files.py <path-to/data.csv>
```

This uses the default global scale (0.9 standard deviations).

### Custom scale

```bash
python3 data_to_files.py <path-to-data.csv> 3.0
```

Specify a custom standard deviation multiple to adjust color intensity.

### Input data format

Your CSV file should have two columns:

-   Column 1: Year (e.g., "2000", "2001", etc.)
-   Column 2: Temperature value (numeric)

Example:

```csv
Year,Temperature
2000,0.32867876
2001,0.47405365
2002,0.53470516
```

### Output files

The script generates three files:

1. `warming-gradient.css` - A CSS file with classes for a smooth gradient and sharp stripes (the original look)
2. `warming-gradient.svg` - Smooth gradient as SVG
3. `warming-stripes.svg` - Sharp stripes

## How It Works

### Color mapping

-   **Blue shades**: Below baseline (cooler temperatures)
-   **Red shades**: Above baseline (warmer temperatures)
-   **Gray**: Missing data

### Reference periods

-   **Baseline (1961-2010)**: Defines the midpoint where blue transitions to red
-   **Standard Deviation (1901-2000)**: Used to scale color intensity (only if a custom scale is provided)

### Scaling modes

-   **Fixed scale**: Uses a constant value (default 0.9) when no argument is provided
-   **Calculated scale**: Multiplies the calculated standard deviation by your specified value

[Read my blog post for more information](https://blog.fvoort.com/3m7kxdme6q22w)

## License

[Code licensed under MIT license.](LICENSE) Licenses for data are included in their directory. Please double-check the license for all data yourself.
