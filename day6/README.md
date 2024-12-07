# Day 6

## Part 1
The first part was straightforward enough, so I decided that I would create a proper object-oriented architecture to solve this first part. That (unsurprisingly) turned out to be a mistake for the next part, but it made for a nice solution to this particular problem. The solution itself was nothing fancy--evolve the guard according to the rules, keeping track of the visited locations, until the guard has left the mapped area.

## Part 2
I initially thought that I had discovered a nice way of tackling this second part. The idea was this: every simple loop has certain properties. Due to the simplicity of how the guard turns when facing an obstacle, every simple loop looks something like this:
  1. The guard hits an obstacle above it, causing it to move right for $n$ steps before it encounters the next obstacle.
  2. The guard moves down for $m$ steps until it encounters the next obstacle.
  3. The guard moves left for $n$ steps until it encounters the same obstacle.
  4. The guard moves $m$ steps up until it encounters the original obstacle.

This places a strong constraint on the position of relevant obstacles. So my plan was to iterate through the existing obstacles and determine which groups of 3 original obstacles plus one added obstacle would permit these cycles. Finally, I would determine which of these cycles are actually reachable from the initial conditions of the guard. Utilizing this symmetry made for a satisfying solution. Unfortunately, it does not lead to a correct solution. The issue is that this method only works for simple loops, where 4 obstacles are used. For more topologically complex loops, this algorithm will fail. And extending it to arbitrarily complex loop topologies did not seem trivial.

So in the end, I just ended up brute forcing the solution. I enumerated over all of the valid locations for the new obstacle and counted which encountered cycles. To determine if a cycle had occurred while the system evolved, I created a 3rd order tensor, where each spatial location indexed a list of visited directions. This history of spatial directions was updated as the system evolved, so that cycles could be detected if a spatial location with the current direction had already been recorded.

Algorithmically, the solution was not complicated. But the implementation was more difficult than necessary due to the OOP decisions made in Part 1. It is hard to design an object-oriented architecture and arrive at the right choice of abstractions without knowing the significant changes that will be made to the problem in the second half. For this reason, the implementation that was pleasing for Part 1 led to a more clunky implementation for this second half. It is possible that I would have guessed the correct the abstractions to make the design modular and extensible for the next part, but I should probably avoid the temptation of investing too much time in a satisfying architecture for the first part of the problem moving forward.

