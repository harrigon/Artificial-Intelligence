remove(X, ListIn, ListOut) :- remove(X, ListIn, ListOut, []).

remove(X, [], ListOut, ListOut).
remove(A, [A|T], ListOut, HelpList) :- remove(A, T, ListOut, HelpList).
remove(A, [B|T], ListOut, HelpList) :- append(HelpList, [B], L), remove(A, T, ListOut, L).





test_answer :-
    remove(d, [a, b, c], L),
    write(L).
    
test_answer :-
    remove(a, [], L),
    write(L).

test_answer :-
    remove(term2, [term1, term2, term3], [term1, term3]),
    write('OK').
