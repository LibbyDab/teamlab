import sys

def main():
    write_to = open(sys.argv[4], 'a')
    with open(sys.argv[1]) as f:
        for line in f:
            tags = line.strip().split('\t')
            start = float(tags[0])
            end = float(tags[1])
            text = tags[2].strip()
            name = str(sys.argv[3])
            write_to.write(f'{name}_{start}_{end}\tffmpeg -loglevel -8 -i {sys.argv[2]} -ss {start} -to {end} -f wav -acodec pcm_s16le -ac 1 -ar 16k - |\n')
    write_to.close()

if __name__ == '__main__':
    main()