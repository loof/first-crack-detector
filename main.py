import os
import threading
import sox
from pathlib import Path
from pyAudioAnalysis import audioTrainTest as aT

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyEventHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print(event.src_path, "modified.")

    def on_created(self, event):
        result = aT.file_classification(event.src_path, "svmSMtemp","svm")
        f = open("myfile.txt", "a")
        f.write(str(result[1][0]))
        f.close()

    def on_moved(self, event):
        print(event.src_path, "moved to", event.dest_path)

    def on_deleted(self, event):
        print(event.src_path, "deleted.")


#aT.extract_features_and_train(["classifierData/crack","classifierData/environment"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmFirstCrack", False)
#aT.file_classification("data/doremi.wav", "svmSMtemp","svm")

def task1():
    args = ['-t', 'waveaudio', '-d', 'audio.wav', 'trim', '0', '01',  ':', 'newfile', ':', 'restart']
    sox.core.sox(args)

def task2():
    observer = Observer()
    observer.schedule(MyEventHandler(), "./data", recursive=False)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



def main():
    # Use a breakpoint in the code line below to debug your script.

    threads = list()
    threads.append(threading.Thread(target=task1, args=()))
    threads.append(threading.Thread(target=task2, args=()))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
