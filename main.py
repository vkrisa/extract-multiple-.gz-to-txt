from tqdm import tqdm
import argparse
import pathlib
import gzip

parser = argparse.ArgumentParser(description="Read tar.gz files content and save it to train.txt")
parser.add_argument('root', type=pathlib.Path, help="webcrawl tar.gz folder path")

args = parser.parse_args()


def collect(root: pathlib.Path):
    for item in root.iterdir():
        if item.is_file() and item.suffix == '.gz':
            yield item


def extract(file: pathlib.Path) -> str:
    with gzip.open(str(file), 'rt', encoding='utf-8') as f:
        content = f.read()
        return content


if __name__ == '__main__':
    files = tuple(collect(args.root))
    with open("train.txt", "w", encoding='utf-8') as f:
        for file in tqdm(files):
            text = extract(file)
            f.write(text)

