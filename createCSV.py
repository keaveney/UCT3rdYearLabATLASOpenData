import pandas as pd
import uproot

listofdataframes = []

listoffiles = ["data_A.GamGam.root",
               "data_B.GamGam.root",
               "data_C.GamGam.root",
               "data_D.GamGam.root"
    ]

for arrays in uproot.iterate(listoffiles, "mini", ["photon_pt", "photon_eta", "photon_phi", "photon_E", "photon_eta", "photon_isTightID","photon_etcone20","photon_ptcone30", "trigP","photon_trigMatched"], outputtype=pd.DataFrame):
         listofdataframes.append(arrays)


skimFile = uproot.recreate("data_preSel.root", compression=None)


#df.to_csv('data_A.GamGam.csv')
