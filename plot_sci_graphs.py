import pandas as pd
from astropy.io import fits
import os
from google.colab import files

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# Excel
df = pd.read_excel('KIC stars and data.xlsx')

# print the first column as an array
Prot = df['Prot'].to_numpy()
KIC = df['KIC'].to_numpy()
Mass = df['Mass'].to_numpy()
logg = df['log(g)'].to_numpy()
Teff = df['Teff'].to_numpy()
Radius = df['Radius'].to_numpy()

"""
print(Prot)
print(KIC)
print(Mass)
print(logg)
print(Teff)"""



################################################################################

file_name = "txt.txt"

a = []

###########################################################################

#plt.figure(figsize=(13,8))

# Fast 0-10, Medium 10-20, Small 20-30, Very Small 30+

inp1 = input("Auto download every graph (.png). y/n >>>   ")

def save_graphs(graph_name):
  plt.savefig(graph_name + ".png")
  if inp1 == "y" or inp1 == "Y":
    files.download(graph_name + ".png")

  return



target_array_logg_0010 = []
target_array_logg_1020 = []
target_array_logg_2030 = []
target_array_logg_3099 = []

target_array_Teff_0010 = []
target_array_Teff_1020 = []
target_array_Teff_2030 = []
target_array_Teff_3099 = []

target_array_Mass_0010 = []
target_array_Mass_1020 = []
target_array_Mass_2030 = []
target_array_Mass_3099 = []

target_array_Radius_0010 = []
target_array_Radius_1020 = []
target_array_Radius_2030 = []
target_array_Radius_3099 = []

for index, item in enumerate(Prot):
  if item < 10:
    target_array_logg_0010.append(logg[index])
    target_array_Teff_0010.append(Teff[index])
    target_array_Mass_0010.append(Mass[index])
    target_array_Radius_0010.append(Radius[index])
  elif item >= 10 and item <= 20:
    target_array_logg_1020.append(logg[index])
    target_array_Teff_1020.append(Teff[index])
    target_array_Mass_1020.append(Mass[index])
    target_array_Radius_1020.append(Radius[index])
  elif item > 20 and item <= 30:
    target_array_logg_2030.append(logg[index])
    target_array_Teff_2030.append(Teff[index])
    target_array_Mass_2030.append(Mass[index])
    target_array_Radius_2030.append(Radius[index])
  elif item > 30:
    target_array_logg_3099.append(logg[index])
    target_array_Teff_3099.append(Teff[index])
    target_array_Mass_3099.append(Mass[index])
    target_array_Radius_3099.append(Radius[index])



############# --- Prot --- #############

H0 = np.linspace(min(Prot), max(Prot), 8)

plt.xlabel("Period (Days)")
plt.ylabel("Quantity")
plt.title("Histogram of period")
plt.hist(Prot, H0, rwidth=0.8)

save_graphs("0. Prot histogram") # image name

plt.show()


##########
print("\n")






##############################################
plt.title("Effective temperature graph")
plt.plot(Teff, "o", color="black", markersize=1)
plt.xlabel("Numeric number")
plt.ylabel("Kelvin")
plt.autoscale()
save_graphs("1. Teff numerical graph") # image name
plt.show()

plt.title("logg graph")
plt.plot(logg, "o", color="black", markersize=1)
plt.xlabel("Numeric number")
plt.ylabel("logg")
plt.autoscale()
save_graphs("2. logg Numeric graph") # image name
plt.show()

plt.title("Mass graph")
plt.plot(Mass, "o", color="black", markersize=1)
plt.xlabel("Numeric number")
plt.ylabel("Solar mass")
plt.autoscale()
save_graphs("3. Mass Numeric graph") # image name
plt.show()

plt.title("Radius graph")
plt.plot(Radius, "o", color="black", markersize=1)
plt.xlabel("Numeric number")
plt.ylabel("Solar radius")
plt.autoscale()
save_graphs("4. Radius Numeric graph") # image name
plt.show()












