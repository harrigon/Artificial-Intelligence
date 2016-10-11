element(L, I, V) :- element(L, I, V, 0).
element([V|_], I, V, I).
element([H|T], I, V, N) :- N1 is N+1, element(T, I, V, N1).





test_answer :-
    element([a, b, c, d, e, f], 2, X),
    writeln(X).


test_answer :-
    element([a, b, c, d], I, d),
    writeln(I).
