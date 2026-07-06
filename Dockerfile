# 1. Start from an official pre-built image: a tiny Linux with Python 3.12
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements list in, then install the packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of your code into the container
COPY . .

# 5. The command to run when the container starts
CMD ["python", "api_test.py"]
