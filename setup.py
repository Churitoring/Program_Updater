import subprocess

file_name="programupdaterupdater"

def run_pyinstaller():
    command = f'pyinstaller --onefile --icon=programupdater.ico {file_name}.py'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print(f'Error: {error}')
    else:
        print(f'Output: {output}')

if __name__ == "__main__":
    run_pyinstaller()