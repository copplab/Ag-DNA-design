# Ag-DNA-design
This repository contains code for the design of DNA-stabilized silver nanoclusters across the full known spectral range, 400 nm to 1,000 nm.

Instructions for executing the code for the 1v1 SVM model for Agn-DNA nanocluster design as described in:





To predict the color class of DNA sequences the the predict_sequences.py file must be executed. To excute this file it is necessary to include a textfile
containing the seqeunces of interested. The name of the file must be included in line 27 in place of file_name, and the sequnces must be inlcuded in the 
file as follows. 

A C G T A C G T A C . 
C G T A C G T A C A . 
A C G A C G T A C G . 
T A C G T A C A C G . 

Executing the code will output a out.csv file that includes the probablity of each sequence falling into a color class for each 1v1 svm. 


Training data files can be found in the training data folder. Each file contains two of the spectral classes as definged in the paper.
to add addtional training data it must be included in the following way, with the 0 corrisponding to the smaller wavelengthclass and 1 the larger class. 

A C G T A C G T A C 0 . 
C G T A C G T A C A 0 . 
A C G A C G T A C G 1 . 
T A C G T A C A C G 1 . 

