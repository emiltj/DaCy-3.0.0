import json, sys

if __name__ == "__main__":
    model_name = str(sys.argv[1])
    # "dane_dansk"

    version = str(sys.argv[2])
    # 0.1.1

    size = str(sys.argv[3])
    # small

    meta_json_path = str(sys.argv[4])
    # training/small/dane_dansk_ontonotes/model-best/meta.json

    no_partitioning = bool(sys.argv[5])
    # 0

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
        }
        # "large": {
        #     "name": "xlm-roberta-large",
        #     "author": "Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, Veselin Stoyanov",
        #     "url": "https://huggingface.co/xlm-roberta-large",
        #     "license": "CC BY 4.0",
        # },
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
            "name": "UD Danish DDT v2.5",
            "url": "https://github.com/UniversalDependencies/UD_Danish-DDT",
            "license": "CC BY-SA 4.0",
            "author": "Johannsen, Anders; Mart\u00ednez Alonso, H\u00e9ctor; Plank, Barbara",
        },
        {
            "name": "DaNE",
            "url": "https://github.com/alexandrainst/danlp/blob/master/docs/datasets.md#danish-dependency-treebank-dane",
            "license": "CC BY-SA 4.0",
            "author": "Rasmus Hvingelby, Amalie B. Pauli, Maria Barrett, Christina Rosted, Lasse M. Lidegaard, Anders S\u00f8gaard",
        },
        {
            "name": "DANSK - Danish Annotations for NLP Specific TasKs",
            "url": "",
            "license": "",
            "author": "",
        },
        # {
        #     "name": "OntoNotes 5.0",
        #     "url": "https://catalog.ldc.upenn.edu/LDC2013T19",
        #     "license": "LDC User Agreement for Non-Members",
        #     "author": "Ralph Weischedel, Martha Palmer, Mitchell Marcus, Eduard Hovy, Sameer Pradhan, Lance Ramshaw, Nianwen Xue, Ann Taylor, Jeff Kaufman, Michelle Franchini, Mohammed El-Bachouti, Robert Belvin, Ann Houston",
        # },
        model,
    ]
    meta[
        "description"
    ] = f"""
    <a href="https://github.com/centre-for-humanities-computing/Dacy"><img src="https://centre-for-humanities-computing.github.io/DaCy/_static/icon.png" width="175" height="175" align="right" /></a>

    # DaCy {size} transformer

    DaCy is a Danish language processing framework with state-of-the-art pipelines as well as functionality for analysing Danish pipelines.
    DaCy's largest pipeline has achieved State-of-the-Art performance on Named entity recognition, part-of-speech tagging and dependency 
    parsing for Danish on the DaNE dataset and the yet-to-be-released DANSK dataset. Check out the [DaCy repository](https://github.com/centre-for-humanities-computing/DaCy) for material on how to use DaCy and reproduce the results. 
    DaCy also contains guides on usage of the package as well as behavioural test for biases and robustness of Danish NLP pipelines.
    """

    with open(meta_json_path, "w") as out_file:
        json.dump(meta, out_file)
