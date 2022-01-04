FROM python:3.9-alpine

# Prevents writing .pyc files and turns off buffering.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1

# Other environment variables.
ENV DELAY_MINUTES=60

# Install requirements and remove the file afterwards.
COPY requirements.txt .
RUN yes | pip install -r requirements.txt

COPY . /app

# Cleanup
RUN rm requirements.txt
RUN rm /app/requirements.txt

WORKDIR /app

# # Change user.
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

CMD ["python", "alwaysup.py"]