############# --- Teff --- #############
def TEFF():
  # Define a 2x2 grid of subplots
  fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

  fig.suptitle("Effective temperature histogram by period")

  H = np.linspace(min(target_array_Teff_0010), max(target_array_Teff_0010), 8)
  axs[0, 0].set_xlabel("Kelvin")
  axs[0, 0].set_ylabel("Quantity")
  axs[0, 0].hist(target_array_Teff_0010, H, rwidth=0.8, color="#540000", edgecolor="black", alpha=1, label="Period <10 days")
  axs[0, 0].legend()

  H = np.linspace(min(target_array_Teff_1020), max(target_array_Teff_1020), 8)
  axs[0, 1].set_xlabel("Kelvin")
  axs[0, 1].set_ylabel("Quantity")
  axs[0, 1].hist(target_array_Teff_1020, H, rwidth=0.8, color="#eb4600", edgecolor="black", alpha=0.5, label="Period 10-20 days")
  axs[0, 1].legend()

  H = np.linspace(min(target_array_Teff_2030), max(target_array_Teff_2030), 8)
  axs[1, 0].set_xlabel("Kelvin")
  axs[1, 0].set_ylabel("Quantity")
  axs[1, 0].hist(target_array_Teff_2030, H, rwidth=0.8, fill=True, color="#ff9f05", edgecolor="black", alpha=0.5, label="Period 20-30 days")
  axs[1, 0].legend()

  H = np.linspace(min(target_array_Teff_3099), max(target_array_Teff_3099), 8)
  axs[1, 1].set_xlabel("Kelvin")
  axs[1, 1].set_ylabel("Quantity")
  axs[1, 1].hist(target_array_Teff_3099, H, rwidth=0.8, fill=False, edgecolor="black", alpha=1, label="Period >30 days")
  axs[1, 1].legend()

  # Adjust the spacing between subplots
  fig.tight_layout()

  save_graphs("1. Teff Separated histogram") # image name

  plt.show()

TEFF()
print("\n")

############# --- logg --- #############
def LOGG():
  # Define a 2x2 grid of subplots
  fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

  fig.suptitle("logg histogram by period")

  H = np.linspace(min(target_array_logg_0010), max(target_array_logg_0010), 8)
  axs[0, 0].set_xlabel("logg")
  axs[0, 0].set_ylabel("Quantity")
  axs[0, 0].hist(target_array_logg_0010, H, rwidth=0.8, color="black", edgecolor="black", alpha=1, label="Period <10 days")
  axs[0, 0].legend()

  H = np.linspace(min(target_array_logg_1020), max(target_array_logg_1020), 8)
  axs[0, 1].set_xlabel("logg")
  axs[0, 1].set_ylabel("Quantity")
  axs[0, 1].hist(target_array_logg_1020, H, rwidth=0.8, color="#6b86ff", edgecolor="black", alpha=0.7, label="Period 10-20 days")
  axs[0, 1].legend()

  H = np.linspace(min(target_array_logg_2030), max(target_array_logg_2030), 8)
  axs[1, 0].set_xlabel("logg")
  axs[1, 0].set_ylabel("Quantity")
  axs[1, 0].hist(target_array_logg_2030, H, rwidth=0.8, color="#6ba5ff", edgecolor="black", alpha=0.5, label="Period 20-30 days")
  axs[1, 0].legend()

  H = np.linspace(min(target_array_logg_3099), max(target_array_logg_3099), 8)
  axs[1, 1].set_xlabel("logg")
  axs[1, 1].set_ylabel("Quantity")
  axs[1, 1].hist(target_array_logg_3099, H, rwidth=0.8, color="#96bfff", edgecolor="black", alpha=1, label="Period >30 days")
  axs[1, 1].legend()

  # Adjust the spacing between subplots
  fig.tight_layout()

  save_graphs("2. logg Separated histogram") # image name

  plt.show()

LOGG()
print("\n")

############# --- Mass --- #############
def MASS():
  # Define a 2x2 grid of subplots
  fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

  fig.suptitle("Mass histogram by period")

  # Plot the histogram of target_array_Mass_0010 on the top-left subplot
  H = np.linspace(min(target_array_Mass_0010), max(target_array_Mass_0010), 8)
  axs[0, 0].set_xlabel("Solar mass")
  axs[0, 0].set_ylabel("Quantity")
  axs[0, 0].hist(target_array_Mass_0010, H, rwidth=0.8, color="#003015", edgecolor="black", alpha=1, label="Period <10 days")
  axs[0, 0].legend()

  # Plot the histogram of target_array_Mass_1020 on the top-right subplot
  H = np.linspace(min(target_array_Mass_1020), max(target_array_Mass_1020), 8)
  axs[0, 1].set_xlabel("Solar mass")
  axs[0, 1].set_ylabel("Quantity")
  axs[0, 1].hist(target_array_Mass_1020, H, rwidth=0.8, color="#00fcbd", edgecolor="black", alpha=0.5, label="Period 10-20 days")
  axs[0, 1].legend()

  # Plot the histogram of target_array_Mass_2030 on the bottom-left subplot
  H = np.linspace(min(target_array_Mass_2030), max(target_array_Mass_2030), 8)
  axs[1, 0].set_xlabel("Solar mass")
  axs[1, 0].set_ylabel("Quantity")
  axs[1, 0].hist(target_array_Mass_2030, H, rwidth=0.8, fill=True, color="#00ff08", edgecolor="black", alpha=0.5, label="Period 20-30 days")
  axs[1, 0].legend()

  # Plot the histogram of target_array_Mass_3099 on the bottom-right subplot
  H = np.linspace(min(target_array_Mass_3099), max(target_array_Mass_3099), 8)
  axs[1, 1].set_xlabel("Solar mass")
  axs[1, 1].set_ylabel("Quantity")
  axs[1, 1].hist(target_array_Mass_3099, H, rwidth=0.8, fill=False, edgecolor="black", alpha=1, label="Period >30 days")
  axs[1, 1].legend()

  # Adjust the spacing between subplots
  fig.tight_layout()

  save_graphs("3. Mass Separated histogram") # image name

  plt.show()

