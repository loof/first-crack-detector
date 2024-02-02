import os

from pyAudioAnalysis import audioTrainTest as aT

classifier_data_dir = './classifierData'


def classify(folder_list, classifier_type, model_name, compute_beat):
    folder_paths = []
    for folder in folder_list:
        folder_paths.append(os.path.join(classifier_data_dir, folder))

    aT.extract_features_and_train(
        folder_paths,
        1.0,
        1.0,
        aT.shortTermWindow,
        aT.shortTermStep,
        classifier_type,
        model_name,
        compute_beat)


def main():
    # Use a breakpoint in the code line below to debug your script.
    classify(["crack", "environment"], "knn", "knnCrackEnvironment", False)

if __name__ == '__main__':
    main()
