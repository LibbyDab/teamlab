from readline import read_init_file
import sys
import os

def main():
    filepath = '/mount/arbeitsdaten61/studenten3/team-lab-phonetics/2022/student_directories/Catherine_Dabrowski/kaldi/egs/mini_librispeech/s5/Dysarthria_Data/'
    for speaker in sorted(os.listdir('F_Data')):
        os.chdir(os.path.join(filepath, 'F_Data'))
        for session in sorted(os.listdir(speaker)):
            os.chdir(os.path.join(filepath, 'F_Data', speaker, session))
            for txt_file in sorted(os.listdir('Prompts')):
                wav_file = str(txt_file).replace('.txt', '.wav')
                if os.path.isfile(os.path.join('Prompts', txt_file)) and os.path.isfile(os.path.join('Audio', wav_file)):
                    read_file = open(os.path.join('Prompts', txt_file), 'r')
                    write_file = open('text.txt', 'a')
                    utt_ID = str('F_Data.F01.' + str(session).replace('Session', '') + '.' + str(txt_file).replace('.txt', ''))
                    caption = read_file.readlines()[0].replace('\n', '').upper()
                    punc = '!()-[]{};:"\,<>./?@#$%^&*_~'
                    for char in caption:
                        if char in punc:
                            caption = caption.replace(char, '')
                    write_file.write(utt_ID + '\t' + caption + '\n')
                    write_file.close()
                    read_file.close()

if __name__ == '__main__':
    main()