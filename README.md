# Pymage Downloader

Pymage Downloader is a simple and efficient tool for downloading random images from [Lorem Picsum](https://picsum.photos/). It offers both a graphical interface and a command-line interface.

## Features

- Asynchronous image downloading
- User-friendly graphical interface
- Command-line support
- Customizable image dimensions
- Random dimensions option
- Operation logging

## Prerequisites

To install the required dependencies:

    pip install -r requirements.txt

## Usage

### Graphical Interface

Simply run the script without arguments:

    python main.py

### Command Line

    python main.py --sizes "4@800x800,2@1920x1080,3@random"

### Specification Format

Dimensions are specified in the following format:
- `number@widthxheight`: For fixed dimensions
- `number@random`: For random dimensions

Examples:
- `4@800x800`: 4 images of 800x800 pixels
- `2@1920x1080`: 2 images in Full HD
- `3@random`: 3 images with random dimensions

## Project Structure

    pymage-downloader/
    │
    ├── main.py           # Main script
    ├── downloaded_images/ # Downloaded images folder
    └── README.md         # Documentation

## Logging

The program logs all operations to the console with the following information:
- Download directory creation
- Download status
- Potential errors

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## License

This project is licensed under the MIT License.
