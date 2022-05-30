---
title: Interfaces
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr), MINES ParisTech"
date: "Licence : [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
# author: ""
# license: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
---

ℹ️ Il est question dans ce document d'**interfaces de programmation applicative**
(🇺🇸 : **Application Programming Interface** ou **API**[^IPA]) variées : des interfaces
Python bien sûr, mais aussi des interfaces en ligne de commande et des
interfaces Web.

Ce projet fait suite à l'étude du 😷 [modèle épidémiologique SIR].

[modèle épidémiologique SIR]: https://boisgera.github.io/python-advanced-companion/tps/fonctions/

[^IPA]: L'acronyme **IPA** désigne 🍺 [tout autre chose](https://en.wikipedia.org/wiki/India_pale_ale).

## 🖥️ Dans le terminal

### Ligne de commande

Où l'on conçoit une interface en ligne de commande 
(🇺🇸 : **Command-Line Interface (CLI)**) pour obtenir les résultats de
simulation de notre modèle épidémiologique.


#### 🚀 Ligne de commande

Développez un programme Python `SIR.py` qui affiche l'évolution jour par jour 
et pendant un an de la population de personnes infectées :

``` bash
$ python SIR.py
1.0
1.0723973837364937
1.1497875982707628
...
0.3091773334306973
0.312319093274788
0.3155338502766228
```

#### ✨ Solution

::: collapse

``` python
# Third-Party Librairies
import numpy as np
from scipy.integrate import solve_ivp

WEEK = 7
YEAR = 365

N = 100
beta = 1 / (WEEK)
gamma = 1 / (2 * WEEK)
omega = 1 / YEAR

S0, I0 = 99.0, 1.0
R0 = N - S0 - I0
T_SPAN = (0.0, YEAR)

def dSIR(t, SIR):
    S, I, R = SIR
    dS = omega * R - beta * I * S / N
    dI = beta * I * S / N - gamma * I
    dR = gamma * I - omega * R  
    return (dS, dI, dR)

if __name__ == "__main__":
    results = solve_ivp(
        dSIR, 
        t_span=T_SPAN, 
        y0=(S0, I0, R0), 
        dense_output=True
    )
    sol = results["sol"]
    t = np.arange(0, YEAR)
    S, I, R = sol(t)
    for I_ in I:
        print(I_)
```

:::

### Sparklines

On souhaite offrir en option un affichage "graphique" permettant 
d'interpréter plus facilement les résultats de la simulation.
Nous allons pour ce faire utiliser des ✨ [sparklines] et 
dans cette optique, exploiter le projet [spark].

#### 🚀 Clone, Install, Test

  - Cloner le dépôt github du projet spark sur votre machine. 

  - Installer spark dans votre environnement en exécutant la commande

    ```
    python setup.py install
    ``` 

    ou 

    ```
    pip install .
    ``` 

    dans le répertoire racine de ce projet.

  - Tester les interfaces en ligne de commande et Python de cet outil.

#### 🚀 "Forkez" le projet

Spark serait plus facile à utiliser s'il acceptait directement des données
sous forme de nombres flottants et pas uniquement des entiers.

  - Forkez le projet sur GitHub. 
  
  - Ajoutez-lui cette fonctionnalité.

  - Mettez à jour les fichiers `README.md` et `setup.py` en conséquence.

  - Puis déployez cette nouvelle version de spark dans votre environnement.

#### Solution

::: collapse

Le fichier `spark.py` modifié :

``` python 
# -*- coding: utf-8 -*-

"""
Spark
================================================================================

A port of @holman's [spark] project for Python 3.

[spark]: https://github.com/holman/spark
"""

import sys

ticks = " ▁▂▃▄▅▆▇█"


def spark_string(floats, fit_min=False):
    """Returns a spark string from given iterable of floats.
    
    Keyword Arguments:
    fit_min: Matches the range of the sparkline to the input integers
             rather than the default of zero. Useful for large numbers with
             relatively small differences between the positions
    """
    min_range = min(floats) if fit_min else 0
    step_range = max(floats) - min_range
    step = (step_range / float(len(ticks) - 1)) or 1
    return "".join(ticks[int(round((f - min_range) / step))] for f in floats)


def spark_print(floats, stream=None, fit_min=False):
    """Prints spark to given stream."""
    if stream is None:
        stream = sys.stdout
    stream.write(spark_string(floats, fit_min=fit_min) + "\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        sparks = [float(arg) for arg in sys.argv[1:]]
        spark_print(sparks)
        print
    else:
        usage = print(
            """Spark: ▁▂▃▅▂▇ in your shell

Usage:
  python -m spark [spaces separated values]

Examples:"""
        )

        print("  $ python -m spark 1 5 22 13 53")

        spark_print([1, 5, 22, 13, 53])

        print("  $ python -m spark 0 30 55 80 33 150")

        spark_print([0, 30, 55, 80, 33, 150])

        print("  $ python -m spark 0.0 0.25 0.5 0.75 1.0")

        spark_print([0.0, 0.25, 0.50, 0.75, 1.0])

```

