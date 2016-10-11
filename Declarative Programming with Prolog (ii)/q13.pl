py_triple(A, B, C) :- 0 < A, 0 < B, 0 < C,
                      A =< B, B=< C,
                      Asq is A*A,
                      Bsq is B*B,
                      Csq is C*C,
                      AsqAddBsq is Asq + Bsq,
                      AsqAddBsq == Csq.

test_answer :-
    py_triple(3,4,5),
    write('OK').
