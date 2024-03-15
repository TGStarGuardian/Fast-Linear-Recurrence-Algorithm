# Fast-Linear-Recurrence-Algorithm
Python implementations of algorithms from [this paper](https://inria.hal.science/hal-02917827/document). In theory, algorithms presented in the paper offer better time complexities for solving some problems regarding linear recurrence equations.
This repository contains the following algorithms:
* the least significant bit (LSB) algorithm to compute the N-th term of any linear recurrence sequence in time $(2M(d) + d)log(N) + M(d)$, where $M(d)$ is the time needed to multiply two polynomials of degree $d$
* the most significant bit (MSB) algorithm to compute the N-th term of any linear recurrence sequence in time $3M(d)log(N)$
* an algorithm to compute the power series expansion of $\frac{1}{Q}$ from $N - d + 1$ up to $N$, where $x^d$ is the largest term in $Q(x)$
* an algorithm to compute the N-th term of more than one linear recurrence sequence satisfying the same equation, but differing in initial values. This program runs in time $O(M(d)log(N) + kd)$, where $k$ is the number of sequences
* an algorithm to compute the N-th term of the Fibonacci sequence with initial values 0 and 1 when N is a power of 2
* an algorithm to compute the N-th term of the Fibonacci sequence with initial values 0 and 1 when N is any number
* a Fiduccia style algorithm to produce a slice of terms $[F_N, \ldots, F_{N + d - 1}]$. The algorithm is an improvement of the original (see [this paper](https://epubs.siam.org/doi/10.1137/0214007)) algorithm with less polynomial multiplications. The time complexity is $(2M(d) + d) log(N) + O(M(d))$, compared to Fiduccia's $(3M(d) + d) log(N) + O(M(d))$, as shown in from the [aforementioned paper](https://inria.hal.science/hal-02917827/document).
