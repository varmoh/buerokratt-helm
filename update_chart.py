import os
import shutil

def read_version_from_env():
    # Read version from .env file
    env_file_path = os.path.join(os.getcwd(), '.env')
    with open(env_file_path, 'r') as env_file:
        lines = env_file.readlines()
        for line in lines:
            if line.startswith('version'):
                return line.split('=')[1].strip()

def update_chart_version(version):
    # Update line 6 in Chart.yaml with the content from .env
    chart_file_path = os.path.join(os.getcwd(), 'chat_backoffice', 'Chart.yaml')
    try:
        with open(chart_file_path, 'r') as chart_file:
            chart_lines = chart_file.readlines()

        # Update line 6 with the content from .env
        chart_lines[5] = f'version: {version}\n'

        # Write updated Chart.yaml
        with open(chart_file_path, 'w') as chart_file:
            chart_file.writelines(chart_lines)

        print(f"Chart version updated to {version}")
    except Exception as e:
        print(f"Error updating Chart version: {e}")

def main():
    version = read_version_from_env()
    if version:
        update_chart_version(version)
        
        # Create Archive directory if it doesn't exist
        archive_dir = os.path.join(os.getcwd(), 'charts', 'archive')
        os.makedirs(archive_dir, exist_ok=True)
        
        # Move previous tarball files to Archive directory
        chart_dir = os.path.join(os.getcwd(), 'charts')
        for file_name in os.listdir(chart_dir):
            if file_name.endswith('.tar.gz') and file_name != f'chat_backoffice-{version}.tar.gz':
                shutil.move(os.path.join(chart_dir, file_name), os.path.join(archive_dir, file_name))
                
        print("Previous tarball files moved to Archive folder.")
    else:
        print("Version not found in .env file")

if __name__ == "__main__":
    main()
