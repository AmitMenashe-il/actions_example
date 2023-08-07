FROM python
WORKDIR /app
EXPOSE 5000
COPY requirements.txt main.py .
RUN pip3 install -r requirements.txt
CMD ["python", "main.py"]