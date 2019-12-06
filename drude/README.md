
# CHARMM Reference Energies for a Drude System

These numbers are used in OpenMM's Drude tests of the CharmmPsfFile class.

CHARMM input file: drudetest.inp

| Test             | Parameters           | Energy (kcal/mol) |
| ---------------- | -------------------- | ----------------- |
| no long-range correction | `{"LRC":""}` | -1788.36644 |
| dispersion correction (Allen-Tild.) | `{"LRC":"LRC"}` | -1832.17898 |
| long-range correction (Shirts et al.) | `{"LRC":"LRC_MS"}` | -1835.06427 |


