addone([],[]).
addone([H|T], [N|T2]) :- N is H+1, addone(T, T2).

test_answer :-
    addone([3, 6, 7], L),
    writeln(L).
