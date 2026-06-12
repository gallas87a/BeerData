from difflib import SequenceMatcher
import csv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
import streamlit as st

def read_csvs(csv_location):
    i = 1

    while True:
        filename = os.path.join(csv_location, f"BeerEmbeddings{i}.csv")

        if not os.path.exists(filename):
            break

        print(f"Reading {filename}")

        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader) #header elimination
            for row in reader:
                emb_data.append(row)
        i += 1
    if streamlit_var:
        st.write(f"Loaded {len(emb_data)} rows from {i-1} files.")
    else:
        print(f"Loaded {len(emb_data)} rows from {i-1} files.")
    
    return emb_data

streamlit_var = True
if os.environ.get("OPENAI_API_KEY"):
    streamlit_var = False
    
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
    pref_beer = st.text_input("Please provide the name of the name of the beer: ")
else:
    pref_beer = input("Please provide the name of the name of the beer: ")

choice = 0
best_sim=0
count=0
same=0
eq_beer=[]
ids=[]
for i, text in enumerate(beer_data):
    if pref_beer.lower() == text[2].lower():
        count=1
        ids.append(i)
        eq_beer.append(text[1] + " : " + text[2])
        same=same+1

if same>1:
    if streamlit_var:
        st.write("Please select which beer you wanted to choose!\n")
    else:
        print("Please select which beer you wanted to choose!\n")

    for i,eq in enumerate(eq_beer):
        if streamlit_var:
            st.write("Name fully matching with",i,eq, ids[i])
        else:
            print("Name fully matching with",i,eq, ids[i])
    while True:
        try:
            if streamlit_var:
                choice = int(st.number_input("Choose a beer by entering the number: "))
            else:
                choice = int(input("Choose a beer by entering the number: "))
            if 0 <= choice <= len(eq_beer)-1:
                break
            if streamlit_var:
                st.write(f"Please enter a number between 0 and {len(eq_beer)-1}!")
            else:
                print(f"Please enter a number between 0 and {len(eq_beer)-1}!")
        except ValueError:
            if streamlit_var:
                st.write("Please enter a valid integer!")
            else:
                print("Please enter a valid integer!")
else:
    choice=0

if ids:
    for i, text in enumerate(beer_data):
        if i==ids[choice]:
            best_text=text[2]
            best_brewery=text[1]
            best_sim=1
            best_idx = i
else:
    pass #do nothing

while True:
    try:
        if streamlit_var:
            top_k = int(st.input("How many similar beers you want to see: "))
        else:
            top_k = int(input("How many similar beers you want to see: "))
        if 5 <= top_k <= 20: #arbitrary maximized in 20
            break
        if streamlit_var:
            st.write(f"Please enter a number between 5 and 20!")
        else:
            print(f"Please enter a number between 5 and 20!")
    except ValueError:
        if streamlit_var:
            st.write("Please enter a valid integer!")
        else:
            print("Please enter a valid integer!")

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
        st.write("I cannot find the choosen beer!")
    else:
        print("I cannot find the choosen beer!")
else:
    if streamlit_var:
        st.write(f"Index: {best_idx}")
        st.write(f"Similarity: {best_sim:.3f}")
        st.write(f"The name of the choosen beer: {best_text}")
        st.write(f"Brewery of the choosen beer: {best_brewery}\n")
    else:
        print(f"Index: {best_idx}")
        print(f"Similarity: {best_sim:.3f}")
        print(f"The name of the choosen beer: {best_text}")
        print(f"Brewery of the choosen beer: {best_brewery}\n")
    pref_beer=best_text
    
#CSV reading
emb_data=[]
emb_data = read_csvs(csv_location)
    
#cosine similarity
emb_data = np.array(emb_data, dtype=np.float32) #necessary conversion

pref = emb_data[best_idx].reshape(1, -1)
similarities = cosine_similarity(pref, emb_data)[0]

top_idx = np.argsort(similarities)[::-1] 
top_idx = top_idx[top_idx != (best_idx)][:top_k]

for i in top_idx:
    if streamlit_var:
        st.write(i, similarities[i],beer_data[i])
        st.write("\n")
    else:
        print(i, similarities[i],beer_data[i])
        print("\n")