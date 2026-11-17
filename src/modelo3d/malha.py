"""Marching Cubes, suavizacao e exportacao. Escrita em conjunto no dia 1; dono depois: A."""

def construir_malha(volume_bool, espacamento, nivel=0.5, passo=1, n_iter=300):
    """Retorna (vertices, faces) ja suavizados."""
    raise NotImplementedError

def exportar_malha(vertices, faces, caminho_stl, caminho_obj=None):
    raise NotImplementedError
