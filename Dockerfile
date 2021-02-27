FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt update && apt -y install tesseract-ocr pandoc libgl1-mesa-dev mecab libmecab-dev mecab-ipadic-utf8
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --default-timeout=100 -r requirements.txt
RUN jupyter contrib nbextension install --user
RUN jupyter-nbextension install rise --py --sys-prefix
RUN jupyter-nbextension enable rise --py --sys-prefix
COPY . /code/