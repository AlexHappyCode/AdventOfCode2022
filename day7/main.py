import os
from colorama import Fore

print(os.getcwd())

with open('input.txt') as input:
    lines = input.readlines()

def find_at_most_100000(lines):
    dir_sizes = dict()
    filenames = set()
    stack = []

    for line in lines:
        #print(Fore.LIGHTYELLOW_EX + 'dir_sizes', dir_sizes)
        line = line.strip('\n')
        print(Fore.RED + 'stack', stack)

        # command
        if line.startswith('$'):
            print(Fore.GREEN + 'command', line)
            # cd
            if line.startswith('$ cd'):
                if line == '$ cd ..':
                    stack.pop()
                elif line.startswith('$ cd /'):
                    if line == '$ cd /':
                        print('back to root')
                        stack = ['/']
                    else:
                        stack = line[5:].split('/')[1:]
                        stack.insert(0, '/')
                    print('ABSOLUTE PATH', stack)
                elif line.startswith('$ cd '):
                    stack.append(line[5:])
        else: #output
            # file
            print(Fore.CYAN + line)
            file = '/'.join(stack) + '/' + line.split(' ')[1]
            if line.split(' ')[0] == 'dir':
                pass
            else: # file
                #print('file_size', line.split()[0])
                print('filepath', file)
                #print('filenames', filenames)
                file_size = int(line.split(' ')[0])
                if file not in filenames:
                    filenames.add(file)
                    # add to every dir in stack
                    for i, dir in enumerate(stack): # get the full path
                        dir = '/'.join(stack[:i + 1])
                        dir_sizes[dir] = dir_sizes.get(dir, 0) + file_size
    total = 0 # add total sum of less than 1000000

    # total space is 70000000
    unused_space = 70000000 - dir_sizes['/']
    smallest_after_30000000 = float('inf')
    for i, (k, v) in enumerate(dir_sizes.items()):
        if v + unused_space >= 30000000:
            smallest_after_30000000 = min(smallest_after_30000000, v)
        print(k, v)
        if v <= 100000:
            total += v
    print('smallest after 30000000', smallest_after_30000000)
    
    #for filename in filenames:
    #    print(filename)
    #print(dir_sizes)
    #print(filenames)
    print('total used', dir_sizes['/'])
    return total


#print(find_at_most_100000(lines[:50]))
# 1325919 is the answer
# 48,381,165 is the total space
print('at most 1000000', find_at_most_100000(lines))
