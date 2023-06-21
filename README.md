# YouTube Video Metadata

This script allows you to retrieve metadata for YouTube videos by providing a valid YouTube video link. It uses the `tkinter` library to create a simple graphical user interface (GUI) where you can enter the YouTube link and click a button to fetch the video metadata.

## Prerequisites

Make sure you have the following libraries installed before running the script:

- `tkinter`: This library is usually included with Python installations.
- `requests_html`: Install it using `pip install requests-html`.
- `BeautifulSoup`: Install it using `pip install beautifulsoup4`.

## Usage

1. Run the script using a Python interpreter.
2. A window titled "YouTube Video Metadata" will open.
3. Enter a valid YouTube video link in the provided input field.
   - The link should start with "https://www.youtube.com/watch?v=" followed by the video ID.
4. Click the "Get Metadata" button to fetch the video metadata.
   - If the link is valid, a messagebox will display the metadata information, including the video title, description, and tags.
   - If there is an error, an error messagebox will be shown with the corresponding error message.

Note: The GUI window is centered on the screen for better visibility.

## Example

Here's an example of how to use the script:

1. Run the script.
2. Enter the YouTube video link in the input field: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`.
3. Click the "Get Metadata" button.
4. A messagebox will appear with the video metadata.
