
# CHARMM Reference Energies for a NBFIX System

These numbers are used in OpenMM's tests of the CharmmPsfFile class.

CHARMM input file: nbfixtest.inp

| Test             | Parameters           | Energy (kcal/mol) |
| ---------------- | -------------------- | ----------------- |
| no long-range correction | `{"LRC":""}` | 15559.71602 |
| dispersion correction (Allen-Tild.) | `{"LRC":"LRC"}` | 15497.11568 |
| long-range correction (Shirts et al.) | `{"LRC":"LRC_MS"}` | 15490.09028 |


