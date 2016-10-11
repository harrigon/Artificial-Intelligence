twice([], []).
twice([H|T], [H,H|Rest]) :- twice(T, Rest).

test_answer :-
    twice([a, b, c, d], L),
    writeln(L).
