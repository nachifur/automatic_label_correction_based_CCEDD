from data_processing import data_processing
import sys
# run
# python datasets_generate.py 0
# debug
# python datasets_generate.py 1

inputs = sys.argv[1]
if inputs=="1":
    debug=1
else:
    debug=0

# label_correct
DATA_PATH = "../cell_data/label_correct"
train_ratio = 6
val_ratio = 1
test_ratio = 3
ratio_list = [train_ratio, val_ratio, test_ratio]
data_processing(DATA_PATH, ratio_list, debug, label_correct=True)


# label_no_correct
DATA_PATH = "../cell_data/label_no_correct"
train_ratio = 6
val_ratio = 1
test_ratio = 3
ratio_list = [train_ratio, val_ratio, test_ratio]
data_processing(DATA_PATH, ratio_list, debug, label_correct=False)
