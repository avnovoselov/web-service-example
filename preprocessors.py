import pandas as pd

from IPython.display import display
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler

"""
Шаги для pipeline

Ниже идут несколько классов, которые наследуют `BaseEstimator` и `TransformerMixin`
для каждого нас интересуют методы `fit` и `transform`.

* `fit` - используется для обучения
* `transform` - для преобразования данных

В процессе обучения `pipeline.fit` будут использованы
оба метода. Для этого примешиваем в классы `TransformerMixin`, который добавит метод `fit_transform`.
"""


class Scaler(BaseEstimator, TransformerMixin):
    """
    Scaler - трансформер для нормализации признаков

    `MinMaxScaler` можно пробросить в pipeline напрямую (без класса Scaler),
    но тогда все последующие шаги будут работать с np.array, а не pd.DataFrame-ом
    """

    def __init__(self, columns: list):
        self.columns = columns
        self.scaler = MinMaxScaler()

    # noinspection PyUnusedLocal
    def fit(self, x, y=None):
        self.scaler.fit(x[self.columns])
        return self

    def transform(self, x):
        x = x.copy()
        x.loc[:, self.columns] = self.scaler.transform(x[self.columns])

        return x.copy()


class Drop(BaseEstimator, TransformerMixin):
    """
    Drop - удаляет колонки

    Не имеет реализации `fit` - только `transform`
    """

    def __init__(self, columns: list):
        self.columns = columns

    # noinspection PyUnusedLocal
    def fit(self, x: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, x: pd.DataFrame):
        return x.copy().drop(self.columns, axis=1)


class DateTimeParser(BaseEstimator, TransformerMixin):
    """
    DateTimeParser - парсит строку в объект datetime

    Не имеет реализации `fit` - только `transform`
    """

    def __init__(self, column: str, datetime_format):
        self.column = column
        self.datetime_format = datetime_format

    # noinspection PyUnusedLocal
    def fit(self, x: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, x: pd.DataFrame):
        x = x.copy()
        x[self.column] = pd.to_datetime(x[self.column], format=self.datetime_format)

        return x


class Info(BaseEstimator, TransformerMixin):
    """
    Info - вывод информацию по DataFrame-у

    Не имеет реализации `transform` - только `fit`
    """

    # noinspection PyUnusedLocal
    def fit(self, x: pd.DataFrame, y: pd.Series = None):
        # noinspection PyTypeChecker
        display(x.info())
        print()
        return self

    # noinspection PyMethodMayBeStatic
    def transform(self, x: pd.DataFrame):
        return x.copy()
