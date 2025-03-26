import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def load_data():
    data = pd.read_csv("data/BeansDataSet.csv")  
    return data

df = load_data()


st.title(" Analyse des Ventes - Beans & Pods")



st.markdown("""
 
Ce projet  permet d'analyser les données de vente de différents types de café, selon le canal de vente et la région.

""")


st.sidebar.header(" Filtres")
channel = st.sidebar.selectbox("Sélectionner le canal", df["Channel"].unique())
region = st.sidebar.selectbox("Sélectionner la région", df["Region"].unique())

donnee_filtre = df[(df["Channel"] == channel) & (df["Region"] == region)]


st.subheader("Aperçu des données filtrées")
st.dataframe(donnee_filtre.head())


st.subheader(" Ventes par type de café")
categories = ["Robusta", "Arabica", "Espresso", "Lungo", "Latte", "Cappuccino"]
melted_df = donnee_filtre.melt(id_vars=["Channel", "Region"], value_vars=categories, var_name="Type de café", value_name="Ventes")

fig, ax = plt.subplots()
melted_df.groupby("Type de café")["Ventes"].sum().plot(kind="bar", ax=ax, color=['blue', 'green', 'red', 'purple', 'orange', 'brown'])
ax.set_title("Répartition des ventes par type de café")
ax.set_ylabel("Ventes")
st.pyplot(fig)


st.subheader("Histogramme des ventes")
fig, ax = plt.subplots()
ax.hist(melted_df["Ventes"], bins=20, color='skyblue', edgecolor='black')
ax.set_title("Distribution des ventes")
ax.set_xlabel("Ventes")
ax.set_ylabel("Fréquence")
st.pyplot(fig)


st.subheader(" Boîtes à moustaches des ventes")
fig, ax = plt.subplots()
sns.boxplot(x="Type de café", y="Ventes", data=melted_df, ax=ax)
ax.set_title("Analyse des ventes par type de café")
ax.set_ylabel("Ventes")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)


st.subheader(" Statistiques des ventes")
st.write("**Total des ventes :**", donnee_filtre[categories].sum().sum())
st.write("**Moyenne des ventes par type de café :**")
st.dataframe(donnee_filtre[categories].mean())

st.write("**Médiane des ventes par type de café :**")
st.dataframe(donnee_filtre[categories].median())

st.write("**Écart-type des ventes par type de café :**")
st.dataframe(donnee_filtre[categories].std())

st.write("**Variance des ventes par type de café :**")
st.dataframe(donnee_filtre[categories].var())

st.write("**Étendue des ventes par type de café :**")
st.dataframe(donnee_filtre[categories].apply(lambda x: x.max() - x.min()))


st.subheader("Corrélations entre les types de café")
corr_matrix = donnee_filtre[categories].corr()
st.write("**Matrice de corrélation :**")
st.dataframe(corr_matrix)


fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)

st.pyplot(fig)

# Conclusion
st.subheader("analyse et recommandations")
st.markdown("""
**Moyennes et variances des ventes par produit :**
            

Les grains de café (Robusta et Arabica) montrent des ventes moyennes plus élevées que les gousses (Lungo, Latte, Cappuccino, Espresso), suggérant une préférence pour les produits non transformés.
Les variances des gousses, en particulier Cappuccino et Latte, sont élevées, ce qui indique des écarts significatifs dans les performances de vente par région et par canal.

Corrélations entre les produits :
            
Les ventes de Robusta et Arabica présentent une forte corrélation, montrant que les deux types de grains de café sont souvent achetés ensemble.
Les gousses comme Espresso et Lungo montrent des corrélations modérées.
            
Régions et canaux performants :
Les ventes en ligne dépassent légèrement celles en magasin, indiquant un potentiel croissant pour le commerce électronique.
La région Nord enregistre les ventes totales les plus élevées, tandis que la région Sud montre une variabilité plus importante.
La région Nord domine en termes de ventes totales. Elle affiche les meilleurs résultats pour les grains de café, notamment Robusta et Arabica, ainsi que pour certaines gousses comme le Latte.

            
selon l'histogramme des ventes pour etudier la distribution des ventes,Les ventes de Robusta et Arabica ont une distribution concentrée autour de valeurs élevées, indiquant qu’ils sont régulièrement vendus en grandes quantités.
Les ventes des gousses comme Lungo et Cappuccino montrent une distribution plus étendue, ce qui suggère une variabilité importante entre les régions et les canaux.Les produits Robusta et Arabica bénéficient d’une demande stable et homogène, ce qui en fait les piliers de l’offre.
            

D'apres la boite a mousatche,Les ventes de Robusta et Arabica ont une plage interquartile relativement étroite, indiquant une faible dispersion des ventes.
En revanche, des produits comme Latte et Cappuccino montrent une dispersion plus large et des valeurs extrêmes, suggérant des différences  entre les régions ou les canaux.

            

Recommandations pour la campagne marketing
            
Personne ciblées :
Les campagnes devraient se concentrer sur la région Nord pour capitaliser sur les ventes élevées.
Investissir dans le canal en ligne, particulièrement pour Robusta et Arabica.
Promotion croisée :	Proposez des offres combinées pour Robusta et Arabica pour augmenter les volumes.
Encouragez la diversification des achats avec des promotions sur les gousses (comme Espresso ou Latte) pour équilibrer les ventes.
            

Suggestions pour collecter des données supplémentaires
        
            

Comportements des clients : Ajoutez des données sur les préférences des clients, comme leur fréquence d’achat ou leurs types de produits préférés.
Durée et saisonnalité : Intégrez des données sur les périodes de vente pour comprendre les tendances saisonnières.
Marketing et retours : Collectez des données sur l’efficacité des campagnes marketing et les retours des clients.


""")
