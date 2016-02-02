#Cayley Table Generator
## Requires Python 2.7.x

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

    python cayley.py u 10 x
    python cayley.py z 4 +
