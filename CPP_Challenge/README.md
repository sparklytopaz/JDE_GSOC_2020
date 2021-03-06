# Labyrinth
Let's imagine you have a labyrinth described as walls (#) and holes (.) where you cannot pass through the walls and you can move to adjacent holes. Diagonal adjacencies will not be taken into account, only vertical and horizontal.

Your applications should find the largest pathway moving only between holes, reading the labyrinth schema from a txt file, using only standard libraries of c++11. All the lines in the input file will have the same number of elements. Your application should save the schema of the largest detected pathway, overwriting the holes (.) with the order in which the hole has been visited.
Example:
input:
```
##.##.#
#..##.#
#.#####
#..####
#######
```
output:
```
6
##0##.#
#21##.#
#3#####
#45####
#######
```
Requirements:\
Your application should compile with the gcc compiler > 4.8 \
Results:\
Make of CMakeLists to compile the application.\
The source code of the application.

# HOW TO COMPILE :-
On Ubuntu terminal
```
g++ main.cpp -std=c++11
```
This will create a.out file

# HOW TO RUN :-

```
./a.out input.txt
```
