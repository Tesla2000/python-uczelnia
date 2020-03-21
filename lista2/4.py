from collections import defaultdict
import argparse
import hashlib
import os

def file_hash(filename):
    h = hashlib.sha256()
    b = bytearray(128 * 1024)
    m = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda: f.readinto(m), 0):
            h.update(m[:n])
    return h.hexdigest()

parser = argparse.ArgumentParser(description='Finds duplicate files in given directory')
parser.add_argument('root_dir', help='The directory to look in')

args = parser.parse_args()

known_files = defaultdict(lambda: [])

for root, dirs, files in os.walk(args.root_dir, topdown=True):
    for name in files:
        f_name = os.path.join(root, name)
        f_size = os.stat(f_name).st_size
        f_hash = file_hash(f_name)
        known_files[(f_hash, f_size)].append(f_name)

for file_list in known_files.values():
    print('------------------------')
    for file in file_list:
        print(file)
print('------------------------')
