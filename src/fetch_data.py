def fetch_dane_as_conllu():
    from danlp.datasets import DDT

    ddt = DDT()
    train, dev, test = ddt.load_as_conllu(predefined_splits=True)
    with open("assets/dane/dane_train.conllu", "w") as f:
        train.write(f)
    with open("assets/dane/dane_dev.conllu", "w") as f:
        dev.write(f)
    with open("assets/dane/dane_test.conllu", "w") as f:
        test.write(f)

def fetch_dansk():
    # Needs to be written out
    pass

def fetch_ontonotes():
    # Needs to be written out
    pass

if __name__ == "__main__":
    fetch_dane_as_conllu()
    
    # fetch_dansk()
    print("DANSK not fetched, please transfer manually ...")
    
    # fetch_ontonotes()
    print("Ontonotes not fetched, please transfer manually... ")
