#
FROM python:3.10-slim

#
WORKDIR /fastAPIproject

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#
COPY ./requirements.txt .

#
RUN pip install --no-cache -r requirements.txt

#
COPY . .

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]