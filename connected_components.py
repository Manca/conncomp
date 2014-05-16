#!/usr/bin/python
"""
Connected components finder using Depth-First Search Graph Traversal.
Copyright (C) 2011 Nenad Mancevic (manca1@gmail.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.					
"""
__author__="""Nenad Mancevic (manca1@gmail.com)"""
import networkx as nx
import time
import random
import matplotlib.pyplot as plt

"""
Main class GraphX:
methods:
  isEdge(u, v)     - checks whether there is an edge between nodes u and v
  DFS(start)       - calls DFS algorithm with the starting node start
  runDFS(u, st)    - starts DFS traversal; args: u - node, st - nodes status vector (white, gray, black)
  connComponents() - finds connected components and draws them interactively 
  printGraph()     - prints basic Graph information
  printStates()    - prints all the status vector values
"""
class GraphX:

    def __init__(self):      
        self.G = nx.Graph()
        grane = list(input("Enter edges (i, j) (separated by comma): "))
        if not isinstance(grane[1], tuple):             # checks if there is only one edge
            self.G.add_edge(grane[0], grane[1])
        else:
            self.G.add_edges_from(grane)                # if we have more than one, we add the edges array in graph

        for i in self.G.nodes_iter():
            self.G.node[i] = 'white'                    # all the nodes get the 'White' starting color
        self.state = dict(self.G.nodes(data=True))      # creates a dictionary of all the nodes and their states
        self.no_conncomp = 0
        self.already_visited = []
        self.components = []
        """
		   The following code initializes drawing surface. It also draws graph initially.
        """
        plt.ion()                                                                               # turns on interactive mode
        self.pos=nx.circular_layout(self.G)
        figure = plt.figure(figsize=(8,8))
        nx.draw(self.G,pos=self.pos,node_size=700,with_labels=False,node_color="#FFFFFF")       # draws graph
        nx.draw_networkx_labels(self.G,self.pos,font_size=20)                                   # sets the nodes names
        plt.show()
    def isEdge(self, u, v):
        if ((u, v) in self.G.edges() or (v, u) in self.G.edges()):
            return True
        else:
            return False

    def DFS(self, start):
        self.runDFS(start, self.state)

    def runDFS(self, u, st):                                                                         
      st[u] = 'gray'
      print 'Traversing %s (%s)' % (u, st[u])
      nx.draw_networkx_nodes(self.G,self.pos,nodelist=[u],node_color='#969696',node_size=700)       # draws the current node and colors it gray
      nx.draw_networkx_labels(self.G, self.pos,labels={u:u},font_size=20)                           # draws its name
      plt.draw()                                                                                    # interatively draws on surface
      time.sleep(1)
      for v in self.G.nodes_iter():
        if self.isEdge(u,v) and st[v]=='white':
          nx.draw_networkx_edges(self.G,self.pos,edgelist=[(u,v)],edge_color='b', width=2.0)        # draws an edge between (u,v) and colors it blue
          plt.draw()
          self.runDFS(v, st)                                                                        # recursively goes through the currentlyy explored node
      st[u]='black'
      print 5*'-'+'Backtrace %s (%s)' % (u, st[u])
      time.sleep(1)
      nx.draw_networkx_nodes(self.G,self.pos,nodelist=[u],node_color='#000000',node_size=700)       # once it's done with current node, colors it black
      plt.draw()      
      self.already_visited.append(u)                                                                # adds current node to a list of already visited
      
    def connComponents(self):
        for i in self.G.nodes_iter():
            if self.state[i] == 'white':
                self.DFS(i)
                self.components.append(self.already_visited)                                        # assigns all the visited nodes to a new connected component
                boja = [(random.random(), random.random(), random.random())]*len(self.already_visited)              # generates random color for the connected component
                nx.draw_networkx_nodes(self.G,self.pos,nodelist=self.already_visited,node_color=boja,node_size=700) # and colors all of its nodes the same color
                plt.draw()
                self.already_visited = []                                                           # resets already_visited list because it enters in new connected component
                self.no_conncomp = self.no_conncomp+1
                if not self.already_visited:
                    print 3*'-'+str(self.no_conncomp)+'. connected component.'+3*'-'+'\n'
        print '\nTotal number of connected components: %d ' % self.no_conncomp
        print 'They are:'
        for i in self.components:
            print '\t'+str(i)
    
    def printGraph(self):
        print 'Number of nodes: %s' % self.G.number_of_nodes()
        print 'Number of edges: %s' % self.G.number_of_edges()
        print 'The edges are: %s\n' % self.G.edges()

    def printStates(self):
        print 'States:'
        for i in self.state.items():
            print i        

if __name__ == '__main__':
    g = GraphX()
    print '\n--- Graph G=(V,E) ---'
    g.printGraph()
#    print '--- Before DFS ---'
#    g.printStates()
    g.connComponents()
    raw_input("\nPress enter to exit...")
#    print '--- After DFS ---'
#    g.printStates()

