% Base de conocimiento

gana(bruja, guerrero).
gana(bruja, enano).
gana(bruja, elfo).

gana(elfo, enano).
gana(elfo, vampiro).

gana(enano, troll).
gana(enano, orco).

gana(troll, mago).
gana(troll, bruja).

gana(mago, dragon).
gana(mago, elfo).
gana(mago, vampiro).

gana(dragon, guerrero).
gana(dragon, enano).
gana(dragon, bruja).

gana(guerrero, troll).
gana(guerrero, orco).
gana(guerrero, enano).

gana(orco, vampiro).
gana(orco, mago).

gana(vampiro, bruja).
gana(vampiro, dragon).


tropa(guerrero).
tropa(mago).
tropa(elfo).
tropa(enano).
tropa(troll).
tropa(dragon).
tropa(orco).
tropa(vampiro).
tropa(bruja).

:- dynamic derrotado/2.

% Reglas
 ganador_combate(Atacante, Defensor) :-
     gana(Atacante, Defensor),
     agregar_enemigo_derrotado(Atacante, Defensor).
 
obtener_tropa_aleatoria(Enemigo) :-
    findall(Tropa, tropa(Tropa), Tropas),
    length(Tropas, N),
    N > 0,
    random(0, N, Index),
    nth0(Index, Tropas, Enemigo).

agregar_enemigo_derrotado(Atacante,Defensor) :-
    asserta(derrotado(Atacante,Defensor)).

obtener_enemigos_derrotados(Lista) :-
    findall((Atacante, Enemigo),
            (derrotado(AtacanteAtom, EnemigoAtom),
             atom_string(AtacanteAtom, Atacante),
             atom_string(EnemigoAtom, Enemigo)),
            Lista).