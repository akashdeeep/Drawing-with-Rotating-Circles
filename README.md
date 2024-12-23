# Fourier Graphics Renderer

This project visualizes 2D graphics using Fourier transforms. It animates a series of rotating vectors (arrows) that combine to draw a specified shape or pattern. The input for the shapes is derived from an SVG file, and the output showcases the beauty of Fourier-based rendering.

---

## Features

- **Fourier Transformation:** Decomposes 2D points into Fourier coefficients and uses them to animate graphics.
- **Dynamic Visualization:** Displays rotating vectors and the resulting composite figure in real-time.
- **SVG Path Input:** Supports importing 2D shapes from SVG files for Fourier decomposition.
- **Interactive Animation:** Visualizes the reconstruction of the shape step-by-step using Fourier components.
- **Customizable Settings:** Configure the number of coefficients, canvas size, and frame rate.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Configuration](#configuration)
4. [Project Structure](#project-structure)
5. [Dependencies](#dependencies)
6. [Future Improvements](#future-improvements)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fourier-graphics-renderer.git
   cd fourier-graphics-renderer
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have a valid SVG file for input (example: `input.svg`).

---

## Usage

1. Place your SVG file in the project directory.

2. Run the script:

   ```bash
   python main.py
   ```

3. Watch the Fourier-based rendering animation in a `pygame` window.

4. Modify settings in `conf` for custom behavior (e.g., number of coefficients, SVG file path).

---

## Configuration

The project can be customized using the `conf` dictionary in `main.py`. Key options include:

- **SVG Path:**

  ```python
  conf['svg_path'] = "input.svg"
  ```

- **Number of Fourier Coefficients:**

  ```python
  conf['n_coefficients'] = 100
  ```

- **Animation Settings:**
  ```python
  conf['fps'] = 60
  conf['canvas_size'] = (800, 800)
  ```

---

## Project Structure

```
.
├── main.py                # Entry point for the application
├── fourier.py             # Fourier computation and related utilities
├── svg_handler.py         # Functions for parsing and sampling SVG paths
├── renderer.py            # Visualization and animation logic using pygame
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
└── input.svg              # Example SVG file
```

---

## Dependencies

This project requires Python 3.7+ and the following libraries:

- `pygame`: For rendering and animation.
- `numpy`: For numerical computations.
- `svg.path`: For parsing SVG files.

Install them using:

```bash
pip install pygame numpy svg.path
```

---

## Future Improvements

- **Adaptive Sampling:** Automatically adjust the sampling density based on SVG path complexity.
- **Performance Optimization:** Cache Fourier coefficients and enable multi-threaded rendering.
- **GUI Integration:** Add a user interface for loading SVG files and adjusting settings dynamically.
- **3D Visualization:** Extend functionality to support 3D shapes and animations.

---

Enjoy creating beautiful graphics with Fourier transforms!
