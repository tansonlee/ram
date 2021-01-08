# Random Access Memory ADT

## Implementation of a RAM using Functional Programming Techniques

You can use this implementation online using repl.it here: [RAM](https://repl.it/@TansonL/ram)

## Table of Contents
1. [Introduction](#introduction)
2. [List of Functions](#list-of-functions)
3. [Example](#example)
4. [Description of Functions](#description-of-functions)
5. [How to Use](#how-to-use)

## Introduction

An implementation of a RAM in Python using Functional Programming. The implementation is based on a trie which can be found here:
[Implementation of Trie](https://github.com/tansonlee/trie). 

This implementation of a RAM can be used to implement other data structures such as an array, linked-list, binary tree, and trie.

## List of functions
* ram
* ram_store(ram, address, value)
* ram_fetch(ram, address)
* core_dump(ram)

## Example

```python
my_ram = ram_store(ram_store(ram, 77, 1010), 2, 999)
core_dump(my_ram)

my_ram_replace_2 = ram_store(my_ram, 2, 111)
core_dump(my_ram_replace_2)

```

The output is:
```python
-----------------------
[2]: 999
[77]: 1010
-----------------------

-----------------------
[2]: 111
[77]: 1010
-----------------------
```

## Description of Functions

**ram**
* O(1) time
* returns the empty RAM

**ram_store(ram, address, value)**
* O(1) in the unit-cost model
* O(log(n)) where n = address in the log-cost model
* takes a ram, natural number address, and natural number value
* returns a new ram with all the elements of ram and value stored at address

**ram_fetch(ram, address)**
* O(1) in the unit-cost model
* O(log(n)) where n = address in the log-cost model
* takes a ram and natural number address
* returns the value stored in address; None if there is no value there

**core_dump(ram)**
* impure function
* O(1)
* takes a ram
* outputs the all addresses with their corresponding values in ram
* **only outputs to address 1000

## How to Use

1. Follow this link to the online editor: [RAM](https://repl.it/@TansonL/ram)

2. Replace the example in main.py with your program.

3. Run the program by clicking the green Run button.