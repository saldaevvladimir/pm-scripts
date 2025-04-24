import matplotlib.pyplot as plt
from collections import Counter


class Visualizer():
    def __init__(self, data):
        self.data = data

    def plot_all(self):
        self.plot_gender_distribution()
        self.plot_age_distribution()
        self.plot_employment_status_distribution()
        self.plot_main_income_source_distribution()
        self.plot_income_level_distribution()
        self.plot_interests_distribution()
        self.plot_when_started_anime_distribution()
        self.plot_watching_frequency_distribution()
        self.plot_last_watched_distribution()
        self.plot_choose_distribution()
        self.plot_fav_genres_distribution()
        self.plot_device_usage_distribution()
        self.plot_format_distribution()
        self.plot_ongoing_distribution()
        self.plot_anime_source_distribution()
        self.plot_source_reasons_distribution()
        self.plot_most_valuable_distribution()
        self.plot_less_valueable_distribution()
        self.plot_social_networks_distribution()
        self.plot_community_distribution()

    def plot_distribution(self, column_index, title, split=False):
        if column_index < 0 or column_index >= len(self.data[0]):
            raise ValueError(f"Некорректный индекс столбца: {column_index}")

        column_data = []
        for row in self.data[1:]:
            if row[column_index]:
                if split:
                    column_data.extend(row[column_index].split(', '))
                else:
                    column_data.append(row[column_index])

        # Определяем, являются ли данные числовыми
        try:
            column_data = [float(x.strip()) for x in column_data]
            is_numeric = True
        except ValueError:
            is_numeric = False

        if is_numeric:
            column_data.sort()

        counter = Counter(column_data)
        labels, values = zip(*counter.items())

        plt.figure(figsize=(10, 6))
        if is_numeric:
            # Используем гистограмму для числовых данных
            plt.hist(column_data, bins=10, color='skyblue', edgecolor='black')
            plt.xlabel('Значение')
            plt.ylabel('Количество')
            plt.title(title)
            plt.xticks(rotation=45, ha='right')
        else:
            # Используем столбчатую диаграмму для строковых данных
            plt.bar(labels, values, color='skyblue')
            plt.xlabel('Категория')
            plt.ylabel('Количество')
            plt.title(title)
            plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    def plot_gender_distribution(self):
        self.plot_distribution(1, 'Распределение по полу') 

    def plot_age_distribution(self):
        self.plot_distribution(2, 'Распределение по возрасту')

    def plot_employment_status_distribution(self):
        self.plot_distribution(3, 'Распределение по статусу занятости')  

    def plot_main_income_source_distribution(self):
        self.plot_distribution(4, 'Распределение по основному источнику заработка') 

    def plot_income_level_distribution(self):
        self.plot_distribution(5, 'Распределение по уровню заработка')

    def plot_interests_distribution(self):
        self.plot_distribution(6, 'интересы и хобби', True)

    def plot_when_started_anime_distribution(self):
        self.plot_distribution(7, 'Распределение по времени начала просмотра аниме')

    def plot_watching_frequency_distribution(self):
        self.plot_distribution(8, 'Распределение по частоте просмотра аниме')

    def plot_last_watched_distribution(self):
        self.plot_distribution(9, 'последнее просмотренное аниме', True)

    def plot_choose_distribution(self):
        self.plot_distribution(10, 'как выбирает что смотреть', True)

    def plot_fav_genres_distribution(self):
        self.plot_distribution(11, 'любимые жанры', True)

    def plot_device_usage_distribution(self):
        self.plot_distribution(12, 'Распределение по устройству для просмотра аниме')

    def plot_format_distribution(self):
        self.plot_distribution(13, 'дубляж или субтитры')

    def plot_ongoing_distribution(self):
        self.plot_distribution(14, 'ждет ли пока выйдет весь сезон')

    def plot_anime_source_distribution(self):
        self.plot_distribution(15, 'в каком источнике обычно смотрит', True)

    def plot_source_reasons_distribution(self):
        self.plot_distribution(16, 'причины выбора этого источника', True)

    def plot_most_valuable_distribution(self):
        self.plot_distribution(17, 'НАИБОЛЕЕ важное', True)

    def plot_less_valueable_distribution(self):
        self.plot_distribution(18, 'НАИМЕНЕЕ важное', True)

    def plot_social_networks_distribution(self):
        self.plot_distribution(19, 'основные соц сети', True)
    
    def plot_community_distribution(self):
        self.plot_distribution(20, 'состоит в тематических сообществах', True)


    