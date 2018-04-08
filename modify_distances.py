import sys

# For modifying values of vertex-vertex distances
# Default distances are 1 along edges, 4 along diagonals

def modify_distance(string):

    # modified
    if string=='modify':

         print('The weight array is')
         print('[[0,w01,w02,w03],[w01,0,w12,w13],[w02,w12,0,w23],[w03,w13,w23,0]]')
         print('The default is')
         print('weight = [[0,1,4,1],[1,0,1,4],[4,1,0,1],[1,4,1,0]]')
         print('w01=1, w02=4, w03=1, w12=1, w13=4, w23=1')
         print()
         print('Input new integer values for w01,w02,w03,w12,w13,w23 ')
         print()

         w01,w02,w03,w12,w13,w23 = map(int,sys.stdin.readline().split())

         weight = [[0,w01,w02,w03],[w01,0,w12,w13],[w02,w12,0,w23],[w03,w13,w23,0]]

    # default
    elif string=="":
         weight = [[0,1,4,1],[1,0,1,4],[4,1,0,1],[1,4,1,0]]

    print(weight)

    return weight

def main():

    modify_distance('modify')

main()
