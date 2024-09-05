FROM python:3.9-slim

WORKDIR RESOLVER_O.R_PROBLEM

COPY . .

RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 5000

CMD ["python", "run.py"]
