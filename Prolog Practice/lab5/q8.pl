remove(X, ListIn, Listout) :- remove(X, ListIn, ListOut, []).

remove(X, [], ListOut, ListOut).
remove(A, [A|T], ListOut, HelpList) :- remove(A, T, ListOut, HelpList).
remove(A, [B|T], ListOut, HelpList) :- append(HelpList, [B], L), remove(A, T, ListOut, L).

test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    writeln(L).
