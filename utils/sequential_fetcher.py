from libs.datasets import load_dataset

class SequentialFetcher:
    def __init__(self, rel_dir, type="imagefolder") :
        self._type = type
        self._rel_dir = rel_dir

    def return_dataset(self):
        dataset = load_dataset(self._type, data_dir=self._rel_dir)

        return self.dataset
    
