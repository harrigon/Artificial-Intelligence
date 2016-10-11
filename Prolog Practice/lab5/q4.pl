twice([], []).
twice([A|T1], [A,A|T2]) :- twice(T1, T2).


test_answer :-
    twice([a, b, c, d], L),
    writeln(L).


test_answer :-
    twice(L, [1, 1, 2, 2, 3, 3]),
    writeln(L).
