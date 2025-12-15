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

The CSS class and variable will now be available in your project.

## Option 2: Use via CDN

Just paste this `<link>` in the `<head>` of your HTML file and the CSS class and variable will be available in your project:

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

Apply the class or variable directly in your HTML, for example:

```html
<!-- Use with class -->
<div class="warming-gradient" style="height: 100px"></div>

<!-- Use with variable -->
<div style="height: 100px; background: var(--warming-gradient)"></div>
```

## License

[Licensed under MIT license.](LICENSE)
