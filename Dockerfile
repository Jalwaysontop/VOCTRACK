# Use Python 3.9 image
FROM python:3.9

# Set the working directory to /code
WORKDIR /code

# 1. Install the system library required by librosa (The missing piece on Render)
RUN apt-get update && apt-get install -y libsndfile1

# 2. Copy requirements and install Python dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 3. Copy the rest of the application code
COPY . .

# 4. Create the uploads folder and fix permissions
# Hugging Face runs as user 1000, so we need to ensure it can write to this folder
RUN mkdir -p uploads && chmod 777 uploads

# 5. Run the application
# Note: Hugging Face expects port 7860
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:7860"]
