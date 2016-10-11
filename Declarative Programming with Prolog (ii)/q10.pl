merge([], [], []).
merge(ListA, [], ListA).
merge([], ListB, ListB).
merge([HA|TA], [HB|TB], [HA|T]) :- HA < HB, merge(TA, [HB|TB], T).
merge([HA|TA], [HB|TB], [HB|T]) :- merge([HA|TA], TB, T).


test_answer :-
    merge([3, 6, 7], [1, 2, 3, 5, 8], L),
    writeln(L).
