# Моделька + flash сервер

## Как запустить?

Клонируем репозиторий

```shell
git clone ...
```

Устанавливаем и активируем venv

```shell
python -m venv venv/

. ./venv/bin/activate
```

Устанавливаем зависимости

```shell
pip3 install -r requirements.txt
```

Запускаем jupyter и выполняем все ячейки 

В `preprocessors.py` можно посмотреть как устроены трансформеры,
в `manager.py` - загрузка и сохранение модели.

Запускаем сервер

```shell
python start.py
```

Из коробки работает по адресу [http://0.0.0.0:5000/predict](http://0.0.0.0:5000/predict?CRIM=2.37934&ZN=0.0&INDUS=19.58&CHAS=0&NOX=0.871&RM=6.13&AGE=100.0&DIS=1.4191&RAD=5&TAX=403&PTRATIO=14.7&B=172.91&LSTAT=27.8&MEDV=13.8&DT_1=03.03.2021+02%3A53%3A03&DT_2=2021-03-22)

Для прода лучше использовать не pickle, а [onnx](http://onnx.ai/sklearn-onnx/index.html)
и не голый flask, а [nginx + wsgi + flask](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04-ru)
