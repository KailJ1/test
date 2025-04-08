import os


def display_txt_files():
    # Указываем путь к целевой директории
    target_directory = '/home/mayor/Documents/kapibarovsk/'

    # Проходим по всем файлам в указанной директории
    for filename in os.listdir(target_directory):
        # Если файл имеет расширение .txt
        if filename.endswith('.txt'):
            file_path = os.path.join(target_directory, filename)
            print(f"Содержимое файла {filename}:")
            # Открываем и выводим содержимое файла
            with open(file_path, 'r') as file:
                print(file.read())
            print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    display_txt_files()