Le fichier `setup.py` associé (avec la version mise à jour) :

``` python 
# File setup.py
from distutils.core import setup

setup(
    name="spark",
    version="1.1",
    description="Sparklines with Python 3",
    author="Sébastien Boisgérault",
    author_email="Sebastien.Boisgerault@mines-paristech.fr",
    url="https://github.com/boisgera/spark.py",
    py_modules=["spark"],
)

```

et finalement le contenu du `README.md` faisant état de la nouvelle fonctionnalité :


> # Spark
> 
> ### Sparklines with Python 3
>
> See? Here's a graph of your productivity gains after using spark: ▁▂▃▅▇
>
> ## Install
>
> The original [spark](https://github.com/holman/spark),
> [by Zach Holman](https://github.com/holman/spark/blob/master/LICENSE.md) 
> is a [shell script](https://github.com/holman/spark/blob/master/spark)
> (to be dropped in a directory that's in your `$PATH`).
>
> This Python 3 port can be installed with:
>
>     $ python setup.py install
>
>
> ## Usage
>
> ### Command-line interface
>
>     $ python -m spark.py 0.01 29.5 55 80.0 33 150
>      ▂▃▄▂█
>
>
> ### Python interface
>
>     >>> from spark import spark_print
>     >>> spark_print([0.01, 29.5, 55, 80.0, 33, 150])
>      ▂▃▄▂█

:::

#### 🚀 Intégration

Faites en sorte que notre application affiche des sparklines représente 
l'évolution du niveau d'infection lorsque l'option `--sparklines` est
sélectionnée :

``` bash
$ python SIR.py --sparklines
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▂▂▂▂▂▂▂▃▃▃▃▃▃▃▄▄▄▄▄▅▅▅▅▅▆▆▆▆▆▇▇▇▇▇▇▇██████████████████▇▇▇▇▇▇▇▇▇▆▆▆▆▆▆▆▅▅▅▅▅▅▅▄▄▄▄▄▄▄▄▄▃▃▃▃▃▃▃▃▃▃▃▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
```

#### ✨ Solution

::: collapse

``` python
# Python Standard Library
import sys

# Third-Party Librairies
import spark
...

...

if __name__ == "__main__":
    results = solve_ivp(
        dSIR, 
        t_span=T_SPAN, 
        y0=(S0, I0, R0), 
        dense_output=True
    )
    sol = results["sol"]
    t = np.arange(0, YEAR)
    S, I, R = sol(t)

    if "--sparklines" in sys.argv[1:]:
        spark.spark_print(I)
    else:
        for I_ in I:
            print(I_)
```

:::


[sparklines]: https://en.wikipedia.org/wiki/Sparkline 
[spark]: https://github.com/boisgera/spark.py

### Gestion des arguments

#### 🚀 Plus d'options

  - Etudier les fonctionnalités proposées par la bibliothèque [typer]. 
    On pourra se contenter de lire l'[exemple minimal] de d'introduction
    et la section consacrée aux [options avec aide].

  - Réimplementez la fonctionnalité des sparklines en utilisant `typer`
    plutôt que `sys.argv`. Vérifiez au passage que `typer` vous donne
    "gratuitement" le support pour l'option `--help`.

  - Profitez de cette migration vers `typer` pour permettre à l'utilisateur 
    de changer la valeur du taux de contagion :

    ``` bash
    $ python SIR.py --sparklines --beta=0.8
    ▁▂▃▅▆▇███▇▇▇▆▆▅▅▅▄▄▄▄▃▃▃▃▃▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
    ```                                                                                                 
    ``` bash
    $ python SIR.py --sparklines --beta=0.05
    ███▇▇▇▇▇▇▇▆▆▆▆▆▆▆▅▅▅▅▅▅▅▅▅▄▄▄▄▄▄▄▄▄▄▄▄▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
    ```            

#### ✨ Solution 

::: collapse

Initialement pour migrer vers `typer` :

``` python
...

# Third-Party Librairies
import typer
...

...

def main(
  sparklines: bool = typer.Option(False, help="Output sparklines")
):
    results = solve_ivp(
        dSIR, 
        t_span=T_SPAN, 
        y0=(S0, I0, R0), 
        dense_output=True
    )
    sol = results["sol"]
    t = np.arange(0, YEAR)
    S, I, R = sol(t)

    if sparklines:
        spark.spark_print(I)
    else:
        for I_ in I:
            typer.echo(I_)

if __name__ == "__main__":
    typer.run(main)
```

puis pour supporter l'option `--beta` :

``` python
...

BETA = beta = 1 / (WEEK)

...

def main(
    sparklines: bool = typer.Option(False, help="Output sparklines"),
    beta: float = typer.Option(BETA, help="Contagion rate")
):
    globals()["beta"] = beta
    results = solve_ivp(dSIR, t_span=t_span, y0=(S0, I0, R0), dense_output=True)
    sol = results["sol"]
    t = np.arange(0, 1 * YEAR)
    S, I, R = sol(t)

    if sparklines:
        spark.spark_print(I)
    else:
        for I_ in I:
            typer.echo(I_)


if __name__ == "__main__":
    typer.run(main)
```

:::
                                                                                     
[typer]: https://typer.tiangolo.com/
[exemple minimal]: https://typer.tiangolo.com/#the-absolute-minimum
[options avec aide]: https://typer.tiangolo.com/tutorial/options/help/

## 🌍 Sur le Web

Comme alternative à la ligne de commande et pour donner accès à notre service
de simulation depuis l'autre bout du globe, on peut l'exposer à travers 
une API Web, hébergée par un serveur Web. 
Ce serveur enverra les résultats
sous forme de données JSON en réponse aux requêtes [HTTP] qui lui sont
faites.

[HTTP]: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol

### FastAPI


#### 🚀 Découvrir FastAPI

Découvrez, installez puis testez la bibliothèque Python 
[FastAPI](https://fastapi.tiangolo.com/), permettant une création rapide d'API Web.
Vous pourrez vous limiter aux sections suivantes du tutoriel / guide utilisateur :

  - 📖 [Introduction](https://fastapi.tiangolo.com/tutorial/)

  - 📖 [Premiers pas](https://fastapi.tiangolo.com/tutorial/first-steps/)

  - 📖 [Paramètres de requêtes](https://fastapi.tiangolo.com/tutorial/query-params/)

### Conception de l'API Web 

#### 🚀 Création de l'API Web 


Créez une interface Web renvoyant (à sa racine) la liste des valeurs de la 
population de personnes infectées jour par jour au cours de la première année.
Faites en sorte que l'interface accepte le paramètre de requête optionel
`beta` permettant de simuler les évolutions associées à différents taux
de contagion.

#### ✨ Solution

::: collapse

``` python
...

# Third-Party
from fastapi import FastAPI
from typing import Optional
...

...

app = FastAPI()

@app.get("/")
async def root(beta: Optional[float] = BETA):
    globals()["beta"] = beta
    results = solve_ivp(
      dSIR, 
      t_span=(0, YEAR), 
      y0=(S0, I0, R0), 
      dense_output=True
    )
    sol = results["sol"]
    t = np.arange(0, YEAR)
    S, I, R = sol(t)
    return list(I)
```

:::


#### 🚀 Test de l'API Web 

Après avoir lancé le service, ouvrez un navigateur web à l'adresse <http://127.0.0.1:8000/>.

Vérifiez que vous pouvez lire la documentation de l'API à <http://127.0.0.1:8000/docs>.

Puis, requérez les données associées à de nouvelles valeurs du taux de contagion :

  - $\beta=0.8$ : <http://127.0.0.1:8000?beta=0.8> 
  
  - $\beta=0.05$ : <http://127.0.0.1:8000?beta=0.05>

### Exploitation de l'API Web

#### 🚀 Utilisation de `requests`
La bibliothèque Python [requests] permet de faire des requêtes à un
serveur Web et d'obtenir ses réponses avec du code Python.
Exploitez cette bibliothèque pour récupérer les données de simulation
fournies par le serveur depuis le confort douillet de votre interpréteur 
Python, sans ouvrir de navigateur Web !

[requests]: https://docs.python-requests.org/

#### ✨ Solution

::: collapse

Les données associées à la valeur par défaut de $\beta$ sont fournies par :

``` python
>>> import requests
>>> r = requests.get("http://127.0.0.1:8000")
>>> r.json()
[1.0, 1.0723973837364937, 1.1497875982707628, 1.232471793968265, ..., 0.3091773334306973, 0.312319093274788, 0.3155338502766228]
```

On obtient les données associés à d'autres valeurs de $\beta$ de la façon
suivante :

``` python
>>> r = requests.get(
...     "http://127.0.0.1:8000", 
...     params={"beta": 0.8}
... )
>>> r.json()
[1.0, 2.04725791572934, 4.135056370632144, 8.139634672723165, ..., 3.3730866986615555, 3.371500978216086, 3.3699478398428373]
```

:::

