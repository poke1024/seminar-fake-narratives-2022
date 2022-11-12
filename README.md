# Python setup for seminar on fake narratives, 2022/23

Please make sure you have anaconda or miniconda installed. If you don't have any of these installed, please go to https://docs.conda.io/en/latest/miniconda.html and use the "Latest Miniconda Installer Links" for your operating system.

## Step 1: clone repo

```bash
git clone https://github.com/poke1024/seminar-fake-narratives-2022
```

## Step 2: create conda environment

```
cd seminar-fake-narratives-2022
conda env create -f environment.yml
```

## Step 3: download models

```
conda activate fakenarr2022
python load_models.py
```

Upon first calling this, this might take some time, since it downloads several GBs of data for various models. If everything works OK, you will see:

```
loading insightface... OK
loading easyocr... OK
loading DETR... OK
loading RoBERTa... OK
```

## Step 4: check that jupyter is functional

```
conda activate fakenarr2022
jupyter lab
```

This should a browser with jupyter lab.

