FROM python:3

ADD ./cmd/requirements.txt /cmd/
RUN pip install --upgrade pip && pip3 install -r /cmd/requirements.txt --target ./package

ADD ./cmd/ /cmd

CMD ["python3", "cmd/main.py"]