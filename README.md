## py-2048
Program is simulating playing of game [2048](http://2048game.com/). There are available 3 strategies.

#### Random
At each turn is choosen one random side to slide.
#### Simple
If there are two number in row or column that can be connected this turn will be used. If there arent any random turn is used instead.
#### Stragery thinking few turns ahead
This strategy calculates score for each possible turn, best turn will be used. Because this strategy checks few steps to future, it is able to connect some numbers even in few turns.

### Usage
```python 2048.py -h```

Test of random and simple strategy, 10 games 
```python 2048.py -s -t 10```

Test of multiple levels of prediction 
```python 2048.py -l -t 3```

## py-2048
Program simuluje hranie hry [2048](http://2048game.com/). Dostupné sú 3 stratégie. Každá stratégia dosahuje lepšie výsledky ako predchádzajuca.

#### Náhodná
Na každom ťahu sa vyberie náhodný smer.
#### Jednoduchá
Ak sa daju spojiť dva čísla v riadku alebo stĺpci, tak sa spoja. Ak nieje žiaden takýto prípad, vykoná sa náhodný ťah.
#### Ktorá skúša niekoľko ťahov dopredu
Táto stratégia spočíta koľko bodov získa ktorým ťahom. Ale stratégia takto skúša niekoľko ťahov dopredu, takže je schopná odhadnúť ako sa dajú čísla spojiť aj pomocou niekoľkych ťahov.

### Použitie
```python 2048.py -h```

Otestovanie náhodnej a jednoduchej stratégie, 10 hier 
```python 2048.py -s -t 10```

Test rôzných úrovni predvídania ťahov 
```python 2048.py -l -t 3```