import joblib
import numpy as np
from urllib.request import urlopen
import subprocess
import sys
from pkg_resources import resource_filename



class Sinkaf:

    BERT_MAX_SENTENCE_TOKEN_LENGTH = 113
    BERT_HIGH_PRECISION_MODEL_NAME = "bert_pre"
    BERT_HIGH_RECALL_MODEL_NAME = "bert_rec"
    BERT_MODEL_NAMES = [
        BERT_HIGH_PRECISION_MODEL_NAME,
        BERT_HIGH_RECALL_MODEL_NAME]
    LINEAR_MODEL_NAME = "linear"

    def __init__(self, model=LINEAR_MODEL_NAME):

        self.model = model

        if self.model == Sinkaf.LINEAR_MODEL_NAME:
            self.clf = joblib.load(resource_filename('sinkaf', 'data/model_linearSVC.joblib'))
        elif self.model in Sinkaf.BERT_MODEL_NAMES:
            if self.model == Sinkaf.BERT_HIGH_PRECISION_MODEL_NAME:
                self.clf = joblib.load(resource_filename('sinkaf', 'data/clf_nn_precision.joblib'))
            elif self.model == Sinkaf.BERT_HIGH_RECALL_MODEL_NAME:
                self.clf = joblib.load(resource_filename('sinkaf', 'data/clf_nn_recall.joblib'))
            # Bert modeli icin kullanilacaklar
            try:
                import torch
                from transformers import AutoTokenizer, AutoModel
            except ImportError:
                print("BERT kullanimi icin torch ve transformers paketleri kurulacak.\n")
                Sinkaf._install_package("torch")
                Sinkaf._install_package("transformers")
            finally:
                from transformers import AutoTokenizer, AutoModel
            print("Tek seferlik BERT kurulumu gerekebilmektedir.\n")
            self.tokenizer = AutoTokenizer.from_pretrained(
                "dbmdz/bert-base-turkish-128k-uncased")
            self.bert = AutoModel.from_pretrained(
                "dbmdz/bert-base-turkish-128k-uncased")

    def _bert_vectorize(self, texts):
        input_ids = self._tokenize_input(texts)
        return self._sentence_2_vec(input_ids)

    @staticmethod
    def _get_profane_prob(prob):
        return prob[1]

    @staticmethod
    def _install_package(package):
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package])

    @staticmethod
    def _predict_prob(clf, sentence_vectors):
        return np.apply_along_axis(
            Sinkaf._get_profane_prob, 1,
            clf.predict_proba(sentence_vectors))

    def _sentence_2_vec(self, padded):
        import torch
        # pylint: disable=no-member, not-callable
        input_ids = torch.tensor(np.array(padded)).to(torch.int64)
        with torch.no_grad():
            last_hidden_states = self.bert(input_ids)
            features = last_hidden_states[0][:, 0, :].numpy()
        return features

    def _tokenize_input(self, texts):
        tokenized = [self.tokenizer.encode(
            s, add_special_tokens=True) for s in texts]
        padded = np.array(
            [s + [0]*(Sinkaf.BERT_MAX_SENTENCE_TOKEN_LENGTH-len(s)) for s in tokenized])
        return padded

    def tahmin(self, texts):
        if self.model == Sinkaf.LINEAR_MODEL_NAME:
            return self.clf.predict(texts)
        elif self.model in Sinkaf.BERT_MODEL_NAMES:
            return self.clf.predict(self._bert_vectorize(texts))

    def tahminlik(self, texts):
        if self.model == Sinkaf.LINEAR_MODEL_NAME:
            return Sinkaf._predict_prob(self.clf, texts)
        elif self.model in Sinkaf.BERT_MODEL_NAMES:
            sentence_vectors = self._bert_vectorize(texts)
            return Sinkaf._predict_prob(self.clf, sentence_vectors)
