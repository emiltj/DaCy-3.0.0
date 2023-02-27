import spacy, sys
from spacy.tokens import DocBin


def merge_datasets(datasets_to_include, no_dev_test):
    nlp = spacy.blank("da")
    datasets_docs = {"train": [], "dev": [], "test": []}
    partitions = ["train", "dev", "test"]

    if not no_dev_test:
        if "dansk" in datasets_to_include:
            for p in partitions:
                docs = list(
                    DocBin().from_disk(f"data/dansk_{p}.spacy").get_docs(nlp.vocab)
                )
                datasets_docs[f"{p}"].extend(docs)

        if "dane" in datasets_to_include:
            for p in partitions:
                docs = list(
                    DocBin().from_disk(f"data/dane_{p}.spacy").get_docs(nlp.vocab)
                )
                datasets_docs[f"{p}"].extend(docs)

    if no_dev_test:
        if "dansk" in datasets_to_include:
            for p in partitions:
                docs = list(
                    DocBin().from_disk(f"data/dansk_{p}.spacy").get_docs(nlp.vocab)
                )
                datasets_docs["train"].extend(docs)

        if "dane" in datasets_to_include:
            for p in partitions:
                docs = list(
                    DocBin().from_disk(f"data/dane_{p}.spacy").get_docs(nlp.vocab)
                )
                datasets_docs["train"].extend(docs)

    if "ontonotes" in datasets_to_include:
        docs = list(DocBin().from_disk("data/ontonotes.spacy").get_docs(nlp.vocab))
        datasets_docs["train"].extend(docs)

    for p in partitions:
        db = DocBin()
        for doc in datasets_docs[f"{p}"]:
            db.add(doc)
        db.to_disk(f"data/{p}.spacy")


if __name__ == "__main__":
    datasets_to_include = str(sys.argv[1]).split("_")
    no_dev_test = bool(sys.argv[2])
    merge_datasets(datasets_to_include, no_dev_test)
