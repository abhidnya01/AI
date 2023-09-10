female(pam).
female(liz).
female(pat).
female(ann).
male(jim).
male(bob).
male(tom).
male(peter).
parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
parent(bob,peter).
parent(peter,jim).
mother(X,Y):- parent(X,Y),female(X).
father(X,Y):- parent(X,Y),male(X).
haschild(X):- parent(X,_).
sister(X,Y):- parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.

%% OUTPUT 1
%%| ?- father(X, Y).
%% father(X, Y).
%% X = tom
%% Y = bob ? a
%% X = tom
%% Y = liz

%% X = bob
%% Y = ann

%% X = bob
%% Y = pat

%%  X = bob
%%  Y = peter

%%  X = peter
%%  Y = jim


%% OUTPUT 2

%%| ?- parent(X, Y).
%% parent(X, Y).
%% X = pam
%% Y = bob ? a
%% X = tom
%% Y = bob

%% X = tom
%% Y = liz

%% X = bob
%% Y = ann

%% X = bob
%% Y = pat

%% X = pat
%% Y = jim

%% X = bob
%% Y = peter
%% X = peter
%% Y = jim


%% OUTPUT 3

%% | ?- haschild(X).
%% haschild(X).
%% X = pam ? a
%% X = tom

%% X = tom

%% X = bob

%% X = bob

%% X = pat

%% X = bob

%%X = peter
