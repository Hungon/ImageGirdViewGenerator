import sys
import json
import pyperclip

def generate_image_grid(selected_images, items_per_row):
    html = '''
    <table>
        <tbody>
        <tr>
    '''
    for i, image in enumerate(selected_images):
        html += f'<td><img src="{image}" alt="Image"></td>'
        if (i + 1) % items_per_row == 0:
            html += '</tr><tr>'
    
    html += '''
        </tr>
        </tbody>
    </table>
    '''
    return html

if __name__ == '__main__':
    items_per_row = int(sys.argv[1])
    json_file = sys.argv[2]
    with open(json_file) as file:
        selected_images = json.load(file)
    html_grid = generate_image_grid(selected_images, items_per_row)
    pyperclip.copy(html_grid)
    print("HTML script has been copied to the clipboard.")
