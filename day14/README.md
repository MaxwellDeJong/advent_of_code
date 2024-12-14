# Day 14

## Part 1
The first part was fairly straightforward. Since each robot evolved independent of the others, we could independently calculate the final position of each robot. We can naively evolve the position using the velocity and use the modulo operator to apply the periodic boundary conditions to calculate the final position within the bathroom bounds.

## Part 2
The degree to which this problem was underspecified made this pretty interesting. My initial thought was to use the clues of the problem. Presumably, the bathroom break occurred after the lowest safety value encountered up until that point. So we could keep track of the points with the lowest safety values and look after those iterations to check if any trees were present. But how long does a bathroom break last? If it lasts 100 seconds and there are 10 local minima for the safety value, I would need to manually review 1,000 robot maps. And this still relies on a questionable assumption of bathroom break duration.

So instead, I thought more carefully about how we can detect a Christmas tree in the map without relying on manual review. I do not know the exact shape of this Christmas tree or how many sets of branches it would have. However, I determined that almost any recognizable Christmas tree would contain a very large number of simple triangles. So we could count the number of these triangles as the system evolved, and the iteration with the largest number of these triangles likely contained the Christmas tree. We could then validate this single map to check for a tree. This turned out to be a good approach that minimized the amount of manual review required.
