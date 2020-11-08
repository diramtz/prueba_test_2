def sign(x):
    """
    Helper function for computing sign of real number x.
    """
    if x >=0:
        return 1
    else:
        return -1


#def ortogonalidad(A,i,j):
#    tol = 1e-8
#    numerador = np.abs(np.dot(A[:,i],matriz_A[:,j])) 
#    denominador = np.linalg.norm(A[:,i]) * np.linalg.norm(matriz_A[:,j])
#    ortogonal = numerador/denominador < tol
#    return ortogonal
