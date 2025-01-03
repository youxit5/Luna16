# some directory for output the results:
OUTPUT_PATH = 'H:/Luna16_Data/prepare'

# Resource path which contains: annotations.csv, candidates.csv,
# and subdirectories containing .mhd files.
# This is the directory structure needed to run the code:
# (The code will use all .mhd and .raw files inside subdirectories which their name is in annotations or candidates)
'''
C:/Users/lized/PycharmProjects/medical_image/CPM/data_raw/
            annotations.csv
            candidates.csv
            subset0/
                        *.mhd
                        *.raw
            subset1/
                        *.mhd
                        *.raw
'''
RESOURCES_PATH = 'H:/Luna16_Data/Extracted/luna'





PADDING_FOR_LOCALIZATION = 10
BLOCK_SIZE = 128
COORDS_CUBE_SIZE = 32
TARGET_SHAPE = (COORDS_CUBE_SIZE, COORDS_CUBE_SIZE, COORDS_CUBE_SIZE, 3, 5)
COORDS_SHAPE = (3, COORDS_CUBE_SIZE, COORDS_CUBE_SIZE, COORDS_CUBE_SIZE)
ANCHOR_SIZES = [10, 30, 60]
VAL_PCT = 0.2
TOTAL_EPOCHS = 100
DEFAULT_LR = 0.01
