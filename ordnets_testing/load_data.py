import argparse
import sys
import os
import csv
import yaml
import random

from Data import *
import pickle as pkl

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

def read_config(path):
    return AttrDict(yaml.load(open(path, 'r'), Loader = yaml.FullLoader))


parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
current_dir = os.getcwd()
sys.path.insert(0, parent_dir)

def parse_args():
    parser = argparse.ArgumentParser(description='load_data.py')
    parser.add_argument('-config', default = 'stn', type =str)
    parser.add_argument('-model', default='stn', type=str,
                        choices=['stn'])
    parser.add_argument('-loss', default='comb', type=str,
                        choices=['triplet', 'comb'])
    parser.add_argument('-seed', default=2, type=int,
                        help="Random seed")
    parser.add_argument('-log', default='stn', type=str,
                        help="Log directory")
    parser.add_argument('-facility', default=10606, type=int,
                        help="Log directory")
    parser.add_argument('-split',default='room', type=str,
                        help="split 1/5 sensors or rooms for test",
                        choices = ['room', 'sensor'])
    args = parser.parse_args()
    config = read_config(args.config + '.yaml')
    return args, config

args, config = parse_args()

def main():
    x, y, true_pos = read_colocation_data(config)
    pkl.dump([x,y,true_pos],open("data.pkl","wb"))

if __name__ == '__main__':
    main()
    