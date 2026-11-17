"""Dice e IoU. Dono: B."""

def dice(a, b):
    a, b = a.astype(bool), b.astype(bool)
    return 2 * (a & b).sum() / (a.sum() + b.sum())

def iou(a, b):
    a, b = a.astype(bool), b.astype(bool)
    return (a & b).sum() / (a | b).sum()
