FROM openfabric/tee-python-cpu:dev

# Install system dependencies for LLaMA
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Create necessary directories
RUN mkdir -p /app/models /app/generated_images /app/generated_models

# Install Poetry
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install poetry

# Copy Poetry files
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of the source code into the container
COPY . .

# Download LLaMA model
RUN python3 download_model.py

# Expose port 8888 for the Flask app
EXPOSE 8888

# Start the Flask app using the start.sh script
CMD ["sh","start.sh"]