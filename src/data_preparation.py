import pandas as pd
import numpy as np


df = pd.read_csv("data/liensVilles.csv", dtype='unicode')
df_auto = pd.read_csv("data/auto.csv")
df_chomage = pd.read_csv("data/chomage.csv")
df_csp = pd.read_csv("data/csp.csv")
df_del = pd.read_csv("data/delinquance.csv")
df_demo = pd.read_csv("data/demographie.csv", dtype='unicode')
df_elections = pd.read_csv("data/elections.csv", dtype='unicode')
df_emploi = pd.read_csv("data/emploi.csv")
df_entreprises = pd.read_csv("data/entreprises.csv")
df_immo = pd.read_csv("data/immobilier.csv")
df_infos = pd.read_csv("data/infos.csv", dtype='unicode')
df_salaires = pd.read_csv("data/salaires.csv")
df_sante = pd.read_csv("data/santeSocial.csv", dtype='unicode')
df_candidats = pd.read_csv("data/candidats_2019.csv")
