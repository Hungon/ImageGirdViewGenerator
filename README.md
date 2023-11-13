# Image Grid Generator

This script generates an HTML code for an image grid view based on a given list of image URLs.

## Setup

1. **Navigate to the project directory:**

2. **Install dependencies:**
Make sure you have Python 3.x installed on your system. Then, install the required dependencies using pip:

```
pip install pyperclip
```


## Usage

To generate the HTML code for the image grid view, follow these steps:

1. **Prepare a JSON file:**

Create a JSON file that contains a list of image URLs. Each URL should be a string within the list. For example:

```json
["https://example.com/image1.jpg", "https://example.com/image2.jpg", "https://example.com/image3.jpg"]
```
Save this file as image_links.json in the project directory.

2. **Execute the script:**

Run the script using the following command:
```
python image_grid_generator.py <items_per_row> image_links.json
```
Replace <items_per_row> with the desired number of items in each row of the image grid.

3. **Copy the generated HTML code:**

The script will generate the HTML code for the image grid view based on the provided JSON file and print it to the console. The HTML code will also be copied to your clipboard automatically.

4. **Paste the HTML code:**

Paste the copied HTML code wherever you need it, such as in an HTML file or a content management system (CMS).
