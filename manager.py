import pickle

from sklearn.pipeline import Pipeline


def save_pipeline(pipeline: Pipeline, file_path: str) -> None:
    with open(file_path, 'wb') as f:
        pickle.dump(pipeline, f)


def load_pipeline(file_path: str) -> Pipeline:
    with open(file_path, 'rb') as f:
        return pickle.load(f)
