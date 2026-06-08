from difflib import SequenceMatcher
import csv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
import streamlit as st

streamlit_var = True
if os.environ.get("OPENAI_API_KEY"):
    streamlit_var = False
    print(streamlit_var)
    
beer_data=[]
if streamlit_var:
    csv_location = "/mount/src/beerdata/5_NeuralNetwork/"
else:
    csv_location = ""
    
with open(csv_location+"BeerData.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader) # remove header
    for row in reader:
        beer_data.append(row)

#get user beer preference
if streamlit_var:
    pref_beer = st.text_input("Add meg a sör nevét: ")
else:
    pref_beer = input("Add meg a sör nevét: ")

best_sim=0
count=0
same=0
eq_beer=[]
ids=[]
for i, text in enumerate(beer_data):
    if pref_beer.lower() == text[2].lower():
        if streamlit_var:
            st.write(i,text[2],"Full matching of the beer name!!! \n")
        else:
            print(i,text[2],"Full matching of the beer name!!! \n")
        count=1
        ids.append(i)
        eq_beer.append(text[1] + " : " + text[2])
        same=same+1

print("Please select which beer you wanted to choose!\n")
for i,eq in enumerate(eq_beer):
    print("Name fully matching with",i,eq, ids[i])
while True:
    try:
        choice = int(input("Choose a beer by entering the number: "))
        if 0 <= choice <= len(eq_beer)-1:
            break
        print(f"Please enter a number between 0 and {len(eq_beer)-1}.")
    except ValueError:
        print("Please enter a valid integer.")

for i, text in enumerate(beer_data):
    if i==ids[choice]:
        best_text=text[2]
        best_brewery=text[1]
        best_sim=1
        best_idx = i

for i, text in enumerate(beer_data):    
    if count == 0:
        sim = SequenceMatcher(None, text[2].lower(), pref_beer.lower()).ratio()  
        if sim > best_sim:
            best_sim = sim
            best_idx = i
            best_text=text[2]
            best_brewery=text[1]

if (count==0 and best_sim<0.5) :     #0.5 is arbitrary
    if streamlit_var:
        st.write("nem találtam a kiválasztott sört")
    else:
        print("nem találtam a kiválasztott sört")
else:
    if streamlit_var:
        st.write(f"Index: {best_idx}")
        st.write(f"Similarity: {best_sim:.3f}")
        st.write(f"A kiválasztott sör neve: {best_text}")
        st.write(f"A kiválasztott sör gyártója: {best_brewery}")
    else:
        print(f"Index: {best_idx}")
        print(f"Similarity: {best_sim:.3f}")
        print(f"A kiválasztott sör neve: {best_text}")
        print(f"A kiválasztott sör gyártója: {best_brewery}")
    pref_beer=best_text
    
#CSV reading
emb_data=[]
with open(csv_location+"BeerEmbeddings.csv","r",encoding="utf-8") as file:
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
    if streamlit_var:
        st.write(top_idx,"\n")
    else:
        print(top_idx,"\n")
    for i in top_idx:
        if streamlit_var:
            st.write(i, similarities[i],beer_data[i])
            st.write("\n")
        else:
            print(i, similarities[i],beer_data[i])
            print("\n")