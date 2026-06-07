from difflib import SequenceMatcher
import csv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
import streamlit as st

beer_data=[]
with open("/mount/src/beerdata/5_NeuralNetwork/BeerData.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader) # remove header
    for row in reader:
        beer_data.append(row)

#get user beer preference
pref_beer = st.text_input("Add meg a sör nevét: ")

best_sim=0
count=0
for i, text in enumerate(beer_data):
    if pref_beer.lower() == text[2].lower():
        st.write(i,text[2],"Full matching of the beer name!!! \n")
        count=1
        best_sim=1
        best_idx = i
        best_text=text[2]
        best_brewery=text[1]
        break
    else:
        sim = SequenceMatcher(None, text[2].lower(), pref_beer.lower()).ratio()  
        if sim > best_sim:
            best_sim = sim
            best_idx = i
            best_text=text[2]
            best_brewery=text[1]
    
if (count==0 and best_sim<0.5) :     #0.5 is arbitrary
    st.write("nem találtam a kiválasztott sört")
else:
    st.write(f"Index: {best_idx}")
    st.write(f"Similarity: {best_sim:.3f}")
    st.write(f"A kiválasztott sör neve: {best_text}")
    st.write(f"A kiválasztott sör gyártója: {best_brewery}")
    pref_beer=best_text
    
#CSV reading
emb_data=[]
with open("/mount/src/beerdata/5_NeuralNetwork/BeerEmbeddings.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader) # remove header
    for row in reader:
        emb_data.append(row)
    
    #cosine similarity
    emb_data = np.array(emb_data, dtype=np.float32) #necessary conversion
    
    pref = emb_data[best_idx].reshape(1, -1)
    similarities = cosine_similarity(pref, emb_data)[0]
    top_k = 5
    top_idx = np.argsort(similarities)[::-1] 
    top_idx = top_idx[top_idx != (best_idx)][:top_k]
    st.write(top_idx,"\n")
    for i in top_idx:
        st.write(i, similarities[i],beer_data[i])
        st.write("\n")