import json, sys

if __name__ == "__main__":
    version = str(sys.argv[1])
    size = str(sys.argv[2])
    meta_json_path = str(sys.argv[3])
    no_partitioning = bool(sys.argv[4])

    print(f"Updating {meta_json_path} with relevant information from the config ...")
    with open(meta_json_path) as f:
        meta = json.load(f)

    mdl_used = {
        "small": {
            "name": "jonfd/electra-small-nordic",
            "author": "Jón Daðason",
            "url": "https://huggingface.co/jonfd/electra-small-nordic",
            "license": "CC BY 4.0",
        },
        "medium": {
            "name": "NbAiLab/nb-roberta-base-scandi",
            "author": "Nasjonalbiblioteket AI Lab",
            "url": "https://huggingface.co/NbAiLab/nb-roberta-base-scandinavian",
            "license": "CC BY 4.0",
        },
        "large": {
            "name": "KennethEnevoldsen/dfm-bert-large-v1-2048bsz-1Msteps",
            "author": "Kenneth Enevoldsen",
            "url": "",
            "license": "CC BY 4.0",
        },
        "test": {"test": "test"},
    }
    model = mdl_used[size]

    meta["version"] = version
    if no_partitioning:
        meta["name"] += "_no_test"
    meta["email"] = "Kenneth.enevoldsen@cas.au.dk"
    meta["author"] = "Centre for Humanities Computing Aarhus"
    meta["url"] = "https://chcaa.io/#/"
    meta["license"] = "Apache-2.0 License"
    meta["requirements"] = ["spacy-transformers>=1.0.3,<1.1.0"]
    meta["sources"] = [
        {
            "name": "DANSK - Danish Annotations for NLP Specific TasKs",
            "url": "",
            "license": "",
            "author": "",
        },
        model,
    ]
    meta[
        "description"
    ] = f"""
    <a href="https://github.com/centre-for-humanities-computing/Dacy"><img src="https://centre-for-humanities-computing.github.io/DaCy/_static/icon.png" width="175" height="175" align="right" /></a>

    # DaCy {size} transformer

    DaCy is a Danish language processing framework with state-of-the-art pipelines as well as functionality for analysing Danish pipelines.
    DaCy's largest pipeline has achieved State-of-the-Art performance on Named entity recognition, part-of-speech tagging and dependency 
    parsing for Danish on the DaNE dataset. At the time of publishment it also encorporates the only models for fine-grained NER using the 18 annotation types from Ontonotes.
    Check out the [DaCy repository](https://github.com/centre-for-humanities-computing/DaCy) for material on how to use DaCy and reproduce the results. 
    DaCy also contains guides on usage of the package as well as behavioural test for biases and robustness of Danish NLP pipelines.
    """
    with open(f"template_meta_{size}.json", "w") as f:
        json.dump(meta, f)

    # with open(meta_json_path, "w") as out_file:
    #     json.dump(meta, out_file)
    #     print(f"{meta_json_path} has been updated")
