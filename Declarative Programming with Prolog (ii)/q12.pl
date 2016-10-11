inside(Min, Max, N) :- Min =< Max, N = Min.
inside(Min, Max, N) :- Min < Max, Next is Min + 1, inside(Next, Max, N).

test_answer :-
    findall(X, inside(1, 3, X), List),
    writeln(List).
