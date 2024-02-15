import os
import subprocess

def get_new_line_from_env(env_file_path):
    with open(env_file_path, 'r') as env_file:
        for line in env_file:
            if line.startswith('version'):
                return line.strip() + '\n'
    return None

def update_chart_yaml(file_path, new_line):
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

   
    lines[5] = new_line

    
    with open(file_path, 'w') as file:
        file.writelines(lines)

def commit_changes(file_path, commit_message):
    subprocess.run(['git', 'add', file_path])
    subprocess.run(['git', 'commit', '-m', commit_message])

# Example usage:
env_file_path = '.env'  # Adjust the path to your .env file
chart_file_path = 'chat_backoffice/Chart.yaml'  
commit_message = 'Update version in Chart.yaml'  

new_line = get_new_line_from_env(env_file_path)
if new_line:
    print("New line to be added to Chart.yaml:", new_line)
    if os.path.isfile(chart_file_path):
        print("Chart.yaml exists.")
        try:
            update_chart_yaml(chart_file_path, new_line)
            print("Chart.yaml updated successfully!")
            commit_changes(chart_file_path, commit_message)
            print("Changes committed successfully!")
        except Exception as e:
            print("Error updating Chart.yaml:", e)
    else:
        print("Error: Chart.yaml file not found.")
else:
    print("Error: 'version' line not found in the .env file.")

