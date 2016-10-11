py_triple(A, B, C) :- 0 < A, 0 < B, 0< C,
                      A =< B, B =< C,
                      A2 is A*A, B2 is B*B, C2 is C*C,
                      Sum is A2 + B2,
                      Sum == C2.

test_answer :-
    py_triple(3,4,5),
    write('OK').
