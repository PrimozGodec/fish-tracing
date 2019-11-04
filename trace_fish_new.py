import matplotlib
matplotlib.use('Agg')

import pandas as pd
from matplotlib import pyplot as plt
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', type=str, required=True)
parser.add_argument('-st', '--start', type=float, default=0)
parser.add_argument('-e', '--end', type=float, default=10000)

args = parser.parse_args()

file = args.source
save_path = os.path.join("data", "output", ".".join(os.path.basename(file).split(".")[:-1]))

# create a dir if not existing
if not os.path.exists(save_path):
    os.makedirs(save_path)

exp_data = pd.read_excel(
    file, header=None,
    names=["Time1", "Time2", "X", "Y", "1", "2", "3", "4", "5", "6", "7", "8"],
    index_col=None,
    sheet_name=None)

for ch in exp_data.keys():
    print(ch)

    positions = exp_data[ch]

    if not ("Time1" in positions and "X" in positions):
        print("Skipping {}. Seems to be empty.".format(ch))
        continue

    positions = positions[(positions["Time1"] <= args.end) &
                         (positions["Time1"] > args.start)]

    # when track to short
    if len(positions) == 0 or positions["Time1"].iloc[-1] < args.end:
        print("Warning: {} shorter than {} seconds.".format(ch, args.end))

    # remove positions with unknown values (-)
    positions = positions[(positions["X"] != "-") & (positions["X"] != "-")]

    plt.clf()

    plt.plot(positions["X"], positions["Y"])
    plt.axis('off')
    plt.axis('equal')
    print(os.path.join(save_path, ch + ".png"))
    plt.savefig(os.path.join(save_path, ch + ".png"))
