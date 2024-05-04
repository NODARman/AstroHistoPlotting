import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import time
import sys
import os
from matplotlib.patches import Rectangle
from google.colab import files
from google.colab import runtime
from astropy.io import fits

### Pull data from the Excel file (must be .xlsx) ###
def Santos1(): #Santos 1 - 15 640 KM stars + Radius.xlsx
  global read_file
  global graph_info
  global file_info
  read_file = pd.read_excel('/content/drive/MyDrive/file_name.xlsx') # Mount drive in Colab and change 'file_name.xlsx' with your file name
  graph_info = "\n(Catalogue: KSPC DR25. Total: 15 640 KM stars. Santos 1)" # Seconday (non-changing) title (additional info) of the graphs
  file_info = " - KSPC DR25 - 15 640 KM - Santos 1" # Saved graphs names

def save_graphs(graph_name): # Save graphs
  plt.savefig(graph_name + ".png")
  files.download(graph_name + ".png")
  return

Santos1()

# This array contains values from the Excel file (you may change (or delete) names of the columns)
primaryArray = [read_file['KIC'].to_numpy(),
                read_file['logg'].to_numpy(),
                read_file['Teff'].to_numpy(),
                read_file['Mass'].to_numpy(),
                read_file['Radius'].to_numpy(),
                read_file['Prot'].to_numpy()]

''' Example intervals (in my case) Fast [0-10], Medium [10-20], Slow [20-30], Very slow [30+] <days> '''
# sorted array
dataArray = [[[],[],[],[]], # 0 logg (period): [0-10],[10-20],[20-30],[30+]
             [[],[],[],[]], # 1 Teff (period): [0-10],[10-20],[20-30],[30+]
             [[],[],[],[]], # 2 Mass (period): [0-10],[10-20],[20-30],[30+]
             [[],[],[],[]]] # 3 Radi (period): [0-10],[10-20],[20-30],[30+]

RemovedKIC = [[],[],[],[],[],[]]
a = []

n=0
for index, item in enumerate(primaryArray[5]): # Prot array cycle
  index -= n

  def append_removed():
    n += 1
    for i in range(0,6):
      # KIC, logg, Teff, Mass, Radius, Prot
      RemovedKIC[i].append(primaryArray[i][index])
      #np.delete(primaryArray[i], index)

  def Add(j):
    for i in range(0,4):
      dataArray[i][j].append(float(primaryArray[i+1][index])) # i+1, because in 'primaryArray' logg is the second one

  if not math.isnan(item):
    try:
      if float(primaryArray[4][index]) < 100 or (item != "Nan" and item != "none" and item != 'None'): # Filter by Radius

        # Sort by Prot
        if item < 10:
          Add(0)
        elif item >= 10 and item <= 20:
          Add(1)
        elif item > 20 and item <= 30:
          Add(2)
        elif item > 30:
          Add(3)

      else:
        append_removed()
    except:
      append_removed()
  else:
    append_removed()

### plot graphs (and arrays of strings for loops) ###
titles = ['Period histogram', 'log(g) histo by period',
          'Teff histo by period', 'Mass histo by period',
          'Radius histo by period', ' (combined) ', ' (sequential graphs) ']

