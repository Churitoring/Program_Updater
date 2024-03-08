import os
import shutil
import requests
import zipfile
from subprocess import Popen
import time
import threading
import json
import sys

def loading_spinner():
    spinner = ['\\', '|', '/', '-']
    i = 0
    while True:
        print(f"\r업데이트중! {spinner[i % len(spinner)]}", end="")
        i += 1
        time.sleep(0.1)

def print_update_status(local_version, target_version):
    os.system('cls' if os.name == 'nt' else 'clear')
    if local_version == '':
        print(f"이 창을 닫지 마세요. \n{target_version}까지 최초 다운로드 중...")
    else:
        print(f"이 창을 닫지 마세요. \n{local_version} → {target_version}")

def create_and_execute_updating_file(updater_file_path, updating_file_path):
    if current_exe_name != 'updating....exe':
        shutil.copy(updater_file_path, updating_file_path)
        Popen([updating_file_path])
        os._exit(0)

def download_and_extract_assets(assets, target_version):
    for asset in assets:
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
                                try:
                                    with zip_ref.open(member) as source:
                                        with open(target_path, 'wb') as target:
                                            shutil.copyfileobj(source, target)
                                except Exception as e:
                                    continue  # 덮어쓰기 실패하면 무시하고 계속 진행
                    else:
                        for member in zip_ref.infolist():
                            try:
                                zip_ref.extract(member, current_directory)
                            except Exception as e:
                                continue  # 덮어쓰기 실패하면 무시하고 계속 진행

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
        version_file.write(target_version)

    Popen([updater_file_path])
    os._exit(0)

def delete_empty_files(directory):
    for foldername, _, filenames in os.walk(directory, topdown=False):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if os.path.getsize(file_path) == 0:
                try:
                    os.remove(file_path)
                    print(f'{file_path} has been removed.')
                except Exception as e:
                    print(f'Failed to remove {file_path}: {str(e)}')
        
        if not os.listdir(foldername):
            try:
                os.rmdir(foldername)
                print(f'Empty directory {foldername} has been removed.')
            except Exception as e:
                print(f'Failed to remove directory {foldername}: {str(e)}')


# 파일을 읽기 모드로 열기
with open('./lib/management.json', 'r') as f:
    # JSON 데이터를 읽고, Python 딕셔너리로 변환
    data = json.load(f)

# JSON 데이터에서 실행 파일 이름과 레포지터리 이름 가져오기
github_repo = data['github_repo']
executable_name = data['executable_name']
folder_remove = data['folder_remove']
delete_zerobyte = data['delete_zerobyte']
delta_update = data['delta_update']

if github_repo.startswith('/'):
    github_repo = github_repo[1:]
if github_repo.endswith('/'):
    github_repo = github_repo[:-1]

spinner_thread = threading.Thread(target=loading_spinner)
spinner_thread.daemon = True
spinner_thread.start()
os.system('cls' if os.name == 'nt' else 'clear')
print("이 창을 닫지 마세요.")

current_directory = os.path.dirname(os.path.realpath(sys.executable))
version_file_path = os.path.join(current_directory, 'lib', 'version')
updating_file_path = os.path.join(current_directory, 'updating....exe')
game_exe_path = os.path.join(current_directory, executable_name)
filename, file_extension = os.path.splitext(executable_name)
current_exe_name = os.path.basename(sys.argv[0])
current_exe_path = os.path.join(current_directory, f'{current_exe_name}.exe')
current_exe_json = os.path.join(current_directory, 'lib', 'program_name.json')

if current_exe_name != 'updating....exe':
    # JSON 파일이 존재하는지 확인합니다.
    if not os.path.exists(current_exe_json):
    # JSON 파일이 존재하지 않는 경우, 디렉토리를 생성합니다.
        os.makedirs(os.path.dirname(current_exe_json), exist_ok=True)
    with open(current_exe_json, 'w') as f:
        json.dump(current_exe_name, f)

with open(current_exe_json, 'r') as f:
    updater_file_path = json.load(f)

if not os.path.exists(version_file_path):
    with open(version_file_path, 'w', encoding='utf-8') as version_file:
        local_version = ''
else:
    with open(version_file_path, 'r', encoding='utf-8') as version_file:
        local_version = version_file.read().strip()

if delta_update == True:
    try:
        response = requests.get(f'https://api.github.com/repos/{github_repo}/releases')
        response.raise_for_status()
        releases = response.json()
        # 버전을 기준으로 오름차순 정렬
        releases.sort(key=lambda x: x['tag_name'])
    except requests.exceptions.RequestException as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"릴리즈 목록을 가져오는 중 오류가 발생했습니다: {e}")
        releases = []
    for release in releases:
        release_version = release['tag_name']
        if release_version > local_version:
            create_and_execute_updating_file(updater_file_path, updating_file_path)
            print_update_status(local_version, release_version)
            download_and_extract_assets(release['assets'], release_version)
else:
    try:
        response = requests.get(f'https://api.github.com/repos/{github_repo}/releases/latest')
        response.raise_for_status()
        latest_version = response.json()['tag_name']
    except requests.exceptions.RequestException as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"최신 버전을 확인하는 중 오류가 발생했습니다: {e}")
        latest_version = local_version
    if local_version != latest_version:
        create_and_execute_updating_file(updater_file_path, updating_file_path)
        print_update_status(local_version, latest_version)
        download_and_extract_assets(response.json()['assets'], latest_version)

if os.path.exists(updating_file_path):
    if current_exe_name != 'updating....exe':
        os.remove(updating_file_path)

if delete_zerobyte == True:
    delete_empty_files('./')

os.system('cls' if os.name == 'nt' else 'clear')

if len(executable_name) != 0 :
    if file_extension == '.exe':
        Popen([game_exe_path])
    else: os.startfile(game_exe_path)
    print("실행중...")
    
else: print("업데이트 완료")