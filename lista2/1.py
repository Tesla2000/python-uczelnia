import argparse

parser = argparse.ArgumentParser(description='Counts bytes, lines and words')
parser.add_argument('file', help='The file to read')

args = parser.parse_args()

byte_count = 0
word_count = 0
line_count = 0

curr_line = 0
max_line = 0
with open(args.file, "rb") as f:
    byte = f.read(1)
    while byte:
        byte_count += 1
        curr_line += 1
        if curr_line > max_line:
            max_line = curr_line
        
        if byte == b' ':
            word_count += 1
        elif byte == b'\n':
            line_count += 1
            curr_line = 0

        byte = f.read(1)

print('Bytes:', byte_count)
print('Words:', word_count)
print('Lines:', line_count)
print('Max line:', max_line)