labels = ['period [day]', 'sequential number', 'quantity', 'sun's log(g)', 'Kelvin', 'solar mass', 'solar radius']
sublabels = ['period: <10 days', 'period: 10-20', 'period: 20-30 days', 'period: 30+ days']

comb = [[0,0], #combination
        [0,1],
        [1,0],
        [1,1]]

binA = [[8], # 8 parts
        [0,5,10,15,20,25,30,35,40,45,50, max(primaryArray[5])], # Prot: a lot of parts, combined at the end
        [np.linspace(min(primaryArray[5]), max(primaryArray[5]), 8)], # Prot

        [np.linspace(min(primaryArray[1]), max(primaryArray[1]), 11)], # logg
        [np.linspace(4500, 7500, 12).ravel().tolist()], # Teff
        [np.linspace(min(primaryArray[3]), max(primaryArray[3]), 11)], # Mass
        [np.linspace(min(primaryArray[4]), max(primaryArray[4]), 11)], # Radius

        [{'color':'black','alpha':float('1')}, {'color':'#6b86ff','alpha':float('0.7')}, {'color':'#6ba5ff','alpha':float('0.5')}, {'color':'#96bfff','alpha':float('1')}], # logg colors
        [{'color':'#540000','alpha':float('1')}, {'color':'#eb4600','alpha':float('0.5')}, {'color':'#ff9f05','alpha':float('0.5')}, {'fill':False,'alpha':float('1')}], # Teff colors
        [{'color':'#003015','alpha':float('1')}, {'color':'#00fcbd','alpha':float('0.5')}, {'color':'#00ff08','alpha':float('0.5')}, {'color':'black','fill':False,'alpha':float('1')}], # Mass colors
        [{'color':'#002927','alpha':float('1')}, {'color':'#00cc6d','alpha':float('0.5')}, {'color':'#00ffd0','alpha':float('0.5')}, {'color':'black','fill':False,'alpha':float('1')}]] # Radius colors

### simple graphs ###
def Graphics():
  plt.autoscale()
  for h in range(5):
    plt.title(titles[h] + graph_info)
    plt.xlabel(labels[1])

    if h == 0:
      plt.xlabel(labels[h+2])
      plt.ylabel(labels[h+2])
      plt.hist(primaryArray[5], binA[0][0], rwidth=0.8) # Prot histogram
      save_graphs(str(h) + '. ' + titles[h] + file_info)
    else:
      plt.ylabel(labels[h+2])
      plt.plot(primaryArray[h], "o", color="black", markersize=1) # sequential number
      save_graphs(str(h) + '. ' + titles[h] + titles[6] + file_info)

    plt.show()
    print('\n')
  time.sleep(1)
Graphics()

### quadruple graphs ###
def Histograms():
  for g in range(4):
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10)) # Define a 2x2 grid of subplots
    nA=[]
    fig.suptitle(titles[g+1] + graph_info)
    for h in range(4):
      axs[comb[h][0], comb[h][1]].set_xlabel(labels[g+3])
      axs[comb[h][0], comb[h][1]].set_ylabel(labels[2])
      n, bins, patches = axs[comb[h][0], comb[h][1]].hist(dataArray[g][h], binA[g+3][0], rwidth=0.8, **binA[g+7][h], edgecolor="black", label=sublabels[h])
      axs[comb[h][0], comb[h][1]].legend()

      nA.append(n)
    maxval = max(max(sublist) for sublist in nA)
    for h in range(4):
      v = maxval + maxval/10
      axs[comb[h][0], comb[h][1]].set_ylim([0, v])

    fig.tight_layout() # Adjust the spacing between subplots

    save_graphs(str(g+1) + '. ' + titles[g+1] + file_info)
    plt.show()
    print('\n')
  time.sleep(1)
Histograms()

### combined quadruple graphs ###
def HistogramsComb():
  for g in range(4):
    for h in range(4):
      plt.xlabel(labels[g+3])
      plt.ylabel(labels[2])
      plt.title(titles[g+1] + titles[5] + graph_info)
      plt.hist(dataArray[g][h], binA[g+3][0], rwidth = 1 - (h+1)*0.1, **binA[g+7][h], edgecolor="black", label=sublabels[h])
    plt.legend()

    save_graphs(str(g+1) + '. ' + titles[g+1] + titles[5] + file_info)
    plt.show()
    print('\n')
  time.sleep(1)
HistogramsComb()

if not all(len(inner_list) == 0 for inner_list in RemovedKIC):
  print("removed stars:")
  print("KIC:", RemovedKIC[0], "\nlogg:", RemovedKIC[1], "\nTeff:", RemovedKIC[2], "\nMass:", RemovedKIC[3], "\nRadius:", RemovedKIC[4], "\nProt:", RemovedKIC[5])
  txtt = "KIC:" + str(RemovedKIC[0]) + "\nlogg:" + str(RemovedKIC[1]) + "\nTeff:" + str(RemovedKIC[2]) + "\nMass:" + str(RemovedKIC[3]) + "\nRadius:" + str(RemovedKIC[4]) + "\nProt:" + str(RemovedKIC[5])

  with open(f'removed stars{file_info}.txt', 'w') as file: # Open a new file in write mode
    file.write(txtt) # Write a message to the file
  #files.download(f"removed stars{fileInfo}.txt") # autoDOWNLOAD
  print('File created successfully.')
else:
  print("all stars are used")
