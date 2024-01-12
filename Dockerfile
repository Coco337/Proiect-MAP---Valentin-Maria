FROM python:3.9-slim
WORKDIR /usr/src/myapp
COPY turnuri.py .
CMD ["python", "turnuri.py"]