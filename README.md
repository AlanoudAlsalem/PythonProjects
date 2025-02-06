## 🪁 Project #1 : Polynomial Model Optimizer
Deriving functions to accurately model datasets is no easy feat. 
* This [python script](/polynomials.py) computes the most accurate polynomial obtainable for a given dataset.
* The x and y coordinates are in list format in two lines of code.
* The desired polynomial degree is given as an input (with a maximum degree of 7).
* It uses the substitution of `n + 1` corrdinates, where `n = degree`.
* For each combination of coordinates, the absolute error is computed.
* The algorithm returns the optimal set of coordinates for manual derivation of the function according to the minimum absolute error.

## 🪼 Project #2 : RISC-V Customized Assembler
My 5-stage pipelined [RISC-V processor](https://github.com/AlanoudAlsalem/RISCV-Processor.git) needed an assembler to translate assembly into machine code.
* This customized [python assembler](/RISCV-assembler) does the job. 
