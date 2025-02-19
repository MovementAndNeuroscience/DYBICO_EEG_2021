# -*- coding: utf-8 -*-
""" D-BICO SOFTWARE ANNO 2021
PLEASE REFER TO THE README.md FILE IN THE D-BICO FOLDER FOR INSTRUCTIONS. 
"""

#%% 

if __name__ == '__main__':
    import sys
    import os
    
    ####################################################################
    # get path to script 
    path = os.path.split(sys.argv[0])[0]
    os.chdir(path)
    
    
    #####################################################################
    # installations automatized  K pandas version 1.2.4 before update , lab computer had 1.3.4 
    # if not os.path.exists('C:\\Users\%USERNAME%\Anaconda3\Lib\site-packages\psychopy'): 
    #     import subprocess
    #     subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psychopy'])
    #     subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyqt5==5.12.1'])
    #     subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyqtwebengine==5.12.1'])
    #     # pip install mkl??
    # else: 
    #     print('packages already installed')
    
    #####################################################################
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    #####################################################################
    import adv_gui
    window = adv_gui.MainWindow()
    window.show()
    
    #####################################################################
    sys.exit(app.exec_())
    exit() 
  
    
    
#%% 
    
