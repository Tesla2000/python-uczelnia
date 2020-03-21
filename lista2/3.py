import argparse
import os

parser = argparse.ArgumentParser(description='Lowercases every file and directory under given root')
parser.add_argument('root_dir', help='The directory to rename')

args = parser.parse_args()

for root, dirs, files in os.walk(args.root_dir, topdown=True):
    for name in files:
        os.rename(os.path.join(root, name), os.path.join(root, name).lower())
    for name in dirs:
        os.rename(os.path.join(root, name), os.path.join(root, name).lower())