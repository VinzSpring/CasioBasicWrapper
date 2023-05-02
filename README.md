# CasioBasicWrapper

A collection of python monads for compiling Casio-Basic scripts in python.

## Example (read the libraray, it's self explanatory):
### assignments
```python
assign("C", 1337)
```
### Loops and conditions
```python
        cb_for(
            "I", 0, "N-1", 1,
            pr_var("I"),
        )
        
        cb_if(
            not_equal("Mat B[J,I]", 0),
            pr_txt("not 0"),
        )
```
### support for Matrices and Lists
```python
        alloc_matrix("C", "M", 1)
        assign("Mat C", mult("Mat B", "Mat A"))
```
### 1. Calculating the entropy of given characters given their probability
```python
    casio_basic_code = main(
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
    print(casio_basic_code)
```
