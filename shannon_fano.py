from Basic import *

global_shanon_fano = [        
        assign("A", 0),                 # count
        assign("B", 0),                 # err1
        assign("C", 0),                 # err2
        assign("D", 0),                 # sum

        alloc_matrix("B", 255, 3),      # stack
        assign("E", 0),                 # stack-count

        assign("F", 1),                 # ind_start
        assign("G", 1),                 # ind_end
        assign("H", 1),                 # column

        assign("I", 0),                 # split-at
        assign("J", 0),                 # found_middle
]
shannon_fano = main(
    pr_txt("Shannon Fano"),

    # number of codewords
    pr_txt("N:"),
    rd("N"),

    alloc_matrix("C", 1, "N"),      # codeword-list
    alloc_matrix("A", "N", 255),    # encoded matrix

    # read codeword probability
    cb_for("I", 1, "N", 1,
        pr_txt("enter p(i):"),
        rd("List 1[I]"),
    ),

    # sort ascending
    sortA("List 1"),

    # Init first iteration
    assign("E", "E+1"),
    assign("Mat B[E,1]", 1),
    assign("Mat B[E,2]", "N"),
    assign("Mat B[E,3]", 1),

    # Encode while stack not empty
    lbl("1"),
    cb_while("E>0",
        # Update variables
        assign("F", "Mat B[E,1]"),
        assign("G", "Mat B[E,2]"),
        assign("H", "Mat B[E,3]"),

        # Reset vars
        assign("A", 0),
        assign("J", 0),
        
        # Break condition
        cb_if(equal(sub("G", "F"), 1),
            _then=(
                assign("E", "E-1"),
                goto("1"),
            ),
        ),

        # Interval consist of two items
        cb_if(equal(sub("F", "G"), 1),
            _then=(
                assign("Mat A[F,H]", 1), # TODO: Fix dimenstion error (var F greater than matrix!)
                assign("Mat A[G,H]", 0),
                assign("E", "E-1"),
                goto("1"),
            ),
        ),

        # Get actual item sum
        assign("D", "Sum List 1"),

        cb_for("L", "F", "G", 1,
            cb_if("J=1",
                _then=(
                    assign("Mat A[L,H]", 0),
                ),
                _else=(
                    assign("Mat A[L,H]", 1),
                ),
            ),

            assign("A", "A+Mat C[1,L]"),

            cb_if(gt("A", mul("D", "0.5")+" And "+equal("J", 0)),
                _then=(
                    assign("B", sub("A", mul("D", "0.5"))),
                    assign("C", abslt(sub("A", "Mat C[1,L]", mul("D", "0.5")))),

                    cb_if(lore("B", "C"),
                        _then=( # TODO: fix if-else wrapper!
                            assign("I", "L"),
                        ),
                        _else=(
                            assign("I", "L-1"),
                            assign("Mat A[L,H]", 0),
                        ),
                    ),
                    assign("J", 1),
                ),
            ),
        ),

        # Push next iterations
        assign("H", "H+1"),

        # Dont increase stack to simulate 'pop' from stack
        assign("Mat B[E,1]", "F"),
        assign("Mat B[E,2]", "I"),
        assign("Mat B[E,3]", "H"),

        assign("E", "E+1"),
        assign("Mat B[E,1]", "I+1"),
        assign("Mat B[E,2]", "G"),
        assign("Mat B[E,3]", "H"),
    ),

    pr_var("Mat A"),

    globals=global_shanon_fano
)

if __name__ == '__main__':
    print(shannon_fano)