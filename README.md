# Quine-McCluskey Algorithm Implementation

This project is an implementation of the Quine-McCluskey algorithm in Python, used for minimizing Boolean functions. The algorithm is designed to reduce the complexity of Boolean expressions, making it easier to work with logic circuits.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
  - [Input](#input)
  - [Output](#output)
- [Example](#example)
- [Algorithm Overview](#algorithm-overview)
- [Code](#code)
- [Output](#output)
- [Acknowledgments](#acknowledgments)

## Introduction

The Quine-McCluskey algorithm, also known as the tabulation method, is a method used for minimization of Boolean functions. It is an exact method and provides a systematic approach to simplify Boolean expressions, making it easier to design and implement digital logic circuits.

This implementation allows you to input a set of minterms and optionally don't cares, and then it will produce the minimized Boolean function.

## Features

- Convert minterms to binary.
- Group minterms based on the number of `1`s in their binary representation.
- Compare and combine minterms to find Prime Implicants.
- Generate a Prime Implicant (PI) chart.
- Identify Essential Prime Implicants (EPIs).
- Apply row and column dominance to further minimize the Boolean expression.

## Usage

### Input

- **Minterms**: A list of minterms in decimal form.
- **Don't Cares**: (Optional) A list of don't care terms in decimal form.
- **Bit Size**: The number of bits used in the binary representation of the minterms.

### Output

- **Prime Implicants**: A list of prime implicants in binary form.
- **PI Chart**: A chart displaying the prime implicants and their corresponding minterms.
- **Essential Prime Implicants (EPIs)**: A list of EPIs, which are necessary to cover all minterms.
- **Minimized Boolean Expression**: The simplified Boolean function after applying the algorithm.

## Example


Write minterms: 1 3 7 8 9 11 15
Write dontcares (if not there, enter nothing): 5 13
Enter bit size: 4
===============Minterms=================
['1', '3', '7', '8', '9', '11', '15']
===============Don't Cares=================
Don't Care:  ['5', '13']
...
==========Essential Prime Implicants:=============
...
continue... 
(see pdf for output)

Algorithm Overview
Convert Decimal to Binary: Convert all input minterms and don't cares to binary form.
Group Minterms: Group the binary minterms based on the number of 1s.
Compare and Combine: Compare minterms within adjacent groups and combine them if they differ by only one bit.
Generate Prime Implicants: Collect the prime implicants from the uncombined minterms.
Create PI Chart: Create a chart that shows which minterms are covered by each prime implicant.
Identify Essential Prime Implicants: Identify EPIs that are necessary to cover the minterms.
Minimize Further: Apply row and column dominance to minimize the Boolean expression further.
Code
The full implementation of the Quine-McCluskey algorithm can be found in the provided quine_mccluskey.py file.

Output
The output section displays the minimized Boolean expression and the steps involved in the minimization process, such as identifying prime implicants, generating the PI chart, and determining EPIs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

