# comp3125-individual-sephora
This repository will hold all scripts that will be used in my Sephora Product Exploration Individual Project

# Structure
The project is split in the following fashion: 

```
.
├── README.md
├── code
│   ├── poetry.lock
│   ├── poetry.toml
│   ├── pyproject.toml
│   ├── sephora_analysis
│   │   ├── __init__.py
│   │   ├── analyze.ipynb
│   │   ├── collect_reviews.py
│   │   ├── data
│   │   │   ├── p384060_reviews.json.gz
│   │   │   ├── p39787544_reviews.json.gz
│   │   │   ├── p404827_reviews.json.gz
│   │   │   ├── p411885_reviews.json.gz
│   │   │   ├── p432500_reviews.json.gz
│   │   │   ├── p455936_reviews.json.gz
│   │   │   ├── p467208_reviews.json.gz
│   │   │   ├── p469438_reviews.json.gz
│   │   │   ├── p61003_reviews.json.gz
│   │   │   ├── p87985432_reviews.json.gz
│   │   │   ├── product_info.csv.gz
│   │   │   ├── purchase_intent_features.pkl
│   │   │   ├── purchase_intent_model.pkl
│   │   │   ├── reviews.db
│   │   │   ├── sephora_website_dataset.csv.gz
│   │   ├── predict.ipynb
│   │   └── top_products.py
│   └── setup.cfg
├── data -> ./code/sephora_analysis/data/
├── graphs
│   ├── graph1.png
│   ├── helpfulnessbycontext.png
│   ├── incentivizedvsnonincentivized.png
│   ├── productratingbyeyecolor.png
│   ├── productratingbyhaircolor.png
│   ├── ratingbycontext.png
│   ├── ratingbyskintone.png
│   ├── ratingbyskintype.png
│   ├── ratingwithcontroversialingredients.png
│   ├── recommendationcontroversialingredients.png
│   ├── recommendationratebyskintype.png
│   ├── recommendationrateincentivizedvsnonincentivized.png
│   ├── sentimentbyskintone.png
│   ├── sentimentbyskintype.png
│   ├── top10ingredients.png
│   ├── topwordsinnegativereviews.png
│   ├── topwordsinpositivereviews.png
│   ├── wordcloudnegative.png
│   ├── wordcloudpositive.png
│   └── wordcloudtopingredients.png
├── report
│   ├── FinalReportDraft.docx
│   ├── FinalReportDraft.pdf
│   ├── KledjaCaushiSephoraAnalysis.docx
│   └── KledjaCaushiSephoraAnalysis.pdf
└── reports

9 directories, 56 files
```

## Data
This directory contains all of the scraped data from Sephora.com

> NOTE: This is a symlink to ./code/sephora_analysis/data

## Code

This is the main area where the code is written. Poetry is used as a Python dependency manager.

To run the code run: 
1. `cd ./code`
2. `poetry install`
3. `poetry shell`
4. `eval $(poetry env activate)` to use the virtual env. 

When opening VSCODE, select the kernel/virtualvenv in ./code/.venv/bin/python

## Graphs

All the graphs from the notebooks are saved here for persistence.

## Reports

This directory has the first draft of the report and the final one following IEEE format. 