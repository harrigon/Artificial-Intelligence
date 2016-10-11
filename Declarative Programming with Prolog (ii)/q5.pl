swap_ends([], []).
swap_ends(In, Out) :- append([First|Mid], [Last], In), append([Last|Mid],[First], Out).




test_answer :-
    swap_ends([367], L),
    writeln('Wrong answer!').
