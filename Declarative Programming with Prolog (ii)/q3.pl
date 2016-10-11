listtran([], []).
listtran([H1|T1], [H2|T2]):- tran(H1, H2), listtran(T1, T2).


tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

test_answer :-
    listtran([eins, neun, zwei], X),
    writeln(X).

test_answer :-
    listtran([], []),
    writeln('OK').

test_answer :-
    listtran(X, [one, seven, six, two]),
    writeln(X).

test_answer :-
    listtran(L1, L2),
    writeln('OK').

tran(1, one).
tran(2, two).
tran(3, three).

test_answer :-
    listtran([1, 2, 3], X),
    writeln(X).
