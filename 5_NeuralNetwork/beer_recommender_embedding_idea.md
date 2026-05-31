# Neural háló alapú sörajánló rendszer -- elméleti felépítés

Szerintem ez a legizgalmasabb irány a projektedben.

A feladatod ilyenkor nem az, hogy egy sör stílusát vagy ratingjét
jósolod meg, hanem hogy megtanulod:

> "Mit jelent az, hogy két sör hasonló?"

Ez már reprezentációtanulás (representation learning) probléma.

## Az alapötlet

Tegyük fel, hogy minden sörhöz van 40 feature-öd:

-   ABV
-   IBU
-   Global Rating
-   ...
-   19 style feature
-   ...

Jelenleg egy sör egy 40 dimenziós vektor.

A cél:

40 feature → Neural Network → 8 dimenziós embedding

Például:

-   Guinness → \[0.2, -1.3, 0.8, ..., 0.5\]
-   Dragon's Milk → \[0.1, -1.1, 0.7, ..., 0.4\]

Mivel hasonló sörök, közel kerülnek egymáshoz az embedding térben.

## Hogyan lesz ebből ajánló?

A felhasználó megadja:

-   Guinness
-   KBS
-   Dragon's Milk
-   Old Rasputin
-   Founders Porter

Megkeresed az embeddingjeiket:

-   e1
-   e2
-   e3
-   e4
-   e5

Átlagolod:

user_taste = (e1 + e2 + e3 + e4 + e5) / 5

Ez lesz a „sörízlés-vektor".

Utána minden sörre kiszámolod a hasonlóságot (pl. cosine similarity), és
a legközelebbi söröket ajánlod.

## A nagy kérdés

Hogyan tanulja meg a háló ezt az embeddinget?

Ez a nehéz rész.

## 1. Autoencoder

Ez a legegyszerűbb megoldás.

### Encoder

40 → 32 → 16 → 8

### Decoder

8 → 16 → 32 → 40

A háló feladata:

-   bemenet = beer feature vector
-   kimenet = ugyanaz a beer feature vector

Tanulás közben az encoder kénytelen tömöríteni az információt, és a
lényeges mintázatokat megtartani.

A végén az encoder 8 dimenziós kimenete lesz az embedding.

## 2. Sokkal jobb: Siamese Network

Ez lenne a „profi" megoldás.

A háló bemenete:

-   Beer A
-   Beer B

Kimenet:

-   hasonló?
-   igen/nem

Példák:

-   Imperial Stout -- Porter → hasonló
-   Imperial Stout -- Pilsner → nem hasonló

A háló megtanulja, hogy milyen feature-ök számítanak igazán a hasonlóság
szempontjából.

A végén az embedding space sokkal jobb lesz.

## De honnan lesznek a „hasonló" címkék?

Mivel nincs user history, ez a kulcskérdés.

Lehet generálni mesterségesen:

-   azonos style → pozitív pár
-   nagyon eltérő style → negatív pár

Vagy:

-   kicsi rating különbség
-   kicsi feature távolság

→ pozitív pár

## Amit én csinálnék

### V1

Autoencoder

Mert:

-   egyszerű
-   kevés adat is elég
-   nincs szükség címkére

### V2

Beer embedding

### V3

Ajánló

5 kedvenc sör → embeddingek átlaga → cosine similarity → top 10
legközelebbi sör

## Miért tetszik ez a projektötlet?

Mert nem azt mondja:

> "Ez egy IPA."

hanem azt:

> "Ha szereted a KBS-t és az Old Rasputint, akkor valószínűleg szeretni
> fogod ezt a kevésbé ismert imperial stoutot is."

Ez már valódi ajánlórendszer-logika, és nagyon jól illik egy sörös ML
hobbiprojekthez.

A jelenlegi adataid valószínűleg már elegendőek egy első autoencoderes
beer-embedding modell felépítéséhez.
