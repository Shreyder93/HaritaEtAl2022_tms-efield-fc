# Welcome to the Scripts folder!

Here you can find all the code used to analyze the data and arrive at the results reported in the manuscript.

There are two types of scripts here:

1) Python Code - (files ending in '.py')

These scripts contain code that sets up SimNIBS and runs it based on the 10-20 EEG electrodes selected as dlPFC (F3) and OFC (Fp1) targets. There are two seprate scripts - one for the dlPFC and the other for the OFC. The outputs of these scripts are the dlPFC and OFC subject-specific E-fields which can be found in the 'Data/E_field_Analysis/' sub-folder within this repo.

2) Jupyter Notebooks - (files ending in '.ipynb')

Jupyter notebooks use the E-fields derived using (1) and functional connecitivty data from the human connectome project (HCP) to determine TMS-target (dlPFC, OFC) functional connectivity. For this study we used two types of E-fields and two types of resting-state fMRI:

E-fields: 

1) Subject-specific E-fields (ss_E_fields)
2) Normative E-field (ernie_E_fields) - This is shipped as part of the SimNIBS software package. 

rs-fMRI data: 

1) Subject-specific rs-fMRI data (ss_FC)
2) Group averaged rs-fMRI data (const_FC)

As a result, 3 types of jupyter notebook can be found:

1) ss_E_fields_const_FC - this notebook looks at TMS target connectivity using subject-specific E-fields and group-averaged rs-fMRI data.
2) ernie_E_fields_ss_FC - this notebook looks at TMS target connectivity using ernie (normative) E-fields and subject-specific rs-fMRI data.
3) ss_E_fields_ss_FC - this notebook looks at TMS target connectivity using subject-specific E-fields and subject-specific rs-fMRI data.

The above 3 variations were repeated for the dlPFC and OFC resulting in 6 jupyter notebooks - 3 for dlPFC- and 3 for OFC- TMS connectivty. These are labelled accordingly within the folder.

The 'Statistics.ipynb' does exactly what you'd expect. Here we carry out statistical analysis on our data. This data can be found in the Data folder (within the 'Stats' subfolder). 

The subject IDs of the 12 subjects from the HCP database can be found below (M: male; F: female):

1) 151526 (M)
2) 162935 (M)
3) 189349 (F)
4) 191437 (F)
5) 214524 (M)
6) 667056 (M)
7) 680957 (F)
8) 725751 (M)
9) 783462 (M)
10) 872764 (F)
11) 912447 (M)
12) 990366 (M)