MASS()

############# --- Radius --- #############
def RADIUS():
  # Define a 2x2 grid of subplots
  fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

  fig.suptitle("Radius histogram by period")

  # Plot the histogram of target_array_Mass_0010 on the top-left subplot
  H = np.linspace(min(target_array_Radius_0010), max(target_array_Radius_0010), 8)
  axs[0, 0].set_xlabel("Solar radius")
  axs[0, 0].set_ylabel("Quantity")
  axs[0, 0].hist(target_array_Radius_0010, H, rwidth=0.8, color="#002927", edgecolor="black", alpha=1, label="Period <10 days")
  axs[0, 0].legend()

  # Plot the histogram of target_array_Mass_1020 on the top-right subplot
  H = np.linspace(min(target_array_Radius_1020), max(target_array_Radius_1020), 8)
  axs[0, 1].set_xlabel("Solar radius")
  axs[0, 1].set_ylabel("Quantity")
  axs[0, 1].hist(target_array_Radius_1020, H, rwidth=0.8, color="#00cc6d", edgecolor="black", alpha=0.5, label="Period 10-20 days")
  axs[0, 1].legend()

  # Plot the histogram of target_array_Mass_2030 on the bottom-left subplot
  H = np.linspace(min(target_array_Radius_2030), max(target_array_Radius_2030), 8)
  axs[1, 0].set_xlabel("Solar radius")
  axs[1, 0].set_ylabel("Quantity")
  axs[1, 0].hist(target_array_Radius_2030, H, rwidth=0.8, fill=True, color="#00ffd0", edgecolor="black", alpha=0.5, label="Period 20-30 days")
  axs[1, 0].legend()

  # Plot the histogram of target_array_Mass_3099 on the bottom-right subplot
  H = np.linspace(min(target_array_Radius_3099), max(target_array_Radius_3099), 8)
  axs[1, 1].set_xlabel("Solar radius")
  axs[1, 1].set_ylabel("Quantity")
  axs[1, 1].hist(target_array_Radius_3099, H, rwidth=0.8, fill=False, edgecolor="black", alpha=1, label="Period >30 days")
  axs[1, 1].legend()

  # Adjust the spacing between subplots
  fig.tight_layout()

  save_graphs("4. Radius Separated histogram") # image name

  plt.show()

RADIUS()


##############################################################
############ ----- Separated histograms ----- ############
##############################################################




############# --- Teff --- #############
def TEFFc():
  H = np.linspace(min(target_array_Teff_0010), max(target_array_Teff_0010), 8)
  plt.xlabel("Kelvin")
  plt.ylabel("Quantity")
  plt.hist(target_array_Teff_0010, H, rwidth=0.8, color="#540000", edgecolor="black", alpha=1, label="Period <10 days")

  H = np.linspace(min(target_array_Teff_1020), max(target_array_Teff_1020), 8)
  plt.xlabel("Kelvin")
  plt.ylabel("Quantity")
  plt.hist(target_array_Teff_1020, H, rwidth=0.8, color="#eb4600", edgecolor="black", alpha=0.5, label="Period 10-20 days")

  H = np.linspace(min(target_array_Teff_2030), max(target_array_Teff_2030), 8)
  plt.xlabel("Kelvin")
  plt.ylabel("Quantity")
  plt.hist(target_array_Teff_2030, H, rwidth=0.8, fill=True, color="#ff9f05", edgecolor="black", alpha=0.5, label="Period 20-30 days")

  H = np.linspace(min(target_array_Teff_3099), max(target_array_Teff_3099), 8)
  plt.xlabel("Kelvin")
  plt.ylabel("Quantity")
  plt.title("Effective temperature histogram by period (Combined)")
  plt.hist(target_array_Teff_3099, H, rwidth=0.8, fill=False, edgecolor="black", alpha=1, label="Period >30 days")

  plt.legend()

  save_graphs("1. Teff Combined histogram") # image name

  plt.show()

