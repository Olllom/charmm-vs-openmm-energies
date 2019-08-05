import os
#charmm = "/charmm/c40b1_gnu/exec/gnu/charmm"
charmm = "c41b1"

def run_test(directory, input_file="run.inp", parameters={}, output_file="run.out"):
    olddir = os.getcwd()
    os.chdir(directory)
    env = "".join("{}={}".format(prm, parameters[prm]) for prm in parameters)
    os.system("{} {} < {} > {}".format(charmm, env, input_file, output_file))
    with open(output_file, 'r') as f:
        for line in f:
            if line.strip().startswith("ENER>"):
                result = float(line.strip().split()[2])
    os.chdir(olddir)
    return result

if __name__ == "__main__":
    print("NBFIX")
    print( "no long-range-correction             ",
            run_test("nbfix", "nbfixtest.inp", {"LRC":""}))
    print( "dispersion correction (Allen-Tild.)  ",
            run_test("nbfix", "nbfixtest.inp", {"LRC":"LRC"}))
    print( "long-range correction (Shirts et al.)",
            run_test("nbfix", "nbfixtest.inp", {"LRC":"LRC_MS"}))
    print("DRUDE") 
    print( "no long-range-correction             ",
            run_test("drude", "drudetest.inp", {"LRC":""}))
    print( "dispersion correction (Allen-Tild.)  ",
            run_test("drude", "drudetest.inp", {"LRC":"LRC"}))
    print( "long-range correction (Shirts et al.)",
            run_test("drude", "drudetest.inp", {"LRC":"LRC_MS"}))

