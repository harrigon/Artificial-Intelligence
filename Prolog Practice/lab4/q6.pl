directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).

contains(X, Y):- directlyIn(Y, X).
contains(X, Y):- contains(X, Z), directlyIn(Y, Z).




test_answer :-
    contains(katarina, natasha),
    writeln('OK').
