import os
import shutil

HOME='/home/hungvs/FPT/table_recognition/solutions/deep_learning/table-transformer/src/testset/east'

if os.path.exists(HOME):
    shutil.rmtree(HOME)

os.mkdir(HOME)