FROM python
COPY . .
ENV DATABASE_URI=${DATABASE_URI}
ENV SECRET_KEY=${SECRET_KEY}
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]