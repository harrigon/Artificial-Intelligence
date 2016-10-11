addone([],[]).
addone([H|T], [(N)|Rest]) :- addone(T, Rest), N is H+1.

test_answer :-
    addone([3, 6, 7], L),
    writeln(L).
