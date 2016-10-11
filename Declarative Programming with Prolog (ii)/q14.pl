py_triple(A, B, C) :- 0 < A, 0 < B, 0 < C,
                      A =< B, B=< C,
                      Asq is A*A,
                      Bsq is B*B,
                      Csq is C*C,
                      AsqAddBsq is Asq + Bsq,
                      AsqAddBsq == Csq.


py_triple(A, B, C, Min, Max) :- between(Min, Max, A),
                                between(Min, Max, B),
                                between(Min, Max, C),
                                py_triple(A, B, C).

test_answer :-
    findall([A,B,C],py_triple(A,B,C,1,10),List),
    writeln(List).
