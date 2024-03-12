import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 이동할 폴더 경로들
destinations = {
    '.jpg': r'C:\Users\student\Downloads\images',
    '.jpeg': r'C:\Users\student\Downloads\images',
    '.csv': r'C:\Users\student\Downloads\data',
    '.xlsx': r'C:\Users\student\Downloads\data',
    '.txt': r'C:\Users\student\Downloads\docs',
    '.doc': r'C:\Users\student\Downloads\docs',
    '.pdf': r'C:\Users\student\Downloads\docs',
    '.zip': r'C:\Users\student\Downloads\archive'
}

# 폴더 생성 함수
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 파일 이동 함수
def move_files(source_folder, destination_folder):
    create_folder_if_not_exists(destination_folder)
    for file in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, file)):
            _, extension = os.path.splitext(file)
            if extension in destinations:
                shutil.move(os.path.join(source_folder, file), destination_folder)

# 파일 이동 수행
for source_folder, destination_folder in destinations.items():
    move_files(download_folder, destination_folder)

print("파일을 이동했습니다.")
