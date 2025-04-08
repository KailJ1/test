import os


def display_txt_files():
    # Получаем путь к текущей директории
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Проходим по всем файлам в текущей директории
    for filename in os.listdir(current_directory):
        # Если файл имеет расширение .txt
        if filename.endswith('.txt'):
            file_path = os.path.join(current_directory, filename)
            print(f"Содержимое файла {filename}:")
            # Открываем и выводим содержимое файла
            with open(file_path, 'r') as file:
                print(file.read())
            print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    display_txt_files()
