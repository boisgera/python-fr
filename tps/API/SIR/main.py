# Python Standard Library
import sys

# Third-Party
from fastapi import FastAPI
from typing import Optional
import numpy as np
from scipy.integrate import solve_ivp
import spark
import matplotlib.pyplot as plt
import typer

WEEK = 7
YEAR = 365

N = 100
beta = BETA = 1 / (WEEK)
gamma = GAMMA = 1 / (2 * WEEK)
omega = OMEGA = 1 / YEAR

S0, I0 = 99.0, 1.0
R0 = N - S0 - I0
T_SPAN = [0.0, 1.0 * YEAR]

def dSIR(t, SIR):
    S, I, R = SIR
    dS = omega * R - beta * I * S / N
    dI = beta * I * S / N - gamma * I
    dR = gamma * I - omega * R
    return (dS, dI, dR)

def main(
    sparklines: bool = typer.Option(False, help="Output sparklines"),
    beta: float = typer.Option(BETA, help="Contagion rate")):
   
    globals()["beta"] = beta
    results = solve_ivp(dSIR, t_span=T_SPAN, y0=(S0, I0, R0), dense_output=True)
    sol = results["sol"]
    t = np.arange(0, 1 * YEAR)
    S, I, R = sol(t)

    if sparklines:
        spark.spark_print(I)
    else:
        output = " ".join(f"{v:.2f}" for v in I)
        typer.echo(output)

app = FastAPI()

@app.get("/")
async def root(beta: Optional[float] = BETA):
    globals()["beta"] = beta
    results = solve_ivp(dSIR, t_span=T_SPAN, y0=(S0, I0, R0), dense_output=True)
    sol = results["sol"]
    t = np.arange(0, 1 * YEAR)
    S, I, R = sol(t)
    return list(I)

if __name__ == "__main__":
    typer.run(main)
