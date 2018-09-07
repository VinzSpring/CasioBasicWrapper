# CasioBasicWrapper

A collection of python monads for compiling Casio-Basic scriptsin python.

## Example:
### support for Matrices and Lists
```python
        alloc_matrix("C", "M", 1)
        assign("Mat C", mult("Mat B", "Mat A"))
```
### 1. Calculating the entropy of given characters given their probability
```python
    entropy = main(
        pr_txt("Entropy"),

        pr_txt("N?:"),
        rd("N"),
        pr_txt("sub intervals?:"),
        rd("C"),
        cb_if(
            not_equal("C", 0),
            assign("C", logab(2, "C"))
        ),

        # sum
        clear("A"),
        clear("B"),
        cb_for(
            "I", 0, "N-1", 1,
            pr_txt("enter p(i):"),
            rd("A"),
            assign("B", add("B", mult("A", add(logab(2, div(1, "A")), "C"))))
        ),

        pr_var("B"),
    )
```
