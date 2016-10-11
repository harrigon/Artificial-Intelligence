element(List, Index, Value) :- element(List, Index, Value, 0).

element([H|T], Index, H, Index).
element([H|T], Index, Value, N) :- N1 is N + 1, element(T, Index, Value, N1).

test_answer :-
    element([a, b, c, d, e, f], 2, X),
    writeln(X).

test_answer :-
    element([a, b, c, d], I, d),
    writeln(I).
