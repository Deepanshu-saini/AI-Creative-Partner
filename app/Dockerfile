FROM openfabric/tee-python-cpu:dev

# Install system dependencies for LLaMA
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    ninja-build \
    python3-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install build tools
RUN python3 -m pip install --upgrade pip setuptools wheel

# Install Poetry
RUN python3 -m pip install poetry

# Copy Poetry files
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of the source code into the container
COPY . .

# Expose port 8888 for the Flask app
EXPOSE 8888

# Start the Flask app using the start.sh script
CMD ["sh","start.sh"]