FROM python

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "run.py"]
CMD ["--drivers", "drivers.txt", "--routes", "routes.txt"]
