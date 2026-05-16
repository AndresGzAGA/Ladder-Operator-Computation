In the context of quantum mechanics, ladder operators are operators which increase or decrease the eigenvalue of a given eigenvector. In Dirac notation, these fulfill the relations
$$a^\dagger |n\rangle = \sqrt{n+1}|n+1\rangle, \quad a |n\rangle = \sqrt{n}|n-1\rangle \qquad (1).$$
Here, the ket "n" is an eigenstate with eigenvalue n, the operator "a dagger" is the creation opperator, and the operator "a" is the annihilation operator. The eigenstates can have eigenvalues `n` from 0 to infinity, and the eigenvalue 0 corresponds to the vacuum. When the annihilation operator is applied to the vacuum, the result is zero:
$$a|0\rangle = 0 \qquad (2).$$
The commutator of the operators is
$$[a,a^\dagger] = a a^\dagger-a^\dagger a = 1, \qquad (3).$$
These operators also define a number operator N, with the relations
$$N = a^\dagger a, \quad N|n\rangle = n|n\rangle, \qquad (4),$$
and commutators
$$[N,a^\dagger] = a^\dagger, \quad [N,a] = -a, \qquad (5).$$

Say you have an operator `O` with the same ammount of creation and annihilation operators. For example:
$$\hat{O} = aaa^\dagger a^\dagger.$$
If we want to exress this operator in terms of the number operator, there are various way you can do it, but it usually involves commuting the operators until you can match a number operator, and using the commutation relations (3) and (4) everytime you commute two operators. For example, for this operator:
$$\hat{O} = a(a^\dagger a+1)a^\dagger = a(N+1)a^\dagger = aa^\dagger(N+2)=(N+1)(N+2).$$
Finally, expanding the polynomial gives
$$\hat{O} = 2+3N+N^2.$$

This code automates the calculation for an arbitrary operator with an equal number of creation and annihilation operators.

Code functionality:

**Input Validation**
File: src/utilities/input.py

This utility validates the input list `O`, ensuring that it is a list which represents an operator sequence formed by an equal number of creation and annihilation operators.

The code checks that:
* All elements in `O` are either "a" or "b" (representing annihilation and creation operators respectively).
* The length of `O` is even.
* The number of creation and annihilation operators is equal.

**Number Operator Addition**
File: src/utilities/misc.py

The helper function `def N_str_sum(N_str,n)` takes as an input a string representation of the number operator plus a constant `N_str = "N+c"`, performs the addition to an integer `n`, and returns the string representation of the result.

The code works by first identifying wheter the constant is zero (`len(N_str) == 1`). If this is the case, it just returns the string `"N+n"`, where care is taken for appropiately representing an addition or substraction, depending on whether `n` is positive or negative.

If the constant is not zero, the code performs the addition and stores it in the variable `s`. Depending on whether the result is positive, negative or zero, the appropiate string representation with the addition, substraction, or just `"N"` is respectively returned.

**Commutation and matching of Operators**
Lines starting from `while sum(o == "a" for o in O) + sum(o == "b" for o in O) > 0:` to before the line `coeff = [0]*(len(O)+1)` in src/main.py

This section iteratively matches the ladder operators in the list `O` with the number operator, and commutes them by using the commutation relations defined in equations (3) and (5) in order to match all of the ladder operators into number operators.

This section achieves its purpose by running in a while loop that repeatedly performs the following procedure until there are no more ladder operators:
1.  It pairs adjacent annihilation and creation operators (either "b" followed by "a" or vice versa) and replaces them with the number operator "N" or "N+1" accordingly.
2. It then commutes all of the number operators so that they are on the right side of the operator sequence. For this, it uses a while loop with the element count `n` and the index count `i`. The index identifies where there is a number operator, where a for loop is performed in order to move it to the right side of the list. On each movement, the commutation relations (3) and (5) are re-aranged in the form $$Na = a(N-1)$$ and $$Na^\dagger = a^\dagger(N+1)$$ so that each time the number operator is commuted to the right, a constant -1 or 1 is added depending on the operator. This is done via the helper function `N_str_sum` of the past section. The commutation is freely done when the other operator is also a number operator, because these commute. The index `i` goes back one step every time it finishes re-aranging a number operator in order to avoid missing the other operator which was commuted in its place. The counter `n` accounts for all operators.

**Polynomial distinction**
Lines starting from `coeff = [0]*(len(O)+1)` to before the line `for n in range(m+1,len(coeff)-1):` in src/main.py.

This section of the code distinguishes the resultant number operator terms which are or the composite form `"N+c"` with respect to the ones which are of the single form `"N"`.

The section first initializes the coefficients list `coeff` which will store the coefficients of the expanded number operator polynomial. The last term is readily set as `1` because it corresponds to the largest exponent which is the result from multiplying all of the number operators in each factor.

The section then defines the variable `m` which counts the operators of the form `"N"` which can be readily expanded, and the list `comp` with the string representation of the number operators with the form `"N+c"`. The variable `N = len(comp)-1` is initialized as the last possible index of that list. If `m` is also the length of `O`, then the polynomial is just `N**m`, so the corresponding string representation is returned in that case. If not, then the code proceeds with the computation of each coefficient.

**Helper function**
File: src/utilities/misc.py
The helper function `prod_except(indices, comp)` returns the products of all constants `"c"` in the composite terms `"N+c"` except for the indices in the list `indices`. This helper function is used to compute the polynomial expansion, starting with the coefficient `coeff[m] = prod_except([])` which is the first term when factorizing the `N**m` operators.


**Polynomial expansion**

Lines starting from `for n in range(m+1,len(coeff)-1):` to before the line `polynomial = ""`

This section performs the polynomial expansion of the composite terms `"N+c"`, taking into account the factorization of the terms `N**m`, and saving the result in `coeff`.

The section starts with a for loop over the coefficients of `N**n`. It starts from `m+1` because of the terms `N**m` and because the coefficient `n=m` was computed before the loop. The loop starts defining an index group which goes from `0` to `n-m`. This list is used as an input in the helper function `prod_except` and it accounts for the indices of the terms which will be multiplied by `N` instead of the constant `c` when expanding the composite factors `"N+c"`.

Having accounted for the first possible combination in `indices`, the code iterates all of the different possible combinations of indices corresponding to the coefficient. This is done by consecutively increasing the value of the right-most index in the combination until reaching the maximum value `N = len(comp)-1`. When this value is reached, either all of the combinations are covered (when the `indices` list has length 1), or the next possible index `i-j` to the left is increased by one without going over the maximum value `N`. When doing this, the indices to the right are reset to their minimum values such that the list is in an increasing order. This algorithm produces all possible combinations of indices of length `n-m` which go from 0 to `N` without repetition. With the use of the helper function `prod_except`, this sums over all of the terms which add up to the relevant coefficient of `N**n`.

**Polynomial String Construction**
File: src/utilities/output.py
Lines from `polynomial = ""` to the end of the function

This section constructs the final polynomial string by iterating over the calculated coefficients and assembling the corresponding terms.

The polynomial string is saved in the variable `polynomial`. The code loops over the non-zero coefficients (from `m` on), and adds the string representation of the coefficient times the exponent of `N`. Care is taken for correctly representing the constant term `coeff[0]` without an exponent of `N`, the linear term of `N` without an exponent, and negative coefficients represented as substraction. The resulting string is returned at the end of the function.