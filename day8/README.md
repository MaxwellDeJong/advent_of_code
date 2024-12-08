# Day 8

## Part 1
This problem was not too challenging. For my solution, I iterated across the antenna map and recorded the positions of the antenna of each frequence. For a given frequency, I could then form pairs of antennas and check if the resulting antinodes would fall inside the bounds.

## Part 2
The solution to this part only required a slight modification. Instead of using a single offset from each location, I looped over multiples of the distance difference until the resulting antinode was no longer within the bounds.