TEFFc()

def LOGGc():
  H = np.linspace(min(target_array_logg_0010), max(target_array_logg_0010), 8)
  plt.xlabel("logg")
  plt.ylabel("Quantity")

  plt.hist(target_array_logg_0010, H, rwidth=0.8, color="black", edgecolor="black", alpha=1, label="Period <10 days")
  #plt.show()

  H = np.linspace(min(target_array_logg_1020), max(target_array_logg_1020), 8)
  plt.xlabel("logg")
  plt.ylabel("Quantity")

  plt.hist(target_array_logg_1020, H, rwidth=0.8, color="#6b86ff", edgecolor="black", alpha=0.7, label="Period 10-20 days")
  #plt.show()

  H = np.linspace(min(target_array_logg_2030), max(target_array_logg_2030), 8)
  plt.xlabel("logg")
  plt.ylabel("Quantity")

  plt.hist(target_array_logg_2030, H, rwidth=0.8, color="#6ba5ff", edgecolor="black", alpha=0.5, label="Period 20-30 days")
  #plt.show()

  H = np.linspace(min(target_array_logg_3099), max(target_array_logg_3099), 8)
  plt.xlabel("logg")
  plt.ylabel("Quantity")
  plt.title("logg histogram by period (Combined)")
  plt.hist(target_array_logg_3099, H, rwidth=0.8, color="#96bfff", edgecolor="black", alpha=1, label="Period >30 days")

  plt.legend()

  save_graphs("2. logg Combined histogram") # image name

  plt.show()

LOGGc()

############# --- Mass --- #############
def MASSc():
  H = np.linspace(min(target_array_Mass_0010), max(target_array_Mass_0010), 8)
  plt.xlabel("Solar mass")
  plt.ylabel("Quantity")
  plt.hist(target_array_Mass_0010, H, rwidth=0.8, color="#003015", edgecolor="black", alpha=1, label="Period <10 days")

  H = np.linspace(min(target_array_Mass_1020), max(target_array_Mass_1020), 8)
  plt.xlabel("Solar mass")
  plt.ylabel("Quantity")
  plt.hist(target_array_Mass_1020, H, rwidth=0.8, color="#00fcbd", edgecolor="black", alpha=0.5, label="Period 10-20 days")

  H = np.linspace(min(target_array_Mass_2030), max(target_array_Mass_2030), 8)
  plt.xlabel("Solar mass")
  plt.ylabel("Quantity")
  plt.hist(target_array_Mass_2030, H, rwidth=0.8, fill=True, color="#00ff08", edgecolor="black", alpha=0.5, label="Period 20-30 days")

  H = np.linspace(min(target_array_Mass_3099), max(target_array_Mass_3099), 8)
  plt.xlabel("Solar mass")
  plt.ylabel("Quantity")
  plt.title("Mass histogram by period (Combined)")
  plt.hist(target_array_Mass_3099, H, rwidth=0.8, fill=False, edgecolor="black", alpha=1, label="Period >30 days")

  plt.legend()

  save_graphs("3. Mass Combined histogram") # image name

  plt.show()

MASSc()

############# --- Mass --- #############
def RADIUSc():
  H = np.linspace(min(target_array_Radius_0010), max(target_array_Radius_0010), 8)
  plt.xlabel("Solar radius")
  plt.ylabel("Quantity")
  plt.hist(target_array_Radius_0010, H, rwidth=0.8, color="#002927", edgecolor="black", alpha=1, label="Period <10 days")

  H = np.linspace(min(target_array_Radius_1020), max(target_array_Radius_1020), 8)
  plt.xlabel("Solar radius")
  plt.ylabel("Quantity")
  plt.hist(target_array_Radius_1020, H, rwidth=0.8, color="#00cc6d", edgecolor="black", alpha=0.5, label="Period 10-20 days")

  H = np.linspace(min(target_array_Radius_2030), max(target_array_Radius_2030), 8)
  plt.xlabel("Solar radius")
  plt.ylabel("Quantity")
  plt.hist(target_array_Radius_2030, H, rwidth=0.8, fill=True, color="#00ffd0", edgecolor="black", alpha=0.7, label="Period 20-30 days")

  H = np.linspace(min(target_array_Radius_3099), max(target_array_Radius_3099), 8)
  plt.xlabel("Solar radius")
  plt.ylabel("Quantity")
  plt.title("Radius histogram by period (Combined)")
  plt.hist(target_array_Radius_3099, H, rwidth=0.8, fill=False, edgecolor="black", alpha=1, label="Period >30 days")

  plt.legend()

  save_graphs("4. Radius Combined histogram") # image name

  plt.show()

RADIUSc()


