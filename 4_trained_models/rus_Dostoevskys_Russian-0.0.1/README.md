Russian pipeline optimized for GPU. Components: tok2vec, tagger, parser, senter, lemmatizer.

| Feature | Description |
| --- | --- |
| **Name** | `rus_Dostoevskys_Russian` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `tok2vec`, `tagger`, `parser`, `ner` |
| **Components** | `tok2vec`, `tagger`, `parser`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | `MIT` |
| **Author** | [New Languages for NLP](https://newnlp.princeton.edu) |

### Label Scheme

<details>

<summary>View label scheme (23 labels for 3 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `ADJ`, `ADP`, `ADV`, `AUX`, `CCONJ`, `DET`, `INTJ`, `NOUN`, `NUM`, `PART`, `PRON`, `PROPN`, `PUNCT`, `SCONJ`, `VERB`, `X`, `_` |
| **`parser`** | `ROOT`, `_`, `dep` |
| **`ner`** | `FAC`, `PER`, `null` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TAG_ACC` | 34.35 |
| `DEP_UAS` | 100.00 |
| `DEP_LAS` | 0.00 |
| `SENTS_P` | 100.00 |
| `SENTS_R` | 100.00 |
| `SENTS_F` | 100.00 |
| `ENTS_F` | 9.89 |
| `ENTS_P` | 6.81 |
| `ENTS_R` | 18.04 |
| `TOK2VEC_LOSS` | 0.00 |
| `TAGGER_LOSS` | 75105.88 |
| `PARSER_LOSS` | 0.00 |
| `NER_LOSS` | 38214.29 |