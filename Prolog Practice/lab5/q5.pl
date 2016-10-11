swap_ends(List1, List2) :-append([First|Mid], [End], List1),
                          append([End|Mid], [First], List2).

test_answer :-
    swap_ends([a, b, c, d, e, f], L),
    writeln(L).

test_answer :-
    swap_ends(L, [term1, term2, term3, term4]),
    writeln(L).
