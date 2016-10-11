merge([], [], []).
merge(ListA, [], ListA).
merge([], ListB, ListB).
merge([HA|TA], [HB|TB], [HA|T]) :- HA < HB, merge(TA, [HB|TB], T).
merge([HA|TA], [HB|TB], [HB|T]) :- merge([HA|TA], TB, T).


split_odd_even(ListIn, ListA, ListB) :- split_odd_even(ListIn, ListA, ListB, 1).

split_odd_even([],[],[],_).
split_odd_even([H|TIn], [H|TA], ListB, N) :- Odd is mod(N,2), Odd == 1, N1 is N+1, split_odd_even(TIn, TA, ListB, N1).
split_odd_even([H|TIn], ListA, [H|TB], N) :- Even is mod(N,2), Even == 0, N1 is N+1, split_odd_even(TIn, ListA, TB, N1).

merge_sort([],[]).
merge_sort([A],[A]).
merge_sort(ToSort, Sorted) :- split_odd_even(ToSort, Odd, Even), merge_sort(Odd, SortedOdd), merge_sort(Even, SortedEven), merge(SortedOdd, SortedEven, Sorted).


test_answer :-
    merge_sort([4,3,1,2], L),
    writeln(L).
