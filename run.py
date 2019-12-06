from __future__ import print_function
import os
import sys
import getpass


def charmm_executable():
    if getpass.getuser() in {"travis", "root"}:
        # charmm in docker container
        return "/charmm/c40b1_gnu/exec/gnu/charmm"
    else:
        # local charmm
        return "c41b1"


def parse_readme_values(directory):
    """
    parse README.md file in subdirectory
    and extract
        - CHARMM input file
        - test configurations (short description, input parameters, reference values)
    """
    input_file = None
    tests = []
    readme_file = os.path.join(directory, "README.md")
    if not os.path.isfile(readme_file): return None, []
    with open(readme_file, "r") as f:
        table_row = 0
        for line in f:
            if line.startswith("CHARMM input file:"):
                input_file = line.split(":")[1].strip()
            if line.startswith("|"):
                table_row += 1
                if table_row > 2: # first two lines are table header
                    config = line.replace('`','').split('|')[1:4]
                    config[1] = eval(config[1])
                    config[2] = float(config[2])
                    tests.append(config)
    return input_file, tests


def run_test(directory, input_file, expected, parameters={}, output_file="run.out", throw=False, verbose=False):
    """
    run the test in CHARMM
    """
    olddir = os.getcwd()
    os.chdir(directory)
    env = " ".join("{}={}".format(prm, parameters[prm]) for prm in parameters)
    out = "2>&1 | tee {}".format(output_file) if verbose else "> {}".format(output_file) 
    os.system("{} {} < {} {}".format(charmm_executable(), env, input_file, out))
    with open(output_file, 'r') as f:
        for line in f:
            if line.strip().startswith("ENER>"):
                result = float(line.strip().split()[2])
    os.chdir(olddir)
    if throw:
        assert abs(result-expected) < 0.1
    return result, expected


if __name__ == "__main__":
    verbose = "-v" in sys.argv
    throw = "-t" in sys.argv
    if "-h" in sys.argv:
        print("Run CHARMM tests defined in subdirectories' README files.")
        print("Parameters:")
        print("   -t  throw for mismatching energies")
        print("   -v  print CHARMM output on command line")
        sys.exit(0)
    directories = [d for d in os.listdir() if os.path.isdir(d)]
    for directory in directories:
        print("\n"+directory.upper())
        charmm_input, tests = parse_readme_values(directory)
        for test in tests:
            description, env, ref = test
            result, expected = run_test(directory, charmm_input, ref, env, throw=throw, verbose=verbose)
            print("{:50} {:10.2f} | ref: {:10.2f}".format(description, result, expected))

