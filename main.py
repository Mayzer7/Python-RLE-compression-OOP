class EncoderDecoder:
    def __init__(self):
        self.file_content: str = ""
        self.encode_string: str = ""
        self.decoded_string: str = ""

    def open_file(self):
        with open("Text.txt", "r", encoding="utf-8") as file:
            self.file_content = file.read().replace("\n", "")
            if not self.file_content:
                raise ValueError("Файл пустой! Запишите в него что нибудь, например aaaabbbssssrrasdc")

    def encode(self) -> str:
        """Метод для кодирования текста"""
        count = 1
        for i in range(len(self.file_content) - 1):
            if self.file_content[i] == self.file_content[i + 1]:
                count += 1
            else:
                self.encode_string += self.file_content[i] + str(count) 
                count = 1  # Сбрасываем счётчик

        self.encode_string += self.file_content[-1] + str(count)  # Добавляем последний символ и его количество

        # Запись закодированной строки в файл
        with open("Encode.txt", "w+", encoding="utf-8") as encode:
            encode.write(self.encode_string) 

        return self.encode_string

    def decode(self) -> str:
        """Метод для декодирования строки"""
        char = '' 
        str_number = ""  
        for i in range(len(self.encode_string)):
            if self.encode_string[i].isdigit():
                str_number += self.encode_string[i]
            else:
                if str_number: # Проверяем, есть ли накопленное число
                    self.decoded_string += char * int(str_number)  # Повторяем символ
                    str_number = ""  # Сбрасываем строку для чисел
                char = self.encode_string[i]  # Обновляем текущий символ

        # Обработка последнего числа и символа
        if str_number:
            self.decoded_string += char * int(str_number)

        # Запись декодированной строки в файл
        with open("Decode.txt", "w+", encoding="utf-8") as decode:
            decode.write(self.decoded_string)  

        return self.decoded_string


e = EncoderDecoder()
e.open_file()
encoded = e.encode()  # Кодируем и сохраняем в файл
print(f"Закодированная строка: {encoded}")
decoded = e.decode()  # Декодируем и сохраняем в файл
print(f"Декодированная строка: {decoded}")
print("Файлы сохранены")