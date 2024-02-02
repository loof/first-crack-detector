import os
import threading
import sox

data_dir = './data'
audio_file_output_name = 'audio.wav'


def start_recording_audio():

    args = ['-t',
            'waveaudio',
            '-d',
            os.path.join(data_dir, audio_file_output_name),
            'trim',
            '0',
            '01',
            ':',
            'newfile',
            ':',
            'restart']
    sox.core.sox(args)

def main():
    # Use a breakpoint in the code line below to debug your script.

    threads = [threading.Thread(target=start_recording_audio, args=())]

    for t in threads:
        t.start()

    for t in threads:
        t.join()



if __name__ == '__main__':
    main()