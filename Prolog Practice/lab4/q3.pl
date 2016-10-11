reflection(point(X,Y), point(Y,X)).


test_answer :-
reflection(point(3, 6), point(6, 3)),
        writeln('OK').


test_answer :-
reflection(point(-5, 8), point(X, Y)),
        writeln(point(X, Y)).        
