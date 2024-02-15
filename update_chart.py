import os
import fileinput

def get_new_line_from_env(env_file_path):
    with open(env_file_path, 'r') as env_file:
        for line in env_file:
            if line.startswith('version'):
                return line.strip() + '\n'
    return None

def update_chart_yaml(file_path, new_line):
    
    for line_number, line_content in enumerate(fileinput.input(file_path, inplace=True), 1):
        if line_number == 6:
            print(new_line, end='')
        else:
            print(line_content, end='')

# Example usage:
env_file_path = '.env'
chart_file_path = 'chat_backoffice/Chart.yaml' 
new_line = get_new_line_from_env(env_file_path)
if new_line:
    print("New line to be added to Chart.yaml:", new_line)
    if os.path.isfile(chart_file_path):
        update_chart_yaml(chart_file_path, new_line)
        print("Chart.yaml updated successfully!")
    else:
        print("Error: Chart.yaml file not found.")
else:
    print("Error: 'version' line not found in the .env file.")
