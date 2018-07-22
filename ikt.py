from Basic import *


if __name__ == '__main__':
    global_vars = [
        assign("D", 10),
    ]

    prgrm = main(
        pr_txt("hello user!"),
        pr_txt("global vars:"),
        pr_txt("D:"), pr_var("D"),

        alloc_matrix("A", 2, 2),
        pr_var("Mat A"),

        alloc_list(1, 10),
        pr_var("List 1"),

        rd("A"),
        assign("B", 51),
        assign("C", "A+B"),
        pr_var("C"),
        cb_for(
            "A", 1, 30, 1,
            pr_var("A")
        ),
        assign("A", 1),
        cb_while(
            "A<10",
            assign("A", "A+1"),
            pr_var("A")
        ),

        globals=global_vars
    )

    entropy = main(
        pr_txt("Entropy"),

        # pr_txt("sub intervals:"),
        # rd("C"),
        pr_txt("N:"),
        rd("N"),
        #sum
        clear("A"),
        clear("B"),
        cb_for(
            "I", 0, "N-1", 1,
            pr_txt("enter p(i):"),
            rd("A"),
            assign("B", "B+" + mult("A", logab(2, div(1, "A"))))
        ),

        pr_var("B"),
    )

    #print(entropy)



    global_shanon_fano = [        
        assign("A", 0),                 # count
        assign("B", 0),                 # err1
        assign("C", 0),                 # err2
        assign("D", 0),                 # sum

        alloc_matrix("B", 255, 3),      # stack
        assign("E", 0),                 # stack-count

        assign("F", 0),                 # ind_start
        assign("G", 0),                 # ind_end
        assign("H", 1),                 # column

        assign("I", 0),                 # split-at
        assign("J", 0),                 # found_middle
    ]
    shannon_fano = main(
        pr_txt("Shannon Fano"),

        # number of codewords
        pr_txt("N:"),
        rd("N"),

        alloc_list(1, "N"),             # codeword-list
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
        cb_while("E>-1",
            # Update variables
            assign("F", "Mat B[E,1]"),
            assign("G", "Mat B[E,2]"),
            assign("H", "Mat B[E,3]"),

            # Reset vars
            assign("A", 0),
            assign("J", 0),
            
            # Break condition
            cb_if("(G-F)=1",
                _then=(
                    assign("E", "E-1"),
                    goto("1"),
                ),
            ),

            # Interval consist of two items
            cb_if("(F-G)=1",
                _then=(
                    assign("Mat A[F,H]", 1),
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

                assign("A", "A+List 1[L]"),

                cb_if("A>=(Dx0.5) and J=0",
                    _then=(
                        assign("B", "A-(Dx0.5)"),
                        assign("C", "|(A-List 1[L])-(Dx0.5)|"),

                        cb_if("B<=C",
                            _then=(
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

    trans_info = main(

        pr_txt("how many inputs?"),
        rd("N"),

        #accumulator
        clear("A"),
        cb_for(
            "I", 0, "N", 1,

            pr_txt("p(X):"),
            rd("P"),

            pr_txt("p(Y|X)"),
            rd("B"),

            assign(
                "A", add(
                    "A",
                    mult(
                        "P", "B", logab(2, div(1, "B"))
                    )
                )
            )
        ),

        pr_txt("H(Y|X):"),
        pr_var("A"),
    )

    print(shannon_fano)