To-do list:
    - Download DaNE somewhere separate and convert to spacy and upload to sciencedata.dk
        (for conversion use https://github.com/centre-for-humanities-computing/DaCy/blob/main/training/v0.1.1/utils.py and "python -m spacy convert assets/${vars.dataset}/${vars.train_name}.conllu corpus/dane --converter conllu --merge-subtokens -n 10")
        (for upload use https://sciencedata.dk/index.php/apps/files/?dir=%2Fdata)
    - Fill dataset_links.txt
    - Fill fetch_data.py 
        (use https://www.tutorialspoint.com/downloading-files-from-web-using-python)
    - Fill remove_ner_dane.py (??)
    - Fill split_datasets.py 
        (for dane, use predefined splits (https://github.com/centre-for-humanities-computing/DaCy/blob/main/training/v0.1.1/utils.py)
    - Fill merge_datasets.py
    - Try out the commands from the top, locally BUT REMEMBER TO DEACTIVATE CONDA

data access for now:
https://sciencedata.dk/index.php/apps/files/?dir=%2Fdata

wandb login:
insert API-key from https://wandb.ai/settings

huggingface login:
insert token (WRITE) from https://huggingface.co/settings/tokens