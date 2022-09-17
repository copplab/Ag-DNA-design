# Ag-DNA-design
This repository contains code for the design of DNA-stabilized silver nanoclusters across the full known spectral range, 400 nm to 1,000 nm.

Training data files can be found in the training data folder. Each file contains two of the spectral classes as definged in the paper.
All training data must be included in a separate text file with the sequences listed below. With the 0 corrisponding to the smaller wavelength
class and 1 the larger class. 

A C G T A C G T A C 0 .
C G T A C G T A C A 0 .
A C G A C G T A C G 1 .
T A C G T A C A C G 1 .

Running the SVM code will will result 

To generate the accuracies of each model the SVM_accuracies code must be executed. 

To predict new seqeunces predict sequences code is must be run. To execute this code 
