# What this is

The simplest non-trivial example I could come up with to illustrate that software concurrency is *hard* but has patterns to it.
- Atomic counter implemented using compare-and-swap.
- What is CAS?
  - Infinite consensus number
  - Universal construction
  - Primtive for lock-free and wait-free data structures
  - https://stackoverflow.com/questions/14758088/how-are-atomic-operations-implemented-at-a-hardware-level
- Threads race to atomically increment a shared counter using CAS.
- After finishing, they say "I'm done" by printing their ID to stdout.
- Any execution or run prints a permutation to stdout
- In theory, the operating system can interleave threads any which way it wants. This is why concurrency is hard. Way too many interleavings.
- But in practice, the OS is a deterministic software. There are probably patterns.
  - Very aggressive response to someone asking about OS-level determinism: https://unix.stackexchange.com/questions/65969/what-makes-the-linux-scheduler-seem-unpredictable
- Attempt to train a really *really* simple autoencoder on 100,000 runs of the above program.
- Plot AUC. Model produced isn't too bad.
