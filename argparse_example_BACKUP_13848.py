<<<<<<< HEAD
import argparse
import sys

# Argparse is a parser for command-line options, arguments, and sub-commands.
# Having even just a very basic command-line interface (CLI) for your program
# can make everyone's life easier for modifying parameters, including programmers, but also non-programmers.
# A CLI for your program can also make it easier to automate running and modifying variables within your program,
# for when you want to run your program with a cronjob or maybe an os.system call.
# Let's make a super simple CLI as an example. Let's make a calculator program:

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? (add, sub, mul, or div)')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

# The above code will take arguments from the command line.
# The first parameter is basically the name of that argument, the next is the type of the variable,
# then a default, and finally a help parameter, just in case someone wants to be able to use -h

# First, just note that, to build the command line parser,
# first we specify the parser,
# then we add arguments,
# then, the line that is args = parser.parse_args() is what ends up using that parser to grab the current args,
# whatever they are

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

if __name__ == '__main__':
    main()

# Via the command line
# python argparse_example.py --x=5 --y=3 --operation=mul
=======
import argparse
import sys

# Argparse is a parser for command-line options, arguments, and sub-commands.
# Having even just a very basic command-line interface (CLI) for your program
# can make everyone's life easier for modifying parameters, including programmers, but also non-programmers.
# A CLI for your program can also make it easier to automate running and modifying variables within your program,
# for when you want to run your program with a cronjob or maybe an os.system call.
# Let's make a super simple CLI as an example. Let's make a calculator program:

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? (add, sub, mul, or div)')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

# The above code will take arguments from the command line.
# The first parameter is basically the name of that argument, the next is the type of the variable,
# then a default, and finally a help parameter, just in case someone wants to be able to use -h

# First, just note that, to build the command line parser,
# first we specify the parser,
# then we add arguments,
# then, the line that is args = parser.parse_args() is what ends up using that parser to grab the current args,
# whatever they are

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

if __name__ == '__main__':
    main()

# Via the command line
# python argparse_example.py --x=5 --y=3 --operation=mul
>>>>>>> origin/master
# python argparse_example.py -h for the help docs