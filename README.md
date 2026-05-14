#BeerData

from pathlib import Path

content = r"""# Untappd ML / Data Science Projektötletek

Az Untappd adatai kiválóan alkalmasak machine learning és data science gyakorlásra, mert:
- strukturáltak,
- zajosak,
- sok kategóriát tartalmaznak,
- emberi preferenciákat tükröznek.

Tipikus mezők:
- beer name
- brewery
- style
- ABV
- IBU
- rating
- rating count
- user rating
- timestamp
- location
- review text
- badge-ek
- food pairing

---

# 1. Regresszió — rating becslése

## Feladat
Próbáld megjósolni egy sör átlagos ratingjét.

## Input feature-ök
- style
- ABV
- IBU
- brewery country
- rating count
- seasonality
- adjuncts

## Target
- globális rating
vagy
- saját rating

## Modellek
- Linear Regression
- Random Forest
- XGBoost
- LightGBM
- Neural Network

## Mit tanulsz?
- feature engineering
- categorical encoding
- interpretability
- feature importance

---

# 2. Recommender System

## Feladat
„Milyen sört ajánljunk a usernek?”

## Adat
User × Beer rating mátrix.

## Megközelítések

### Collaborative Filtering
- Matrix Factorization
- ALS
- SVD

### Content-Based
- style similarity
- flavor tags
- text embeddings

### Hybrid
Netflix-szerű recommendation rendszer.

## Tanulság
- sparse matrix kezelés
- embeddings
- recommendation metrics
- cold start problem

---

# 3. NLP — Review szövegek elemzése

## Feladatok

### Sentiment Analysis
Szöveg → rating.

### Topic Modeling
Milyen témák jelennek meg gyakran?
- citrus
- hoppy
- watery
- overpriced

### Embedding alapú clustering
Ízprofilok csoportosítása.

## Eszközök
- TF-IDF
- BERT
- sentence-transformers
- LDA

---

# 4. Clustering

## Feladat
Csoportosíts söröket feature-ök alapján.

## Feature space
- ABV
- IBU
- style
- review embeddings
- aroma descriptors

## Algoritmusok
- KMeans
- HDBSCAN
- Hierarchical Clustering

## Vizualizáció
- PCA
- t-SNE
- UMAP

---

# 5. Time Series / Trend Prediction

## Feladatok

### Szezonális trendek
- télen stout
- nyáron sour vagy lager

### Brewery popularity prediction
Mely brewery-k trendelnek?

### Hype detection
Virális sörök korai felismerése.

## Modellek
- Prophet
- ARIMA
- LSTM
- Temporal XGBoost

---

# 6. Ranking Model

## Feladat
Ne abszolút ratinget jósolj, hanem:
„User A jobban fogja szeretni X-et mint Y-t?”

## Modellek
- Pairwise Ranking
- LambdaMART
- XGBoost Ranking

---

# 7. Fraud / Anomaly Detection

## Példák
- rating brigading
- brewery self-promotion
- bot activity
- irreálisan gyors check-in-ek

## Modellek
- Isolation Forest
- LOF
- Autoencoder

---

# 8. Graph ML

## Graph struktúra
- user ↔ beer
- brewery ↔ style
- user ↔ user

## Feladatok
- link prediction
- recommendation
- community detection

## Technológiák
- PyTorch Geometric
- DGL

---

# 9. Feature Engineering Projekt

## Példák
- style rarity
- brewery reputation
- weighted rating
- recency decay
- country popularity
- review entropy

## Mit tanulsz?
- leakage elkerülése
- validation
- feature pipelines

---

# 10. Dashboard + ML Deployment

## Stack
- Python
- FastAPI
- Streamlit
- Docker
- PostgreSQL

## Példa
„Adj meg 3 kedvenc sört és ajánlok újakat.”

---

# Beginner → Advanced Roadmap

## Beginner
1. EDA
2. Rating prediction
3. Clustering

## Intermediate
4. NLP
5. Recommender system
6. Ranking

## Advanced
7. Graph neural networks
8. Real-time recommendation
9. MLOps deployment

---

# Konkrét Projektötletek

## „Can I predict my own beer taste?”
Saját ratingek predikciója.

## „Hidden Gem Detector”
Kevés ratinggel rendelkező, de magas predicted score-os sörök keresése.

## „Beer Genome Project”
Embedding alapú hasonlóságkeresés.

## „Style Drift Analysis”
IPA-k és más stílusok változásának elemzése időben.

---

# Technikai Stack Javaslat

## Kezdéshez
- pandas
- scikit-learn
- matplotlib
- seaborn
- xgboost

## Haladó
- PyTorch
- LightGBM
- sentence-transformers
- implicit
- surprise

---

# Amit Recruiterek Értékelnek

Nem az számít leginkább, hogy deep learning-et használsz-e, hanem:
- tiszta pipeline
- jó feature engineering
- helyes validation
- interpretability
- üzleti gondolkodás
- reprodukálhatóság

Egy jól megcsinált Untappd recommendation vagy NLP projekt teljesen legitim portfolio-anyag data science és machine learning irányba.
"""

path = Path("/mnt/data/untappd_ml_otletek.md")
path.write_text(content, encoding="utf-8")

print(f"Markdown file saved to: {path}")

