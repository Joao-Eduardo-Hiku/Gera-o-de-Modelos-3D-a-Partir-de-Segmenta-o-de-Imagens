"""Leitura de series DICOM. Dono: A."""

def carregar_serie_dicom(pasta, recorte=None):
    """Retorna (volume_hu[z,y,x], espacamento=(dz,dy,dx)).
    Converte para HU: pixel * RescaleSlope + RescaleIntercept."""
    raise NotImplementedError
