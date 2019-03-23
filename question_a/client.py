import re

from overlap import Overlap

if __name__ == '__main__':
    name = input("Enter the two groups where the first two numbers belong "
                 "to group 1 and third and fourth belong to group 2. "
                 "Use comma to separate them. (For example: 1,2,3,4) :")
    match = re.match(r'(\d),(\d),(\d),(\d)', name)
    if match:
        group_1 = (int(match.groups()[0]), int(match.groups()[1]))
        group_2 = (int(match.groups()[2])), int(match.groups()[3])
        is_overlap = Overlap.overlap(xy_1=group_1, xy_2=group_2)
        if is_overlap:
            print("Overlap!")
        else:
            print("Not overlap!")
    else:
        print("Invalid input! Try: 1,5,2,6")
