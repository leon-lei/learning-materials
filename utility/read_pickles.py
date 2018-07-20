import os
import pickle

def main():
    """
    Print out all pickles from current directory
    """

    file_list = os.listdir(os.getcwd())
    pickles_list = [x for x in file_list if '.pickle' in x]

    for _ in pickles_list:
        print('\n', '#'*50)
        print(f'Reading {_}')
        with open(_, 'rb') as f:
            p = pickle.load(f)
            for k,v in enumerate(sorted(p)):
                print(k,v)


if __name__=='__main__':
    main()