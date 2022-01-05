
from setuptools import setup
setup(
    name="rus",
    entry_points={
        "spacy_languages": ["rus = rus:Dostoevsky_russian"],
    }
)
