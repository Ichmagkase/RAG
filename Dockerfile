FROM unsloth/unsloth:latest

WORKDIR /app
COPY . .

RUN pip install uv && uv sync

CMD ["uv", "run", "python", "main.py"]
