from termcolor import colored
import argparse
import re
import sys
def mherlyn(file_path,strictness):
    contents = []
    with open(file_path) as file:
        for line in file:
            if line[0] != '#':
                contents.append(line)
        env_map = {}
        for line in contents:
            line = line.strip()
            if not line :
                continue
            try:
                first,last = line.split('=',1)
                if len(first)==0 or len(last)==0:
                    print(colored(f"VALIDATION FAILED AT {line}",'red'))
                    sys.exit(1)
            except:
                print(colored(f"VALIDATION FAILED AT {line}",'red'))
                sys.exit(1)
            if first in env_map:
                print(colored(f"Duplicate entry at {line},VALIDAITON FAILED",'red'))
                sys.exit(1)

            if strictness and (" " in last and not (last.startswith('"') and last.endswith('"'))):
                print(colored(f"Unquoted whitespace in value at {line}, validation failed", 'red'))
                sys.exit(1)
            env_map[first] = last
    print(env_map)
    print(colored("VALID FILE", "green"))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='mherlyn',description='cli based .env file validator')
    parser.add_argument('filename')
    parser.add_argument('-s','--strict',action='store_true')
    args = parser.parse_args()
    mherlyn(args.filename,args.strict)
