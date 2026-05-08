# Python RLE Compression — OOP

> Реализация алгоритма сжатия **Run-Length Encoding (RLE)** на Python с применением объектно-ориентированного программирования.

---

## Что такое RLE?

**Run-Length Encoding** — алгоритм сжатия данных без потерь, который заменяет повторяющиеся символы на символ и количество его повторений.

```
aaaabbbssssrr  →  a4b3s4r2
a4b3s4r2       →  aaaabbbssssrr
```

---

## Быстрый старт

```bash
git clone https://github.com/Mayzer7/Python-RLE-compression-OOP.git
cd Python-RLE-compression-OOP
python main.py
```

---

## Как это работает

1. Запись исходного текста в файл `Text.txt`
2. Запуск скрипта — программа кодирует и декодирует текст
3. Результаты сохраняются в `Encode.txt` и `Decode.txt`

---

## Структура

```
Python-RLE-compression-OOP/
├── main.py        # Основной класс EncoderDecoder
├── Text.txt       # Входной файл
├── Encode.txt     # Закодированный результат
└── Decode.txt     # Декодированный результат
```

---

## Класс `EncoderDecoder`

| Метод | Описание |
|---|---|
| `open_file()` | Читает текст из `Text.txt` |
| `encode()` | Кодирует строку по алгоритму RLE |
| `decode()` | Декодирует обратно в исходный текст |

---

## Технологии

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![OOP](https://img.shields.io/badge/Paradigm-OOP-green?style=flat-square)
