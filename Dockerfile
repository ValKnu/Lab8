FROM python

COPY . /prog.py

WORKDIR /prog.py

CMD ["python3", "prog"]
