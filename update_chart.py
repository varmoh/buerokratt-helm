import os
import yaml

def read_version_from_env():
    # Read version from .env file
    env_file_path = os.path.join(os.getcwd(), '.env')
    with open(env_file_path, 'r') as env_file:
        lines = env_file.readlines()
        for line in lines:
            if line.startswith('VERSION='):
                return line.split('=')[1].strip()

def update_chart_version(version):
    # Load Chart.yaml
    chart_file_path = os.path.join(os.getcwd(), 'chat_backoffice', 'Chart.yaml')
    try:
        with open(chart_file_path, 'r') as chart_file:
            chart_data = yaml.safe_load(chart_file)

        # Update version
        chart_data['version'] = version

        # Write updated Chart.yaml
        with open(chart_file_path, 'w') as chart_file:
            yaml.dump(chart_data, chart_file)
        
        print(f"Chart version updated to {version}")
    except Exception as e:
        print(f"Error updating Chart version: {e}")

def main():
    version = read_version_from_env()
    if version:
        update_chart_version(version)
    else:
        print("Version not found in .env file")

if __name__ == "__main__":
    main()

