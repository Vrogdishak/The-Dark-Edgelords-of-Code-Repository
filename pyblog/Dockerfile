FROM python:3-alpine

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENV WORDPRESS_USER=""
ENV WORDPRESS_PASSWORD=""
ENV WORDPRESS_URL=""


USER 1001

CMD python pyblog.py