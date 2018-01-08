import os
import argparse
import pyrouge
from pyrouge import Rouge155
from pprint import pprint

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--gen_file', type=str, help='generation directory')
    parser.add_argument('--ref_file', type=str, help='reference directory')
    parser.add_argument('--gen_dir', type=str, help='generation directory')
    parser.add_argument('--ref_dir', type=str, help='reference directory')
    parser.add_argument('--gen_pattern', type=str, default='valid.(\d+).txt',
                        help='valid_title.(\d+).txt')
    parser.add_argument('--ref_pattern', type=str, default='valid.[A-Z].#ID#.txt',
                        help='valid_title.[A-Z].#ID#.txt')
    args = parser.parse_args()
    print(vars(args))

    # Model == Reference
    # System == Generated

    with open(args.gen_file, 'r') as f:
        gen = f.readlines()
    for i, l in enumerate(gen):
        f = open(os.path.join(args.gen_dir, 'valid.{}.txt'.format(i)), 'w')
        f.write(l)
        f.close()

    with open(args.ref_file, 'r') as f:
        ref = f.readlines()
    for i, l in enumerate(ref):
        f = open(os.path.join(args.ref_dir, 'valid.A.{}.txt'.format(i)), 'w')
        f.write(l)
        f.close()
        
