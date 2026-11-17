"""Ponte Python <-> Octave (oct2py). Escrita em conjunto (A e B)."""
from pathlib import Path
from oct2py import Oct2Py

PASTA_OCTAVE = Path(__file__).resolve().parents[2] / "octave"

def iniciar_octave():
    oc = Oct2Py()
    oc.addpath(str(PASTA_OCTAVE))
    oc.eval("pkg load image;")
    return oc
