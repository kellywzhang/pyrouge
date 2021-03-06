import argparse
import pyrouge
from pyrouge import Rouge155
from pprint import pprint

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--gen_dir', type=str, help='generation directory')
    parser.add_argument('--ref_dir', type=str, help='reference directory')
    parser.add_argument('--gen_pattern', type=str, default='valid.(\d+).txt',
                        help='valid_title.(\d+).txt')
    parser.add_argument('--ref_pattern', type=str, default='valid.[A-Z].#ID#.txt',
                        help='valid_title.[A-Z].#ID#.txt')
    parser.add_argument('--rouge_path', type=str, default=None,
                        help='/home/kz918/pyrouge/ROUGE-RELEASE-1.5.5')
    args = parser.parse_args()
    print(vars(args))

    # Model == Reference
    # System == Generated

    

    if args.rouge_path is not None:
        r = Rouge155(args.rouge_path)
    else:
        r = Rouge155()
    r.system_dir = args.gen_dir
    r.model_dir = args.ref_dir
    r.system_filename_pattern = args.gen_pattern
    r.model_filename_pattern = args.ref_pattern

    output = r.convert_and_evaluate()
    print(output)
    output_dict = r.output_to_dict(output)
    pprint(output_dict)
    
