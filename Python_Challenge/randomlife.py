import numpy
import pylab
import random
import json
import matplotlib.pyplot as plt
class GameOfLife:

   def __init__(self, N=64, T=10):
      """ Set up Conway's Game of Life. """
      # Here we create two grids to hold the old and new configurations.
      # This assumes an N*N grid of points.
      # Each point is either alive or dead, represented by integer values of 1 and 0, respectively.
      self.N = N
      self.old_grid = numpy.zeros(N*N, dtype='i').reshape(N,N)
      self.new_grid = numpy.zeros(N*N, dtype='i').reshape(N,N)
      self.T = T # The maximum number of generations

      # Set up a random initial configuration for the grid.
      for i in range(0, self.N):
         for j in range(0, self.N):
            if(random.randint(0, 100) < 15):
               self.old_grid[i][j] = 1
            else:
               self.old_grid[i][j] = 0
      
   def live_neighbours(self, i, j):
      """ Count the number of live neighbours around point (i, j). """
      s = 0 # The total number of live neighbours.
      # Loop over all the neighbours.
      for x in [i-1, i, i+1]:
         for y in [j-1, j, j+1]:
            if(x == i and y == j):
               continue # Skip the current point itself - we only want to count the neighbours!
            if(x != self.N and y != self.N):
               s += self.old_grid[x][y]
            # The remaining branches handle the case where the neighbour is off the end of the grid.
            # In this case, we loop back round such that the grid becomes a "toroidal array".
            elif(x == self.N and y != self.N):
               s += self.old_grid[0][y]
            elif(x != self.N and y == self.N):
               s += self.old_grid[x][0]
            else:
               s += self.old_grid[0][0]
      return s

   def play(self):
      print ("Welcome to the game of life")
      # Write the initial configuration to file.
      pylab.pcolormesh(self.old_grid)
      pylab.colorbar()
      pylab.savefig("generation0.png")
      x=self.old_grid.tolist()

      cur_state = {"0": x} 

      plt.plot(self.old_grid)
      plt.show()
      '''with open('config.json', 'w') as json_file:
        json.dump(cur_state, json_file)'''
      t = 1 # Current time level
      write_frequency = 1 # How frequently we want to output a grid configuration.
      while t <= self.T: # Evolve!
         print ("At time level %d" % t)
         #print (type(self.new_grid))

         # Loop over each cell of the grid and apply Conway's rules.
         for i in range(self.N):
            for j in range(self.N):
               live = self.live_neighbours(i, j)
               if(self.old_grid[i][j] == 1 and live < 2):
                  self.new_grid[i][j] = 0 # Dead from starvation.
               elif(self.old_grid[i][j] == 1 and (live == 2 or live == 3)):
                  self.new_grid[i][j] = 1 # Continue living.
               elif(self.old_grid[i][j] == 1 and live > 3):
                  self.new_grid[i][j] = 0 # Dead from overcrowding.
               elif(self.old_grid[i][j] == 0 and live == 3):
                  self.new_grid[i][j] = 1 # Alive from reproduction.

         # Output the new configuration.
         if(t % write_frequency == 0):

            pylab.pcolormesh(self.new_grid)
            pylab.savefig("generation%d.png" % t)

            plt.plot(self.new_grid)
            plt.show()
            plt.figure("Time - %d" % t)

         # The new configuration becomes the old configuration for the next generation.
         self.old_grid = self.new_grid.copy()

         # Move on to the next time level
         t += 1

if(__name__ == "__main__"):
   game = GameOfLife(N = 64, T = 10)
   game.play()
