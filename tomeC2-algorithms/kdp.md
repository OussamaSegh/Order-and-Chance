# Description

In 1844 Gabriel Lamé asked how many steps Euclid's algorithm needs, and so began the mathematics of how fast things can be computed. This book tells that story: what can be computed quickly, how to prove it, and how to prove that nothing quicker exists. Every procedure in it comes with a proof that it is correct and a proof of how long it takes.

Twelve chapters. Measuring: models of computation, the master theorem, amortised analysis, and lower bounds by information and by adversaries, including Lewis Carroll's complaint about tennis tournaments. Sorting, selection and sorting networks, with Batcher's bitonic network, drawn on the cover. Data structures: heaps, balanced trees, universal and perfect hashing, union-find. Graph search, connectivity and shortest paths. Dynamic programming, from edit distance to the travelling salesman. Flows and matchings, up to Edmonds' blossoms, the paper that made polynomial time the definition of efficiency. Linear programming and duality. Randomised computation: Karger's minimum cut, polynomial identity testing, balls into bins, streaming. Algebraic computation: Karatsuba, Strassen, fast polynomial arithmetic. Number-theoretic computation: Miller-Rabin and the AKS theorem that primality is in polynomial time. Strings: Knuth-Morris-Pratt, suffix arrays and the Burrows-Wheeler transform. Approximation and online computation: Christofides, Goemans-Williamson, paging and multiplicative weights.

Every theorem is proved in full. Every chapter opens with a story and a question to think about, and has exercises graded by difficulty, each with a hint and a solution that first explains how to find the idea and then writes it up. Figures show the constructions, research papers come with reading guides, and every chapter ends with its sources.

Each chapter comes with a substantial Python notebook that implements its methods from scratch, checks them against brute force and against the proved bounds, and plays the adversaries of the lower bounds against real programs.

The book is written for the pleasure of seeing why things are true. It is the second volume of the computing track of a series that goes from the foundations of number theory, algebra and probability to the edge of research.

# Keywords

analysis of running time with proofs
master theorem amortised analysis
sorting lower bounds adversary arguments
dynamic programming graph search
network flows linear programming
randomised computing universal hashing
primality testing string matching
