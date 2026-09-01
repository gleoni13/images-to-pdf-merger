# Images to PDF Merger

A Python utility script that merges PNG and JPG images into a single PDF document. It includes natural numerical sorting to ensure pages are ordered correctly (e.g., page 1, 2, ..., 10 instead of 1, 10, 2).

## Features

- **Natural Numerical Sorting**: Correctly sorts numbered filenames using regex parsing.
- **Format Support**: Handles PNG, JPG, and JPEG files seamlessly.
- **RGB Auto-Conversion**: Converts RGBA images automatically to prevent transparency errors during PDF rendering.

## Prerequisites

- Python 3.7+
- Pillow library

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/images-to-pdf-merger.git](https://github.com/your-username/images-to-pdf-merger.git)
   cd images-to-pdf-merger
   ```

## 💡 Usage Guide

### 1. Images to PDF Merger (`images_to_pdf_merger.py`)
1. Place the `images_to_pdf_merger.py` script in the folder containing your images..
2. Run the script:
   ```python
   python images_to_pdf_merger.py

   ```
3. The generated `merged_document.pdf` will appear in the same directory.
