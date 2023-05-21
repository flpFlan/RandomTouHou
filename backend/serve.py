# -- stdlib --
import sys
import os
import argparse
from urllib.parse import urljoin

# -- third party --
from quart import Quart, jsonify, request

imgPool = []


app = Quart(__name__)


@app.route("/img")
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


def start_server():
    parser = argparse.ArgumentParser(prog=sys.argv[0])
    parser.add_argument("img_folder", type=str)
    options = parser.parse_args()
    img_folder = options.img_folder
    for _, _, fs in os.walk(img_folder):
        for f in fs:
            imgPool.append(urljoin("http://flpflan.top/", f))
    app.run()


if __name__ == "__main__":
    start_server()
