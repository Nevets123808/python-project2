FROM python
COPY . .
RUN pip3 install -r requirements.txt
ENV DOCKER_URI=${DOCKER_URI}
ENV SECRET_KEY=${SECRET_KEY}
ENTRYPOINT ["python3", "app.py"]