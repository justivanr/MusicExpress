# MusicExpress

Within this repository, a Music Recommender System using the K-Medoids clustering method is presented. The goal of this system is to provide the user with personalized suggestions, taking into account their preferences in terms of songs. The number of suggestions can be decided by the users (e.g., 5 suggestions). Spotify playlists are used to compute the clusters and provide song suggestions to the user.
The user should provide a playlist with songs they like and may or may not provide a playlist from which suggestions should be made. To compute the best suggestions, a song is randomly picked from the user's preferences, and the Euclidean Distance measure is adopted to determine song recommendations, taking into account the songs' features.

The [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/) library is used to extract both the songs and their features from the playlist or playlists provided by the user.

The Model and Data Cards are available here:

- [Model Card](models/README.md)
- [Data Card](data/README.md)

## Requirements

- Python 3.11.5 ([Download here](https://python.domainunion.de/downloads/release/python-3115/)) (on VS Code select the Python 3.11.5 Kernel) since there might be some problems with the scikit-learn-extra library when using Python 3.12.0

- The libraries **mlflow** and **dagshub** might be highlighted by Pylance (if installed) in the [recommend.py](src/models/recommend.py) script: this won't lead to issues when using the virtual environment to run the code

We suggest you to use a virtual environment in which you can download the requirements.

### Create a Virtual Environment

We report different ways to create a virtual environment so that if you have different versions of Python on your computer, you can easily create one without needing to look it up.

#### Standard creation

- Windows:

```bash
python -m venv your_venv_name
```

- Linux:

```bash
python3 -m venv your_venv_name
```

#### Specifc Python Version creation

```bash
path\to\the\python\version\exe\you\want\to\use -m venv your_venv_name
```

Example:

```bash
path\...\Python311\python.exe -m venv your_venv_name
```

### Activate the virtual environment

- Windows:

```bash
your_venv_name/Scripts/activate
```

```bash
your_venv_name/Scripts/activate.ps1
```

- Linux:

```bash
your_venv_name/bin/activate
```

### Installation of requirements.txt

We suggest to update pip before installing the requirements in the virtual environment. Copy the following code to update pip:

```bash
python.exe -m pip install --upgrade pip
```

After updating pip, you will need to install the requirements.txt in order for the model to work and also plot the results.
You can easily install them as follows:

```bash
pip install -r requirements.txt
```

## Citation

```bibtex
@misc{MusicRecommendationUsingClusters,
author = {Rinaldi Ivan and, de Benedictis Salvatore and, Sibilla Antonio and, Laraspata Lucrezia},
title = {Music Recommendation using the K-Medoids Clustering Model},
month = {October},
year = {2023},
url = {https://github.com/se4ai2324-uniba/MusicExpress}
}
```

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── output         <- Data after clustering and song recommendations
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
