import objective
import numpy as np

def comp(pascal1, pascal2):
    comp_l = (pascal1.get_contents() == pascal2.get_contents())
    comp = np.count_nonzero(comp_l)
    return comp

if __name__ == "__main__":
    print(comp(objective.Pascal(5,1000,0), objective.Pascal(10,1000,0)))
