# DYBICO SOFTWARE ANNO 2021
This is the code for running the experimental Dynamic Bimanual Coordination paradigm for the ReScale Project, version 2021. 
Contact person: Keenie at kaa@nexs.ku.dk 
The original software was produced by Kristoffer Hougaard Madsen at DRCMR (kristofferm@drcmr.dk) and can be located on the server:
I:\SCIENCE-NEXS-ALL\Bimanual 


### NOTES: 
In case of error-messages or suggestions for improvement, please type the comment in the shared document: 
https://docs.google.com/document/d/1JRKlhOa3VbrMvkEC2qH6YLqp1u7w9ivJcc5YWdVuOFU/edit?usp=sharing
and notify Keenie on kaa@nexs.ku.dk.  

Note the software cannot run from the SCIENCE-NEXS-ALL server, but must be run locally. This is in accordance with only collecting data while the computer is offline. 

If Applejack suddenly does not provide input, remove the cord/connection, and reconnect. 

The program can ONLY be ended by clicking “q”, do not simply close the experimental window. 
The program ends automatically when done. If something goes wrong and Python crashes, close Python.  

When running the software a data-folder will be greated for saving data according to the user specified log and timestamp: 
C:\~\DYBICO\DATA
The data should immediately after the experiment be transferred to the server at I:\SCIENCE-NEXS-neurolab\PROJECTS\Bimanual\Bimanual_EEG. 

Do not make changes in the code – if you would like to make changes, save them as 
another file as I might update the scripts through Github. 

### Installations:
1) Download Anaconda https://repo.anaconda.com/archive/Anaconda3-2021.05-Windows-x86_64.exe 
2) Download the SILABS driver for compatibility with force device https://www.silabs.com/documents/public/software/CP210x_Universal_Windows_Driver.zip 
    and execute the CP210xVCPInstaller_x64.exe.
3) Download the InpOut Binaries driver to allow for sending triggers. Go to https://www.highrez.co.uk/downloads/inpout32/ under Download links and select the "Binaries only - x86 & x64 DLLs and libs" option. 
4) Go to the windows search bar, type and open Anaconda Prompt. Then type: pip install psychopy 
5) Go to the windows search bar, type and open Spyder 
6) When downloading the D-BICO Software, make sure that the zip files are extracted to the folder: C:\Users\ %USERNAME% \Documents\DYBICO
7) Open Spyder through the windows search bar, locate and run the __RUN_DYBICO__.py file to initiate the experiment. 
