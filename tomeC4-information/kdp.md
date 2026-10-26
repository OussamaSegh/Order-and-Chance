# Description

In 1948 Claude Shannon showed that information can be measured in bits, and that the measure answers two practical questions exactly: how short a message can be made, and how fast it can be sent through a noisy channel without error. Noise, he proved, need not cause errors at all; it only lowers the rate. Finding codes that reach his limits took fifty years. Meanwhile cryptography became mathematics too: in 1976 two researchers showed how strangers can agree on a secret in public, and in 1994 a third showed that a quantum computer could break their methods. This book tells these stories and proves their theorems.

Twelve chapters. Entropy, mutual information, divergence, Fano's and Pinsker's inequalities, and counting with entropy. Compression: Huffman, arithmetic and Lempel-Ziv coding, and why random data cannot be compressed. Noisy channels: capacity and Shannon's coding theorem with its converse. Kolmogorov complexity and the incompressibility method. Linear codes: Hamming and Golay codes, the MacWilliams identity and the lattice E8. Algebraic codes: Reed-Solomon and BCH codes, and list decoding. Codes on graphs: low-density parity-check codes, expander codes and polar codes. Secrecy and pseudorandomness: perfect secrecy, one-way functions, hard-core bits and pseudorandom generators. Public keys: Diffie-Hellman, RSA, elliptic curves, signatures, and the algorithms that attack them. Lattices and post-quantum cryptography: the LLL algorithm and learning with errors. Zero-knowledge proofs, commitments, secret sharing and secure computation. Quantum computing: the quantum Fourier transform, Shor's factoring algorithm and Grover's search.

Every theorem is proved in full, except for a few landmarks clearly labelled as quoted. Every chapter opens with a story and a question to think about, and has exercises graded by difficulty, each with a hint and a solution that first explains how to find the idea and then writes it up. Figures show the constructions, research papers come with reading guides, and every chapter ends with its sources.

Each chapter comes with a substantial Python notebook that makes the mathematics run: compressors, random codes approaching capacity, Reed-Solomon and list decoders, a peeling decoder, attacks on toy cryptosystems, LLL breaking a knapsack, a learning-with-errors scheme, secret sharing, and a quantum computer simulated on a laptop that factors 15 and 21.

The book is written for the pleasure of seeing how far mathematics can carry a message. It is the fourth volume of the computing track of a series that goes from the foundations of number theory, algebra and probability to the edge of research.

# Keywords

information theory with full proofs
error-correcting codes coding theory
cryptography mathematics RSA elliptic curves
Shannon entropy channel capacity
lattice cryptography learning with errors
quantum computing Shor algorithm Grover
zero-knowledge proofs secret sharing
