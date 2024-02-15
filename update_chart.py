import os

def get_new_line_from_env(env_file_path):
    with open(env_file_path, 'r') as env_file:
        for line in env_file:
            if line.startswith('version'):
                return line.strip() + '\n'
    return None

def update_chart_yaml(file_path, new_line):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    
    lines[5] = new_line

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

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

