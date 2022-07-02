from readline import read_init_file
import sys
import os

def main():
    for speaker in sorted(os.listdir('M_Data')):
        os.chdir('/mount/arbeitsdaten61/studenten3/team-lab-phonetics/2022/student_directories/Catherine_Dabrowski/kaldi/egs/mini_librispeech/s5/Dysarthria_Data/M_Data')
        for session in sorted(os.listdir(speaker)):
            os.chdir(os.path.join('/mount/arbeitsdaten61/studenten3/team-lab-phonetics/2022/student_directories/Catherine_Dabrowski/kaldi/egs/mini_librispeech/s5/Dysarthria_Data/M_Data', speaker, session))
            for txt_file in sorted(os.listdir('Prompts')):
                wav_file = str(txt_file).replace('.txt', '.wav')
                if os.path.isfile(os.path.join('Prompts', txt_file)) and os.path.isfile(os.path.join('Audio', wav_file)):
                    write_file = open('utt2spk.txt', 'a')
                    utt_ID = str('M_Data.' + str(speaker) + '.' + str(session).replace('Session', '') + '.' + str(txt_file).replace('.txt', ''))
                    write_file.write(utt_ID + '\t' + speaker + '\n')
                    write_file.close()

if __name__ == '__main__':
    main()