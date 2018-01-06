import argparse
from pyrouge import Rouge155

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--gen_dir', type=str, help='generation directory')
    parser.add_argument('--ref_dir', type=str, help='reference directory')
    parser.add_argument('--gen_pattern', type=str, help='some_name.(\d+).txt')
    parser.add_argument('--ref_pattern', type=str, help='some_name.[A-Z].#ID#.txt')
    args = parser.parse_args()
    print(vars(args))

    r = Rouge155()
    r.system_dir = args.ref_dir
    r.model_dir = args.gen_dir
    r.system_filename_pattern = args.ref_pattern
    r.model_filename_pattern = args.gen_pattern

    output = r.convert_and_evaluate()
    print(output)
    output_dict = r.output_to_dict(output)

    print(output_dict)
    import pdb; pdb.set_trace()
    
