# Warming Gradient

CSS gradient visualizing historical temperature data, inspired by [Ed Hawkins' Warming Stripes](https://showyourstripes.info).

![](/warming-gradient.svg)

## Installation

You can use NPM (best for projects with a build process), a CDN (quick copy-paste into any HTML file), or download and include the CSS file yourself.

## Option 1: Install with NPM

Make sure you have **Node.js** installed and run this command in your project folder:

```bash
npm install warming-gradient
```

### Import in CSS

Add this at the top of your main CSS file:

```css
@import 'node_modules/warming-gradient/warming-gradient.css';
```

Or just paste this `<link>` in the `<head>` of your HTML file:

```html
<link rel="stylesheet" href="node_modules/warming-gradient/warming-gradient.css" />
```

The CSS classes will now be available in your project.

## Option 2: Use via CDN

Just paste this `<link>` in the `<head>` of your HTML file and the CSS classes will be available in your project:

```html
<link rel="stylesheet" href="https://unpkg.com/warming-gradient" />
```

## Option 3: Self-host warming-gradient.css

1. Download the `warming-gradient.css` file from [the source files here](https://github.com/fvoort/warming-gradient).
2. Place it in your project folder.
3. Include it in your HTML:

```html
<link rel="stylesheet" href="path/to/warming-gradient.css" />
```

## How to use

Apply the classes directly in your HTML, for example:

```html
<div class="warming-gradient" style="height: 100px;"></div>
```

## Contributing

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

Additional columns in the CSV will be ignored. The script assumes the first row contains headers and automatically skips it.

Example:

```csv
Year,Temperature
2000,0.32867876
2001,0.47405365
2002,0.53470516
```

### Output files

The script generates three files:

1. `warming-gradient.css` - A CSS file with class for Warming Gradient
2. `warming-gradient.svg` - Warming Gradient as SVG

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

