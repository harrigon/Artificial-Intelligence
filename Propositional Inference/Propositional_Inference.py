import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    Author: Kourosh Neshatian
    Last Modified: 31 Jul 2015

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = r"\s*(?P<HEAD>{ATOM})\s*".format(**locals())
    BODY   = r"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*".format(**locals())
    CLAUSE = r"{HEAD}(:-{BODY})?\.".format(**locals())
    KB     = r"^({CLAUSE})*$".format(**locals())

    #assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")
        
        
        
def forward_deduce(knowledge_base):
    
    C = set()
    
    to_prove = list(clauses(knowledge_base))
    set_changed = True
    #print(to_prove)
    while set_changed == True:
        set_changed = False
        for rule in to_prove:
            unappendable = False
            for atom in rule[1]:
                if atom not in C:
                    unappendable = True
            if (unappendable == False) and (rule[0] not in C):
                C.add(rule[0])
                set_changed = True     
    return C
