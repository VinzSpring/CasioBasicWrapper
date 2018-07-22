def exec():
    return 'Ù\n'


def pr_txt(txt):
    return '"' + txt + '"'


def pr_var(var):
    return str(var) + "Ø"


def assign(var, val):
    return str(val) + "ã" + str(var)


def rd(var):
    return assign(var, "?")


def main(*lines, globals=[]):
    return (exec()).join(globals) + exec() + (exec()).join(lines) + exec()


def cb_if(cond, _then, _else=None):
    cmd = "If " + cond + exec() + "Then " + exec().join(_then)
    if _else is not None:
        cmd += "\nElse " + "".join(_else) + exec()
    return cmd + exec() + "IfEnd"


def cb_for(var, _from, to, step, *lines):
    return "For " + assign(var, _from) + " To " + str(to) + " Step " + str(step) + exec() + \
           exec().join([str(x) for x in lines]) + exec() + "Next"


def cb_while(condition, *code):
    return "While " + condition + exec() + exec().join([str(x) for x in code]) + exec() + "WhileEnd"


def div(a, b):
    return "(" + str(a) + ")»(" + str(b) + ")"


def square(a):
    return a + "’"


def alloc_list(list_num, length):
    return assign("Dim List " + str(list_num), length)


def alloc_matrix(mat_name, i, j):
    return assign("Dim Mat " + mat_name, "{" + str(i) + "," + str(j) + "}")


def mult(*a):
    return "À".join(a)


def clear(var):
    return assign(var, 0)


def logab(a, b):
    return "log a(b)" + str(a) + "," + str(b) + ")"


def sortA(ls):
    return "SortA(" + str(ls) + ")"


def add(*a):
    return "+".join(a)

def lbl(label):
    return "Lbl " + str(label)

def goto(label):
    return "Goto " + str(label)