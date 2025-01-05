FROM python:3.10

WORKDIR /app

RUN python -m venv /opt/venv


ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "weatherproject.wsgi:application", "--bind", "0.0.0.0:8000"]
