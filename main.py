#!/usr/bin/env python3
"""Entry program for news-image-20261122.

Copies the bundled front-page image (entry.png, drawn offline by
gen_image.py in this same session) to /output/entry.png and checks its
SHA-256 before finishing, so a corrupted copy fails loudly instead of
submitting a wrong image. Standard library only; deterministic: the
bytes written are always exactly the bundled file's bytes.
"""
import hashlib
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
BUNDLED = HERE / "entry.png"
TARGET = pathlib.Path("/output/entry.png")
EXPECTED = "d36d07c96275a879bb10904a1712ae52dc4eeacd27eb8d9bd025bf785c59d858"


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            block = fh.read(1 << 16)
            if not block:
                return h.hexdigest()
            h.update(block)


def run():
    if not BUNDLED.is_file():
        print("missing bundled image: %s" % BUNDLED, file=sys.stderr)
        return 1
    if digest(BUNDLED) != EXPECTED:
        print("bundled entry.png hash mismatch", file=sys.stderr)
        return 1
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(BUNDLED, TARGET)
    got = digest(TARGET)
    if got != EXPECTED:
        print("output hash mismatch: %s" % got, file=sys.stderr)
        return 1
    print("entry.png -> /output/entry.png sha256 %s" % got)
    return 0


if __name__ == "__main__":
    sys.exit(run())
