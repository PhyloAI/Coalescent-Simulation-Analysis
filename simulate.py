import os
from ete3 import Tree
import argparse


parser = argparse.ArgumentParser(description="", add_help=True)
required = parser.add_argument_group("Required arguments")
required.add_argument('-n', '--simulate_times', action="store", metavar='\b', type=str, required=True, help="")
required.add_argument('-o', '--outgroup_species', action="store", metavar='\b', type=str, required=True, help="")

args                           = parser.parse_args()
simulate_times                = args.simulate_times
outgroup_species               = args.outgroup_species


def get_species_num():
    tree1 = Tree("astral.tre.regular.tre")
    n = 0
    for node in tree1.traverse("postorder"):
        if node.is_leaf():
            n = n + 1
    return n
    

species_num = get_species_num()
os.system("Rscript 00.simulate.Rscript astral.tre.regular.tre" + " " + str(species_num) + " " + str(simulate_times))


with open("simulate.trees", "r") as read_file:
    with open("astral.simulate.reroot.tree", "a") as write_file:
        for each_line in read_file:
            tree1 = Tree(each_line)
            tree1.set_outgroup(outgroup_species)
            write_file.write(tree1.write() + "\n")

os.remove("simulate.trees")
