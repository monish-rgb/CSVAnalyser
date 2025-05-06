FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

# Accept build arguments (used during build time)
ARG OPENAI_API_KEY
# Set as environment variable (available at runtime)
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

EXPOSE 8501

CMD ["python","-m","streamlit", "run", "app.py"]
