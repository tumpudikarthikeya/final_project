# Use the official Rasa image
FROM rasa/rasa:3.6.2

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install additional dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Train the model (optional)
RUN rasa train

# Expose port for Rasa API
EXPOSE 5005

# Start Rasa server
CMD ["rasa", "run", "--enable-api", "--cors", "*"]
