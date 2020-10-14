FROM python:3-alpine
WORKDIR  /project
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py FLASK_ENV=development
CMD [ "flask", "run", "--host=0.0.0.0", "--port=80" ]