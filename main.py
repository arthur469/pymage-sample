import os
import random
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import asyncio
import aiohttp
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_directory():
    """
    Create a directory to save downloaded images if it doesn't already exist.
    """
    if not os.path.exists("downloaded_images"):
        os.makedirs("downloaded_images")
        logging.info("Directory 'downloaded_images' created.")
    else:
        logging.info("Directory 'downloaded_images' already exists.")

async def download_image(session, width, height, image_num):
    """
    Download an image from Picsum asynchronously.

    Args:
        session (aiohttp.ClientSession): The aiohttp session to use for the request.
        width (int): The width of the image.
        height (int): The height of the image.
        image_num (str): The identifier for the image.
    """
    url = f"https://picsum.photos/{width}/{height}?random={image_num}"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                with open(f"downloaded_images/image_{image_num}.jpg", "wb") as f:
                    f.write(await response.read())
                logging.info(f"Image {image_num} downloaded successfully.")
            else:
                logging.error(f"Failed to download image {image_num}. Status code: {response.status}")
    except aiohttp.ClientError as e:
        logging.error(f"Error downloading image {image_num}: {e}")

async def download_images(sizes):
    """
    Download specified number of images with specified dimensions asynchronously.

    Args:
        sizes (list): A list of size specifications in the format 'num_images@widthxheight' or 'num_images@random'.
    """
    try:
        async with aiohttp.ClientSession() as session:
            tasks = []
            for size in sizes:
                num_images, dimensions = size.split('@')
                num_images = int(num_images.strip())
                for i in range(1, num_images + 1):
                    if dimensions.strip().lower() == "random":
                        width = random.randint(1, 3840)
                        height = random.randint(1, 2160)
                    else:
                        width, height = map(int, dimensions.strip().split('x'))

                    tasks.append(download_image(session, width, height, f"{width}x{height}_{i}"))

            await asyncio.gather(*tasks)
        logging.info("Images downloaded successfully!")
    except ValueError:
        logging.error("Please enter valid numbers for images and dimensions.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def run_gui():
    """
    Run the GUI for the Pymage Downloader application.
    """
    # Create the main window
    root = tk.Tk()
    root.title("Pymage Downloader")

    # Instructions label
    label_instructions = tk.Label(root, text="Enter the number of images and desired dimensions (e.g., 4@800x800, 10@1080x1920, or random):")
    label_instructions.pack(pady=10)

    # Sizes input
    label_sizes = tk.Label(root, text="Sizes (e.g., 4@800x800, 10@1080x1920, or random):")
    label_sizes.pack()
    entry_sizes = tk.Entry(root)
    entry_sizes.pack()

    # Download button
    button_download = tk.Button(root, text="Download Images", command=lambda: asyncio.run(download_images(entry_sizes.get().split(','))))
    button_download.pack(pady=20)

    # Create download directory and run GUI
    create_directory()
    root.mainloop()

def main():
    """
    Main function to parse command-line arguments and run the appropriate functionality.
    """
    parser = argparse.ArgumentParser(description="Download images from Picsum")
    parser.add_argument('--sizes', type=str, help="Sizes (e.g., 4@800x800, 10@1080x1920, or random)")
    args = parser.parse_args()

    if args.sizes:
        create_directory()
        asyncio.run(download_images(args.sizes.split(',')))
    else:
        run_gui()

if __name__ == "__main__":
    main()
