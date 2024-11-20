# ChatGPT로 파일 자동분류.py
import os
import shutil

# 다운로드 폴더 경로
download_folder = r"C:\Users\student\Downloads"

# 이동 대상 폴더 설정
folders = {
    "images": [".jpg", ".jpeg"],
    "data": [".csv", ".xlsx"],
    "docs": [".txt", ".doc", ".pdf"],
    "archive": [".zip"]
}

# 대상 폴더 루트 경로
target_root = os.path.join(download_folder, "..")  # Downloads 폴더와 같은 위치에 생성

# 대상 폴더 경로 생성
for folder_name in folders.keys():
    folder_path = os.path.join(target_root, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# 파일 이동 함수
def move_file(file_path, destination_folder):
    """
    파일을 지정된 폴더로 이동합니다.
    """
    try:
        shutil.move(file_path, destination_folder)
        print(f"Moved: {file_path} -> {destination_folder}")
    except Exception as e:
        print(f"Failed to move {file_path}: {e}")

# 다운로드 폴더 파일 분류 및 이동
for file_name in os.listdir(download_folder):
    file_path = os.path.join(download_folder, file_name)

    # 파일인지 확인 (디렉터리는 제외)
    if os.path.isfile(file_path):
        # 확장자로 분류
        file_extension = os.path.splitext(file_name)[1].lower()  # 확장자를 소문자로 변환
        for folder_name, extensions in folders.items():
            if file_extension in extensions:
                destination_folder = os.path.join(target_root, folder_name)
                move_file(file_path, destination_folder)
                break
