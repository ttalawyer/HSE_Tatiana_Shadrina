import requests
from bs4 import BeautifulSoup
import json
import os


class ParserCBRF:
    def __init__(self):
        self.__data = {}

    def start(self):
        """Публичный метод: загрузка, парсинг и сохранение данных"""
        html = self.__load_page()
        self.__parse_data(html)
        self.__save_to_json()
        return self.__data

    # ----- Приватные методы -----

    def __load_page(self):
        """Загружает HTML со страницы ЦБ РФ"""
        url = "https://www.cbr.ru/hd_base/KeyRate/"
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def __parse_data(self, html):
        """Извлекает даты и ставки из таблицы"""
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", {"class": "data"})
        rows = table.find_all("tr")[1:]  # пропускаем заголовок таблицы

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                date = cols[0].get_text(strip=True)
                rate = cols[1].get_text(strip=True).replace(",", ".")
                try:
                    self.__data[date] = float(rate)
                except ValueError:
                    continue

    def __save_to_json(self):
        """Сохраняет словарь с данными в файл JSON"""
        with open("cbr_key_rate.json", "w", encoding="utf-8") as file:
            json.dump(self.__data, file, ensure_ascii=False, indent=4)
        print("Данные сохранены в файл cbr_key_rate.json")

    def __get_rate_by_date(self, date):
        """Возвращает ставку по введённой дате"""
        return self.__data.get(date)

    def __load_from_json(self):
        """Загружает данные из JSON, если файл существует"""
        if os.path.exists("cbr_key_rate.json"):
            with open("cbr_key_rate.json", "r", encoding="utf-8") as file:
                self.__data = json.load(file)


# ----- Основная часть программы -----
if __name__ == "__main__":
    parser = ParserCBRF()
    parser.start()

    print("\nДанные успешно загружены и сохранены.")
    user_date = input("Введите дату в формате ДД.ММ.ГГГГ, чтобы узнать ключевую ставку: ").strip()

    rate = parser._ParserCBRF__get_rate_by_date(user_date)

    if rate is not None:
        print(f"Ключевая ставка на {user_date}: {rate}%")
    else:
        print(f"Нет данных о ключевой ставке на дату {user_date}.")
