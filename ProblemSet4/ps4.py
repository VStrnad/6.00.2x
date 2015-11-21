# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

def plotHist(result, title, xLabel, yLabel):
    pylab.hist(result)
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.legend(loc = 1)
    pylab.show()

#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    steps = 150
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005

    delay = 150
    timesteps = steps + delay

    result = []

    virusPop = [0] * timesteps
    virusPopWithDrug = [0] * timesteps

    for trial in range(numTrials):
        viruses = []
        for i in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        patient = TreatedPatient(viruses, maxPop)
        for i in range(timesteps):
            if i == delay:
                patient.addPrescription('guttagonol')
            totalPop = patient.update()
            virusPop[i] += totalPop
            virusPopWithDrug[i] += patient.getResistPop(['guttagonol'])

        result.append(patient.getTotalPop())

    plotHist(result, "simulation With Delay", "total population", "trials")

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO

    first_steps = 150
    lag_steps = 75  #lag time between two drugs
    final_steps = 150

    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    timesteps = first_steps + lag_steps + final_steps

    result = []

    virusPop = [0] * timesteps
    virusPopWithDrug = [0] * timesteps

    for trial in range(numTrials):
        viruses = []
        for i in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        patient = TreatedPatient(viruses, maxPop)
        for i in range(timesteps):
            if lag_steps == 0 and i == first_steps:
                patient.addPrescription('guttagonol')
                patient.addPrescription('grimpex')
            elif i == first_steps:
                patient.addPrescription('guttagonol')
            elif i == (first_steps+lag_steps):
                patient.addPrescription('grimpex')
            totalPop = patient.update()

        result.append(patient.getTotalPop())

    plotHist(result, "simulation With two drugs", "total population with the virus", "no of patients")

numTrials = 500
simulationDelayedTreatment(numTrials)
simulationTwoDrugsDelayedTreatment(numTrials)


