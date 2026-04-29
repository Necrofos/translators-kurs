param(
    [string]$AntlrJar = "antlr-4.9.3-complete.jar"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $AntlrJar)) {
    throw "ANTLR jar not found: $AntlrJar"
}

$outputDir = "src/simple_python/generated"
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

java -jar $AntlrJar -Dlanguage=Python3 -visitor -no-listener -Xexact-output-dir -o $outputDir grammar/SimplePythonLexer.g4 grammar/SimplePythonParser.g4
