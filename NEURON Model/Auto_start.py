### Auto start
## ********************************************************** ##
# Author:       Mohammed Mousa
# Email:        Mohamed.Mousa@wright.edu
# Affiliation:  Wright State University
## ********************************************************** ##
from neuron import h, gui



## loading the cell
h.load_file("Mousa2020_6CModel.hoc")    # Main Model - Control
# h.load_file("Mousa2020_6CModel_ALS.hoc")  # ALS Model 1 branch
# h.load_file("Mousa2020_6CModel_ALS - 9C.hoc") # ALS Model 3 branch
# h.load_file("Soma(Na_K).hoc")  # only Na and K, One compartment
# h.load_file("Soma(All).hoc") # all channels, One compartment (soma)

def singleCellRun():
    
    # myCell = h.fivecompMy()
    myCell = h.Mousa2020()

    return myCell
##-----------------{ systems functions }-----------------------
# #Note : this function is essential for the neuron GUI to work smoothly from python.
# definition of the custom advance process through python.
h('proc advance() {nrnpython("custom_advance()")}')


def custom_advance():
    h.fadvance()
# -----------------End of Function-----------------------------------------------


cell = singleCellRun()
# h.load_file("basic.ses")
h.load_file("iclamp.ses")
