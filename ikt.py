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

    # print(entropy)

    global_shanon_fano = [
        alloc_list(1, "N"),
        alloc_matrix("M", "N", 255),
    ]
    shannon_fano = main(
        pr_txt("Shannon Fano"),

        # number of codewords
        pr_txt("N:"),
        rd("N"),

        # read codeword probability
        cb_for("I", 1, "N", 1,
               pr_txt("enter p(i):"),
               rd("List 1[I]"),
               ),

        # sort ascending
        sortA("List 1"),

        # find middle
        assign("A", "List 1[1]"),
        cb_for("I", 2, "N", 1,
               assign("A", add("A", "List 1[I]")),
               cb_if("(A>0.5) Or (A=0.5)",
                     assign("X", "|A-0.5|"),
                     assign("Y", "|0.5-A|"),  # TODO fix negative numer
                     pr_var("X"),
                     pr_var("Y"),
                     _else=(

                     )

                     ),
               ),

        globals=global_shanon_fano
    )

    trans_info = main(
        pr_txt("how many inputs?"),
        rd("N"),
        pr_txt("how many outputs?"),
        rd("M"),

        alloc_matrix("A", "N", 1),
        cb_for(
            "I", 1, "N", 1,

            pr_txt("P(X)?"),
            rd("Mat A[I,1]")
        ),

        alloc_matrix("B", "N", "M"),
        cb_for(
            "I", 1, "N", 1,
            cb_for(
                "J", 1, "M", 1,

                pr_txt("P(Y->X)?"),
                rd("Mat B[J,I]")
            )
        ),

        alloc_matrix("C", "M", 1),
        assign("Mat C", mult("Mat B", "Mat A")),
        pr_txt("P(Y):"),
        pr_var("Mat C"),

        clear("B"),
        cb_for(
            "I", 1, "M", 1,
            assign("B", "B+" + mult("Mat C[I,1]", logab(2, div(1, "Mat C[I,1]"))))
        ),
        pr_txt("H(Y):"),
        pr_var("B"),

        clear("C"),
        cb_for(
            "I", 1, "N", 1,

            cb_for(
                "J", 1, "M", 1,

                cb_if(
                    not_equal("Mat B[J,I]", 0),
                    assign(
                        "C",
                        add("C", mult("Mat A[I,1]", "Mat B[J,I]", logab(2, div(1, "Mat B[J,I]"))))
                    )
                )
            )
        ),

        pr_txt("H(Y->X):"),
        pr_var("C"),

        pr_txt("Ht:"),
        pr_var("(B-C)"),

        prgrm_name="TransInfo"
    )

    print(entropy)
