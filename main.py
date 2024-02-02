import atexit
import json
import os
import pathlib
import threading
import sox
from pathlib import Path
from pyAudioAnalysis import audioTrainTest as aT

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

data_dir = './data'
audio_file_output_name = 'yves.wav'


class MyEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        try:
            result = aT.file_classification(event.src_path, "knnFirstCrack", "knn")
            if result[1][0] > 0.5:
                print("Crack")
            else:
                print("Environment")
        except Exception as e:
            pass

def start_recording_audio():
    args = ['-t', 'waveaudio', '-d', data_dir + '/' + audio_file_output_name, 'trim', '0', '01', ':', 'newfile', ':', 'restart']
    sox.core.sox(args)


def create_and_start_observer():
    observer = Observer()
    observer.schedule(MyEventHandler(), data_dir, recursive=False)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def remove_files():
    for filename in os.listdir(data_dir):
        if os.path.isfile(os.path.join(data_dir, filename)):
            os.remove(os.path.join(data_dir, filename))

def main():
    # Use a breakpoint in the code line below to debug your script.

    threads = [threading.Thread(target=start_recording_audio, args=()), threading.Thread(target=create_and_start_observer, args=())]

    for t in threads:
        t.start()

    for t in threads:
        t.join()



if __name__ == '__main__':
    main()

