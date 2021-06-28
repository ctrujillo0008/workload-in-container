FROM python:3
WORKDIR C:\Users\christiantr\contain\main.py
COPY . .
RUN pip install deep-security-api && pip install pymsteams
CMD ["main.py"]
ENTRYPOINT ["python3"]
