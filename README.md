Connected Components Finder Using DFS Graph Traversal
========

This simple program ilustrates how you can easily find all the connected components in a graph by just running a DFS on it. Program includes Depth-First Search implementation, as well as algorithm for finding connected components.

The program uses *networkx*[1] library for Graph construction and *matplotlib*[2] for interactive representation of what is currently happening. Therefore these two libraries are requirements.

Installation
=====
To install the program you could just run:
```python
   pip install -r requirements.txt
```
However, matplotlib relies on *freetype* and *libpng* which you may need to install separately. For more info about the proper matplotlib installation check [3].

Usage
====
Using a program is easy. You just specify the list of nodes in your graph in the following format:
```python
   (1,2), (3,4), (3,5), (1,6), (1,7), (4,8)
```
and the graph gets automatically constructed.
The program will then interactively show what is happening with your graph. The final result should look like something like this:
![connected components](http://i61.tinypic.com/2hrh5ih.png "Connected components")

In the shell you should get the following output:
```
--- Graph G=(V,E) ---
Number of nodes: 8
Number of edges: 6
The edges are: [(1, 2), (1, 6), (1, 7), (3, 4), (3, 5), (4, 8)]

Traversing 1 (gray)
Traversing 2 (gray)
-----Backtrace 2 (black)
Traversing 6 (gray)
-----Backtrace 6 (black)
Traversing 7 (gray)
-----Backtrace 7 (black)
-----Backtrace 1 (black)
---1. connected component.---

Traversing 3 (gray)
Traversing 4 (gray)
Traversing 8 (gray)
-----Backtrace 8 (black)
-----Backtrace 4 (black)
Traversing 5 (gray)
-----Backtrace 5 (black)
-----Backtrace 3 (black)
---2. connected component.---


Total number of connected components: 2
They are:
	[2, 6, 7, 1]
	[8, 4, 5, 3]
```

References
====
[1] http://networkx.github.io <br>
[2] http://matplotlib.org<br>
[3] http://matplotlib.org/users/installing.html
