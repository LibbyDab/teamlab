def main():
    write_file = open('Dysarthria_Data/local/corpus.txt', 'a')
    read_file = open('Dysarthria_Data/train_F01_M01_M02/text', 'r')
    words = []
    for line in read_file:
            line = str(line.strip().split('\t')[1])
#            line = line.split()
            write_file.write(line + '\n')
#            for word in line:
#                if word in words or 'Data' in word:
#                    continue
#                else:
#                    words.append(word)
#                    write_file.write(word + '\n')
    write_file.close()

if __name__ == '__main__':
    main()