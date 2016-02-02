#Cayley Table Generator

A simple python program that generates cayley tables based on group type, group size, and
operator.

## Use

    cayley.py <group type> <group size> <operation for group>

Supported Group Types
* U-Group: "u": All the relative primes relative to the group size
* Z-Group: "z": A group of numbers between 0 and group_size - 1

Supported Group Operations
* Multiplication: "x"
* Addition: "+"

Sample

    cayley.py u 10 x
    cayley.py z 4 +
