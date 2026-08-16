import argparse
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path


def translate(text):
    query = urllib.parse.urlencode({
        "client": "gtx", "sl": "en", "tl": "vi", "dt": "t", "q": text,
    })
    with urllib.request.urlopen(
        "https://translate.googleapis.com/translate_a/single?" + query,
        timeout=30,
    ) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return "".join(part[0] for part in payload[0] if part[0])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    lines = Path(args.input).read_text(encoding="utf-8").splitlines()
    output = []
    batch = []

    def flush():
        nonlocal batch
        if not batch:
            return
        original = "\n".join(batch)
        translated = translate(original)
        output.extend(translated.splitlines())
        batch = []

    in_code = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            flush()
            in_code = not in_code
            output.append(line)
            continue
        if in_code or not stripped or stripped.startswith("|") or "http" in line:
            flush()
            output.append(line)
            continue
        if sum(len(item) + 1 for item in batch) + len(line) > 3500:
            flush()
        batch.append(line)
    flush()
    Path(args.output).write_text("\n".join(output) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
