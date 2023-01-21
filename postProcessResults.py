import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from calcAbsorptionCoefficient import cac
mic1 = "Lidinoid_NIT_HarmonicAcousticSim_InputDeck-acouPressure-node-184100-mic1.hist"
mic2 = "Lidinoid_NIT_HarmonicAcousticSim_InputDeck-acouPressure-node-201330-mic2.hist"
dfSim = cac(mic1, mic2, 150)
dfSim.to_csv("alphaVsFrequency_FINAL.csv", index=False)
plt.rcParams["figure.figsize"] = (20,8)
fig = plt.figure()
ax = plt.axes()
plt.xlim([377, 3400])
plt.ylim([0, 1])
plt.ylabel("Absorption Coefficient")
plt.xlabel("Frequrency (Hz)")
ax.plot(dfSim["f"], dfSim["alpha"]);
plt.savefig('SimResults.png')
