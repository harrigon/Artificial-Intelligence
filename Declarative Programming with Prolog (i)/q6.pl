directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).

contains(X,Y) :- directlyIn(Y, X).
contains(X, Y) :- contains(X, Z), directlyIn(Y, Z).


test_answer1 :-
directlyIn(irina, natasha),
        writeln('OK').


test_answer2 :-
\+ directlyIn(irina, olga),
        writeln('OK').

test_answer3 :-
contains(katarina, irina),
        writeln('OK').

test_answer4 :-
contains(katarina, natasha),
        writeln('OK').
