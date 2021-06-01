FROM python:3.7.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime
RUN chmod +x /app/setup.sh
EXPOSE 8000
CMD ["./wait-for-it.sh", "mysql:3306", "-t", "0", "--", "/bin/bash", "/app/setup.sh"]