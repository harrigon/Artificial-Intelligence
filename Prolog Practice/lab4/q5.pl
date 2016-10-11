/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.


diagnosis(hard_lenses, Age, Astig, TearRate) :- normal_tear_rate(TearRate),
                                                Astig == yes,
                                                young(Age).
diagnosis(soft_lenses, Age, Astig, TearRate) :- normal_tear_rate(TearRate),
                                                Astig == no,
                                                young(Age).

diagnosis(no_lenses, Age, Astig, TearRate) :- low_tear_rate(TearRate).

test_answer :-
diagnosis(hard_lenses, 21, yes, 11),
        writeln('OK').

test_answer :-
diagnosis(X, 45, no, 4),
        writeln(X).

test_answer :-
diagnosis(X, 19, no, 5),
        writeln(X).
