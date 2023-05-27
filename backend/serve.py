# -- stdlib --
import sys
import os
import argparse
from urllib.parse import urljoin

# -- third party --
from quart import Quart, jsonify, request

imgPool = []


app = Quart(__name__)


@app.route("/arts")
async def serve():
    index = request.args.get("index", "1")
    num = request.args.get("num", "10")
    if not index.isdecimal():
        index = "1"
    if not num.isdecimal():
        num = "10"
    index, num = int(index) or 1, int(num) or 10
    r = imgPool[num * (index - 1) : num * index]
    return jsonify(r)


def match(f: str) -> bool:
    return (
        f.endswith("png")
        or f.endswith("jpg")
        or f.endswith("jpeg")
        or f.endswith("gif")
    )


def start_server():
    parser = argparse.ArgumentParser(prog=sys.argv[0])
    parser.add_argument("folder", type=str)
    parser.add_argument("--url", type=str, default="")
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=5000)
    options = parser.parse_args()
    folder = os.path.abspath(options.folder)
    url = options.url
    host = options.host
    port = options.port
    for path, _, fs in os.walk(folder):
        for f in fs:
            if not match(f):
                continue
            if url:
                imgPool.append(urljoin(urljoin(url, path.replace(folder, "")), f))
            else:
                imgPool.append(os.path.join(path, f))
    app.run(host=host, port=port)


if __name__ == "__main__":
    start_server()
