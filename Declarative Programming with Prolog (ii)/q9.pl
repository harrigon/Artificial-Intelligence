split_odd_even(ListIn, ListA, ListB) :- split_odd_even(ListIn, ListA, ListB, 1).

split_odd_even([],[],[],_).
split_odd_even([H|TIn], [H|TA], ListB, N) :- Odd is mod(N,2), Odd == 1, N1 is N+1, split_odd_even(TIn, TA, ListB, N1).
split_odd_even([H|TIn], ListA, [H|TB], N) :- Even is mod(N,2), Even == 0, N1 is N+1, split_odd_even(TIn, ListA, TB, N1).






test_answer :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    writeln(B).

test_answer :-
    split_odd_even([1,2,3,5], A, B),
    write(A),
    writeln(B).
