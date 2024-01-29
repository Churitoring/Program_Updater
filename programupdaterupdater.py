import os
import shutil
import requests
import zipfile
from subprocess import Popen
import time
import threading
import sys

executable_name = ""
program_name = "This Program Updater"
github_repo = "Churitoring/Program_Updater"
folder_remove = False
delete_zerobyte = False

if github_repo.startswith('/'):
    github_repo = github_repo[1:]
if github_repo.endswith('/'):
    github_repo = github_repo[:-1]

def loading_spinner():
    spinner = ['\\', '|', '/', '-']
    i = 0
    while True:
        print(f"\r업데이트중! {spinner[i % len(spinner)]}", end="")
        i += 1
        time.sleep(0.1)

spinner_thread = threading.Thread(target=loading_spinner)
spinner_thread.daemon = True
spinner_thread.start()
os.system('cls' if os.name == 'nt' else 'clear')
print("이 창을 닫지 마세요.")

current_directory = os.path.dirname(os.path.realpath(sys.executable))
version_file_path = os.path.join(current_directory, 'versions')
updatingexe_file_path = os.path.join(current_directory, 'updating....exe')
updating_file_path = os.path.join(current_directory, 'updating...')
update_file_path = os.path.join(current_directory, f'{program_name}.exe')
game_exe_path = os.path.join(current_directory, executable_name)
filename, file_extension = os.path.splitext(executable_name)

if not os.path.exists(version_file_path):
    with open(version_file_path, 'w', encoding='utf-8') as version_file:
        local_version = ''
else:
    with open(version_file_path, 'r', encoding='utf-8') as version_file:
        local_version = version_file.read().strip()

try:
    response = requests.get(f'https://api.github.com/repos/{github_repo}/releases/latest')
    response.raise_for_status()
    latest_version = response.json()['tag_name']
except requests.exceptions.RequestException as e:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"최신 버전을 확인하는 중 오류가 발생했습니다: {e}")
    latest_version = local_version

if local_version != latest_version:
    if not os.path.exists(updating_file_path):
        shutil.copy(update_file_path, updatingexe_file_path)
        open(updating_file_path, 'w').close()
        Popen([updatingexe_file_path])
        os._exit(0)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        os.remove(updating_file_path)
        if local_version == '':
            print(f"이 창을 닫지 마세요. \n{latest_version}까지 최초 다운로드 중...")
        else:
            print(f"이 창을 닫지 마세요. \n{local_version} → {latest_version}")

        try:
            response = requests.get(f'https://api.github.com/repos/{github_repo}/releases/latest')
            response.raise_for_status()

            for asset in response.json()['assets']:
                file_url = asset['browser_download_url']
                file_name = os.path.join(current_directory, asset['name'])

                try:
                    file_response = requests.get(file_url)
                    file_response.raise_for_status()

                    with open(file_name, 'wb') as f:
                        f.write(file_response.content)

                    if file_name.endswith('.zip'):
                        with zipfile.ZipFile(file_name, 'r') as zip_ref:
                            if folder_remove == True:
                                for member in zip_ref.infolist():
                                    try:
                                        member.filename = member.filename.encode('cp437').decode('euc-kr', 'ignore')
                                    except UnicodeDecodeError:
                                        member.filename = member.filename.encode('cp437').decode('utf-8', 'ignore')
                                    # 최상위 폴더 구조를 무시하고 파일 경로에서 상위 폴더명을 제거
                                    relative_path = os.path.relpath(member.filename, member.filename.split('/', 1)[0])
                                    target_path = os.path.join(current_directory, relative_path)
                                    # 폴더인 경우 폴더를 생성
                                    if member.is_dir():
                                        os.makedirs(target_path, exist_ok=True)
                                    else:  # 파일인 경우 파일을 쓴다.
                                        with zip_ref.open(member) as source, open(target_path, 'wb') as target:
                                            shutil.copyfileobj(source, target)
                            else: zip_ref.extractall(current_directory)

                    # 압축 파일 삭제
                    try:
                        os.remove(file_name)
                    except Exception as e:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"압축 파일 삭제 중 오류가 발생했습니다: {e}")

                except requests.exceptions.RequestException as e:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"파일 다운로드 중 오류가 발생했습니다: {e}")

            with open(version_file_path, 'w', encoding='utf-8') as version_file:
                version_file.write(latest_version)
        except requests.exceptions.RequestException as e:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"최신 릴리즈 다운로드 중 오류가 발생했습니다: {e}")

        Popen([update_file_path])
        os._exit(0)

def delete_empty_files(directory):
    # 현재 디렉토리와 하위 디렉토리의 모든 파일을 검색합니다.
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            # 파일 크기가 0인 경우 삭제합니다.
            if os.path.getsize(file_path) == 0:
                os.remove(file_path)
                print(f'{file_path} has been removed.')

if os.path.exists(updatingexe_file_path):
    os.remove(updatingexe_file_path)

if delete_zerobyte == True:
    delete_empty_files('./')

os.system('cls' if os.name == 'nt' else 'clear')

if len(executable_name) != 0 :
    if file_extension == '.exe':
        Popen([game_exe_path])
    else: os.startfile(game_exe_path)
    print("실행중...")
    
else: print("업데이트 완료")