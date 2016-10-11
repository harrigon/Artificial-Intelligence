second([_,X|_], X).


test_answer :-
    second([cosc, 2, Var, beethoven], X),
    writeln(X).


test_answer :-
    \+ second([1], X),
    writeln('OK').

test_answer :-
  second([a, b, c, d], b),
  writeln('OK').

test_answer :-
    second(L, X),
    writeln('OK').
