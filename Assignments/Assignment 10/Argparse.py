import argparse
parser = argparse.ArgumentParser()
args = parser.parse_args()
def array_of_numbers(number):
    arr = []
    for index in range(number + 1):
        arr.append(index)

    if args.reverse:
        arr = list(reversed(arr))

    return arr

print(array_of_numbers(int(args.number)))