# Start from the prebuilt base image
FROM agrigorev/zoomcamp-model:2025

# Set working directory (already /code in base image)
WORKDIR /code

# Copy your FastAPI app
COPY app.py .

# Install uv and requests (and other dependencies if needed)
RUN pip install uvicorn fastapi requests

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
