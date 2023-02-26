import spacy, sys
from spacy.tokens import DocBin


def upscale_dansk_train():
    nlp = spacy.blank("da")

    db_in_dansk = DocBin().from_disk("data/dansk_train.spacy")
    dansk_docs = list(db_in_dansk.get_docs(nlp.vocab))

    db_in_ontonotes = DocBin().from_disk("data/ontonotes.spacy")
    ontonotes_docs = list(db_in_ontonotes.get_docs(nlp.vocab))

    dansk_docs *= round(len(ontonotes_docs) / len(dansk_docs))

    db = DocBin()
    for doc in dansk_docs:
        db.add(doc)
    db.to_disk("data/dansk_train.spacy")


if __name__ == "__main__" and bool(sys.argv[1]):
    upscale_dansk_train()
