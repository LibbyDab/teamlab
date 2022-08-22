def main():
    read_file = open('Stuttering_Data/Captions/24fa.csv', 'r')
    write_file = open('Stuttering_Data_24fa/test/text', 'a')
    for line in read_file:
        tags = line.strip().split(',')
        num = tags[0]
        speaker = tags[1]
        caption = tags[2].upper()
        write_file.write(f'{speaker}_{num}\t' + caption + '\n')
    write_file.close()
    read_file.close()

if __name__ == '__main__':
    main()