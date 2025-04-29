#!/bin/bash

# Function to check if running in Docker
is_docker() {
    if [ -f /.dockerenv ]; then
        return 0
    else
        return 1
    fi
}

# Function to start the application
start_application() {
    echo "Starting application..."
    
    # Check if running in Docker
    if is_docker; then
        echo "Running in Docker container"
        # Set environment variables for Docker
        export PYTHONUNBUFFERED=1
        export PYTHONPATH=/app
    else
        echo "Running in local environment"
    fi

    # Start the application
    python3 ./ignite.py
}

# Function to handle API requests
handle_api_requests() {
    echo "API endpoint is ready to receive requests"
    # Add any API-specific setup here if needed
}

# Main execution
echo "Starting AI application..."

# Start the application
start_application &

# Handle API requests
handle_api_requests &

# Keep the container running
if is_docker; then
    echo "Container is running..."
    # Use tail to keep the container running and show logs
    tail -f /dev/null
else
    # In local environment, just wait for background processes
    wait
fi