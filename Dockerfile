FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y openjdk-21-jre curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN curl -fsSL https://www.antlr.org/download/antlr-4.9.3-complete.jar -o antlr-4.9.3-complete.jar \
    && java -jar antlr-4.9.3-complete.jar -Dlanguage=Python3 -visitor -no-listener -Xexact-output-dir -o src/simple_python/generated grammar/SimplePythonLexer.g4 grammar/SimplePythonParser.g4

CMD ["python", "src/main.py", "examples/demo.csub"]
