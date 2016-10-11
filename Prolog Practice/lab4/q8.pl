mirror(leaf(X), leaf(X)).
mirror(tree(X,Y), tree(A,B)) :-mirror(Y, A), mirror(X, B).





test_answer :-
    mirror(tree(leaf(foo), leaf(bar)), tree(leaf(bar), leaf(foo))),
    write('OK'),
    halt.

test_answer :-
    write('Wrong answer!'),
    halt.
