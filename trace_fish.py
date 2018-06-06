import matplotlib
matplotlib.use('Agg')

import pandas as pd
import xlrd
from matplotlib import pyplot as plt
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', type=str, required=True)
parser.add_argument('-d', '--destination', type=str, required=True)
parser.add_argument('-st', '--start', type=float, default=10)
parser.add_argument('-e', '--end', type=float, default=600)

args = parser.parse_args()

save_path = args.destination

files = os.listdir(args.source)
for file in files:
    print(file)
    if not file.startswith("Raw") or \
            os.path.isdir(os.path.join(args.source, file)):
        continue
    exp_data = pd.read_excel(
        os.path.join(args.source, file), header=0, skiprows=list(range(33)),
        sheet_name=None)
    book = xlrd.open_workbook(os.path.join(args.source, file))

    for ch in exp_data.keys():
        print(ch)
        positions = exp_data[ch].loc[  # cut the header
                    10:, ["Trial time", "X center", "Y center"]]
        positions = positions[(positions["X center"] != "-") &
                              (positions["Y center"] != "-") &
                              (positions["Trial time"] <= args.end) &
                              (positions["Trial time"] > args.start)]

        # when track to short
        if len(positions) == 0 or positions["Trial time"].iloc[-1] < args.end:
            print("2")
            continue

        arena = ch.split("-")[1]

        sheet = book.sheet_by_name(ch)

        group = sheet.cell(31, 1).value
        trial = sheet.cell(4, 1).value

        if not os.path.isdir(os.path.join(save_path, group)):
            os.makedirs(os.path.join(save_path, group))

        plt.clf()

        print(os.path.join(save_path, group,
                                 "Trial_{}_{}.png".format(trial, arena)))

        plt.plot(positions["X center"], positions["Y center"])
        plt.axis('off')
        plt.savefig(os.path.join(save_path, group,
                                 "Trial_{}_{}.png".format(trial, arena)))
        # plt.show()



