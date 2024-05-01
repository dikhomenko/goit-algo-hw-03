import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Copy files from source to destination directory and sort them by extension.")
    parser.add_argument("source", type=str, help="Path to the source directory")
    parser.add_argument("destination", type=str, nargs='?', default="dist", help="Path to the destination directory (default: 'dist')")
    return parser.parse_args()

def copy_and_sort_files(source, destination):
    # Створення директорії призначення, якщо вона не існує
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    # Рекурсивне перебирання всіх файлів у вихідній директорії
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:]  # Вилучення розширення без крапки
            if extension == "":
                extension = "no_extension"  # Папка для файлів без розширення

            # Створення піддиректорії для кожного типу файлів
            extension_dir = os.path.join(destination, extension)
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)

            # Копіювання файлу у відповідну піддиректорію
            dest_file_path = os.path.join(extension_dir, file)
            shutil.copy(file_path, dest_file_path)
            print(f"Copied {file_path} to {dest_file_path}")

def main():
    args = parse_arguments()
    try:
        copy_and_sort_files(args.source, args.destination)
        print("Files have been successfully copied and sorted.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
