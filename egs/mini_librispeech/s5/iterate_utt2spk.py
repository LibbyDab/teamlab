import sys

def main():
    write_to = open(sys.argv[3], 'a')
    with open(sys.argv[1]) as f:
        for line in f:
            tags = line.strip().split('\t')
            start = float(tags[0])
            end = float(tags[1])
            text = tags[2].strip().upper()
            name = str(sys.argv[2])
            write_to.write(f'{name}_{start}_{end}\t{name}\n')
    write_to.close()

if __name__ == '__main__':
    main()