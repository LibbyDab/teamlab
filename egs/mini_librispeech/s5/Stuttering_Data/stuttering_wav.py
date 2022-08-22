def main():
    filepath = '/mount/arbeitsdaten61/studenten3/team-lab-phonetics/2022/student_directories/Catherine_Dabrowski/kaldi/egs/mini_librispeech/s5/Stuttering_Data/Audio/24fa'
    read_file = open('Stuttering_Data/Captions/24fa.csv', 'r')
    write_file = open('Stuttering_Data_24fa/test/wav.scp', 'a')
    for line in read_file:
        tags = line.strip().split(',')
        num = tags[0]
        speaker = tags[1]
        write_file.write(f'{speaker}_{num}\t' + f'{filepath}/{speaker}_{num}.wav' + '\n')
    write_file.close()
    read_file.close()

if __name__ == '__main__':
    main()