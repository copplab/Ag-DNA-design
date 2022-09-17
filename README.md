# Ag-DNA-design
This repository contains code for the design of DNA-stabilized silver nanoclusters with peak emission wavelengths from about 400 nm to 1,000 nm.

Instructions for executing the code for the 1v1 SVM model for Agn-DNA nanocluster design are described in [accepted manuscript; DOI coming soon]


To predict the color class of DNA sequences, execute predict_sequences.py , including a textfile containing the sequences of interest. File name must be included in line 27 (in place of file_name), and the sequences must be inlcuded in the 
following format: 

A C G T A C G T A C . 
C G T A C G T A C A . 
A C G A C G T A C G . 
T A C G T A C A C G . 

Executing the code will output a out.csv file that includes the probablity of each sequence falling into a color class for each 1v1 svm. 


Training data files are in the training data folder. Each file contains two of the spectral classes as defined in the paper.
To add addtional training data, list the sequence followed immediately by a 0 or 1 to indicate the color class, with 0 corresponding to the shorter wavelength class and 1 to the longer wavelength class. For example: 

A C G T A C G T A C 0 . 
C G T A C G T A C A 0 . 
A C G A C G T A C G 1 . 
T A C G T A C A C G 1 . 
