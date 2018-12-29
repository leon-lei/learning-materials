def main():
    example = ['left', 'right', 'up', 'down']

    # for i in range(len(example)):
    #     print(i, example[i])

    # cleaner way to print out both index and value
    print('for i,j in enumerate(example):\nprint(i,j)\n')
    for i,j in enumerate(example):
        print(i, j)

    # create a dictionary using enumerate off the list
    print('\nnew_dict = dict(enumerate(example))\nprint(new_dict)\n')
    new_dict = dict(enumerate(example))
    print(new_dict,'\n')

    # printing the k,v is a little weird only because our keys are also the count
    # [print(i, j) for i, j in enumerate(new_dict.items())]

    # printing the k,v from this dict is easier to comphrehend
    example_dict = {'left':'<',
                    'right':'>',
                    'up':'^',
                    'down':'v',}
    print('[print(i, j) for i, j in enumerate(example_dict.items())]\n')
    [print(i, j) for i, j in enumerate(example_dict.items())]

    # 0 ('left', '<')
    # 1 ('right', '>')
    # 2 ('up', '^')
    # 3 ('down', 'v')

if __name__ == '__main__':
    main()
