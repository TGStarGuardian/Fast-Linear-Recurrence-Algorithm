# Fast-Linear-Recurrence-Algorithm
Python implementations of algorithms from [this paper](https://inria.hal.science/hal-02917827/document) and some applications thereof, using algorithms from [this](https://www.researchgate.net/publication/220617048_On_the_Number_of_Nonscalar_Multiplications_Necessary_to_Evaluate_Polynomials) and [this](https://inria.hal.science/hal-03016034v3/document).
This repository contains the following algorithms:
* the least significant bit (LSB) algorithm to compute the N-th term of any linear recurrence sequence in time $(2M(d) + d)\log(N) + M(d)$, where $M(d)$ is the time needed to multiply two polynomials of degree $d$
* an algorithm to compute the power series expansion of $\frac{1}{Q}$ from $N - d + 1$ up to $N$, where $x^d$ is the largest term in $Q(x)$
* an algorithm to compute the N-th term of one or more linear recurrence sequences satisfying the same equation, with potentially different initial values. This program runs in time $O(M(d)log(N) + kd)$, where $k$ is the number of sequences
* an algorithm to compute the N-th term of the Fibonacci sequence with initial values 0 and 1 when N is a power of 2
* an algorithm to compute the N-th term of the Fibonacci sequence with initial values 0 and 1 when N is any number
* a Fiduccia style algorithm to produce a slice of terms $[F_N, \ldots, F_{N + d - 1}]$. The algorithm is an improvement of the original algorithm (for the original algorithm, see [this paper](https://epubs.siam.org/doi/10.1137/0214007)) with less polynomial multiplications. The time complexity is $(2M(d) + d) \log(N) + O(M(d))$, compared to Fiduccia's $(3M(d) + d) log(N) + O(M(d))$, as shown in the [aforementioned paper](https://inria.hal.science/hal-02917827/document).
* Paterson-Stockmeyer algorithm for polynomial evaluation with $2\sqrt(N)$ non-scalar multiplications
* Algorithm for computing characteristic polynomial of matrices in $O(Mat(n) \sqrt(Mat(n)))$ time, where $Mat(n)$ is time needed to compute a product of two square matrices of order $n$
* Matrix exponentiation in time $(2M(n) + n)\log(N) + O(Mat(n) \sqrt(Mat(n)))$
