import os
import shutil

# 다운로드 폴더 경로
download_folder = r'c:\Users\student\Downloads'

# 이미지 파일을 저장할 폴더 경로
image_folder = r'\images'
# CSV 및 엑셀 파일을 저장할 폴더 경로
data_folder = r'\data'
# 텍스트, 워드 및 PDF 파일을 저장할 폴더 경로
docs_folder = r'\docs'
# 압축 파일을 저장할 폴더 경로
archive_folder = r'\archive'

# 폴더 생성 (이미 존재하는 경우 무시)
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# 파일 이동
def move_files(source_folder, target_folder, extensions):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(extensions):
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_folder, file)
                shutil.move(source_path, target_path)
                print(f"Moved {file} to {target_folder}")

# 폴더 생성
create_folder(download_folder + image_folder)
create_folder(download_folder + data_folder)
create_folder(download_folder + docs_folder)
create_folder(download_folder + archive_folder)

# 파일 이동 (확장자별로)
move_files(download_folder, download_folder + image_folder, ('.jpg', '.jpeg'))
move_files(download_folder, download_folder + data_folder, ('.csv', '.xlsx'))
move_files(download_folder, download_folder + docs_folder, ('.txt', '.doc', '.pdf'))
move_files(download_folder, download_folder + archive_folder, '.zip')
