# Path for exported data, numpy arrays
import os
import numpy as np

DATA_PATH = os.path.join('MP_Data') 

# Actions that we try to detect
actions = np.array(['i','man','woman','deaf','namaste','hello','bye','indian','sign','language','thank you'])#,'again','i/me','you','man','woman','he','she','deaf','hearing','teacher','thank you very much','welcome','please','sorry','namaste','how are you','i\'m fine','my name is','practice'])

# Thirty videos worth of data
no_sequences = 30

# Videos are going to be 30 frames in length
sequence_length = 30

# Folder start
start_folder = 30


for action in actions: 
    # dirmax = np.max(np.array(os.listdir(os.path.join(DATA_PATH, action))).astype(int))
    for sequence in range(1,no_sequences+1):
        try: 
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass
