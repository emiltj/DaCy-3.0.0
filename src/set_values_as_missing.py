import spacy, sys
from spacy.tokens import DocBin, Doc

# Below is testing to make it work with settings head to None
# https://github.com/explosion/spaCy/discussions/12307

# nlp = spacy.load("en_core_web_lg")
# text = "This is a text about Paris, France"
# doc = nlp(text)
# spaces = [t.whitespace_ for t in doc]
# words = [t.text for t in doc]
# ents = doc.ents

# for t in doc:
#     print(t.head)
#     print(t.lemma)
#     print(t.dep)


# new_doc = Doc(
#     vocab=nlp.vocab,
#     words=words,
#     spaces=spaces,
#     heads=[None for t in doc],
# )

# for t in new_doc:
#     print(t.head)

# heads = [None for t in doc]


# new_doc.ents = ents
# new_doc.ents
# for t in new_doc:
#     print(t.dep)
#     print(t.lemma)
#     print(t.tag)
#     print(t.head)

# new_doc[0].head = None

# for t in new_doc:
#     print(t.head)


# datasets_to_include = "dane_dansk_ontonotes".split("_")


def set_values_as_missing():

    nlp = spacy.blank("da")

    # DANSK
    if "dansk" in datasets_to_include:
        for partition in ["", "_train", "_dev", "_test"]:
            # Load in dansk partitions
            db_in_dansk = DocBin().from_disk(f"assets/dansk{partition}.spacy")
            docs = list(db_in_dansk.get_docs(nlp.vocab))

            # Set all values for lemmas, parser, tagger as missing
            # Implement code here from https://github.com/explosion/spaCy/discussions/12307
            # Delete this when not needed any longer: Token.lemma, .tag, .dep are already set to missing. .head IS NOT
            # ...
            # ...
            # ...
            new_docs = []
            for doc in docs:
                spaces = [t.whitespace_ for t in doc]
                words = [t.text for t in doc]
                ents = doc.ents
                new_doc = Doc(
                    vocab=nlp.vocab,
                    words=words,
                    spaces=spaces,
                    lemmas=None,
                    deps=None,
                    heads=None,
                    tags=None,
                )
                new_doc.ents = ents
                new_docs.append(new_doc)

            # Save as .spacy
            db_out_dansk = DocBin()
            for doc in new_docs:
                db_out_dansk.add(doc)
            db_out_dansk.to_disk(f"data/dansk{partition}.spacy")

    # DaNE
    if "dane" in datasets_to_include:
        for partition in ["_train", "_dev", "_test"]:
            # Load in the dane partitions
            db_in_dane = DocBin().from_disk(f"assets/dane{partition}.spacy")
            docs = list(db_in_dane.get_docs(nlp.vocab))

            # Set all values ents values as missing
            for doc in docs:
                doc.set_ents([], default="missing")

            # Save as .spacy
            db_out_dane = DocBin()
            for doc in docs:
                db_out_dane.add(doc)
            db_out_dane.to_disk(f"data/dane{partition}.spacy")

    # Ontonotes
    if "ontonotes" in datasets_to_include:
        db_in_ontonotes = DocBin().from_disk("assets/ontonotes.spacy")
        docs = list(db_in_ontonotes.get_docs(nlp.vocab))
        new_docs = []
        for doc in docs:
            spaces = [t.whitespace_ for t in doc]
            words = [t.text for t in doc]
            ents = doc.ents
            new_doc = Doc(
                vocab=nlp.vocab,
                words=words,
                spaces=spaces,
                lemmas=None,
                deps=None,
                heads=None,
                tags=None,
            )
            new_doc.ents = ents
            new_docs.append(new_doc)
        db_out_ontonotes = DocBin()
        for doc in new_docs:
            db_out_ontonotes.add(doc)
        db_out_ontonotes.to_disk("data/ontonotes.spacy")


if __name__ == "__main__":
    datasets_to_include = str(sys.argv[1]).split("_")
    set_values_as_missing()
