
import csv
import ipywidgets as widgets
from IPython.display import display, HTML
import base64

def create_download_link(file_path, description):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        encoded_data = base64.b64encode(file_data).decode()
        href = f'<a href="data:text/html;base64,{encoded_data}" download="{file_path}">{description}</a>'
        return HTML(href)

def download_file():
    """
    Creates a widget to download a file from the working directory.
    """
    # Text input to specify the file name
    file_name_input = widgets.Text(
        value='',
        placeholder='Enter file name',
        description='File:',
        disabled=False
    )
    
    # Button to initiate the download
    download_button = widgets.Button(
        description='Download',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Download the specified file',
        icon='download' # (FontAwesome names without the `fa-` prefix)
    )
    
    # Output widget to display the download link
    output = widgets.Output()

    def on_button_click(b):
        with output:
            output.clear_output()
            file_name = file_name_input.value
            if (not file_name.startswith('.') and not file_name.startswith('_')):
                try:
                    download_link = create_download_link(file_name, 'Click here to download your file')
                    display(download_link)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Please enter a valid file name.")
    
    # Attach the button click event to the handler
    download_button.on_click(on_button_click)
    
    # Display the widgets
    display(widgets.HBox([file_name_input, download_button]), output)