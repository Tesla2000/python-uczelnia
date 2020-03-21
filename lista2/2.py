import argparse

parser = argparse.ArgumentParser(description='Encodes and decodes to and from base64')
group = parser.add_mutually_exclusive_group()
group.add_argument('--encode', help='The file to encode')
group.add_argument('--decode', help='The file to decode')
parser.add_argument('file', help='The result file')

args = parser.parse_args()

token_array = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

if args.encode:
    output_file = open(args.file, 'w')

    with open(args.encode, "rb") as f:
        triplet = f.read(3)
        while triplet:
            if (len(triplet) < 3):
                triplet += b"\0"*(3 - len(triplet))
            output_file.write(token_array[(int.from_bytes(triplet, byteorder='big') & 0b111111000000000000000000) >> 18])
            output_file.write(token_array[(int.from_bytes(triplet, byteorder='big') & 0b111111000000000000) >> 12])
            output_file.write(token_array[(int.from_bytes(triplet, byteorder='big') & 0b111111000000) >> 6])
            output_file.write(token_array[(int.from_bytes(triplet, byteorder='big') & 0b111111)])
            triplet = f.read(3)
else:
    output_file = open(args.file, 'wb')

    with open(args.decode, 'r') as f:
        quad = f.read(4)
        while quad:
            num = (token_array.index(quad[0]) << 18) + (token_array.index(quad[1]) << 12) + (token_array.index(quad[2]) << 6) + token_array.index(quad[3])
            output_file.write(((num & 0b111111110000000000000000) >> 16).to_bytes(1, byteorder='big'))
            output_file.write(((num & 0b1111111100000000) >> 8).to_bytes(1, byteorder='big'))
            output_file.write((num & 0b11111111).to_bytes(1, byteorder='big'))
            quad = f.read(4)