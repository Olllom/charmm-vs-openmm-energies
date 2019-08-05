from __future__ import print_function
import os

charmm = "/charmm/c40b1_gnu/exec/gnu/charmm"
#charmm = "c41b1"

def run_test(directory, input_file, expected, parameters={}, output_file="run.out"):
    olddir = os.getcwd()
    os.chdir(directory)
    env = "".join("{}={}".format(prm, parameters[prm]) for prm in parameters)
    os.system("{} {} < {} 2>&1 | tee {}".format(charmm, env, input_file, output_file))
    with open(output_file, 'r') as f:
        for line in f:
            if line.strip().startswith("ENER>"):
                result = float(line.strip().split()[2])
    os.chdir(olddir)
    assert abs(result-expected) < 0.1
    return result

if __name__ == "__main__":
    print("NBFIX")
    print( "no long-range-correction             ",
            run_test("nbfix", "nbfixtest.inp", 15559.71602, {"LRC":""}))
    print( "dispersion correction (Allen-Tild.)  ",
            run_test("nbfix", "nbfixtest.inp", 15497.11568, {"LRC":"LRC"}))
    print( "long-range correction (Shirts et al.)",
            run_test("nbfix", "nbfixtest.inp", 15490.09028, {"LRC":"LRC_MS"}))
    print("DRUDE") 
    print( "no long-range-correction             ",
            run_test("drude", "drudetest.inp", -1788.36644, {"LRC":""}))
    print( "dispersion correction (Allen-Tild.)  ",
            run_test("drude", "drudetest.inp", -1832.17898, {"LRC":"LRC"}))
    print( "long-range correction (Shirts et al.)",
            run_test("drude", "drudetest.inp", -1835.06427, {"LRC":"LRC_MS"}))

