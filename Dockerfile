# Base image
FROM python:3

# 官方教學有這兩行, 不過拿掉後沒感覺到差別...
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt
RUN python3 manage.py migrate

# 只要有設 port 環境變數, 有沒有寫明 -b 都沒差.不過這邊提醒一下自己.不然又不知道東西去那裡了...
CMD gunicorn -b 0.0.0.0:$PORT accounting.wsgi