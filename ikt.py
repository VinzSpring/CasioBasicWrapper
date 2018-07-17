from Basic.CasioBasic import *


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

        pr_var("List 1"),

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

    print(entropy)