
# CHARMM Reference Energies for CHARMM switching functions

These numbers are used in the openmmtools tests for custom switching functions 
and alchemical functions.

CHARMM input file: switchtest.inp

| Test             | Parameters           | Energy (kcal/mol) |
| ---------------- | -------------------- | ----------------- |
| hard cutoff, original parameters | `{"SOL":"m14", "SUB":"original", "SWITCH":"VSWITCH", "CUT":"10.0"}`         | -10358.06 |
| hard cutoff, annihilated electrostatics | `{"SOL":"m14", "SUB":"uncharged", "SWITCH":"VSWITCH", "CUT":"10.0"}` | -10271.68 |
| hard cutoff, annihilated elec + vdw | `{"SOL":"m14", "SUB":"annihilated", "SWITCH":"VSWITCH", "CUT":"10.0"}`   | -10267.07 |
| vswitch original parameters | `{"SOL":"m14", "SUB":"original", "SWITCH":"VSWITCH", "CUT":"12.0"}`              | -10370.17 |
| vswitch annihilated electrostatics | `{"SOL":"m14", "SUB":"uncharged", "SWITCH":"VSWITCH", "CUT":"12.0"}`      | -10283.79 |
| vswitch annihilated elec + vdw | `{"SOL":"m14", "SUB":"annihilated", "SWITCH":"VSWITCH", "CUT":"12.0"}`        | -10278.77 |
| vfswitch original parameters | `{"SOL":"m14", "SUB":"original", "SWITCH":"VFSWITCH", "CUT":"12.0"}`            | -10333.46 |
| vfswitch annihilated electrostatics | `{"SOL":"m14", "SUB":"uncharged", "SWITCH":"VFSWITCH", "CUT":"12.0"}`    | -10247.08 |
| vfswitch annihilated elec + vdw | `{"SOL":"m14", "SUB":"annihilated", "SWITCH":"VFSWITCH", "CUT":"12.0"}`      | -20243.32 |
