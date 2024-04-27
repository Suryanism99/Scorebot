FROM python:3.12-slim

WORKDIR /scorebot.py

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "scorebot.py"]
