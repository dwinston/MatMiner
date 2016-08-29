__author__ = 'Saurabh Bajaj <sbajaj@lbl.gov>'


def vickers_hardness1(G, K):
    """
    Calculate Vickers hardness for a material.

    References:
        DOI: (not available yet) (Title: "A Statistical Learning Framework for Materials Science: Application to
        Elastic Moduli of k-nary Inorganic Compounds")

    Args:
        G: (float) elastic bulk moduli
        K: (float) elastic shear moduli

    Returns: (float) Vickers hardness

    """
    return 2*(G**3.0/K**2.0)**0.585 - 3


def vickers_hardness2(F, a):
    """
    Calculate Vickers hardness for a material.

    References:
        DOI: 10.1007/s10853-013-7569-1 (Title: "Room temperature mechanical properties of natural-mineral-based
        thermoelectrics")

    Args:
        F: (float) indentation load (N)
        a: (float) half of diagonal length of the indentation impression (m)

    Returns: (float) Vickers hardness

    """
    return (1.8544 * F)/((2*a)**2.0)


def thermal_stress(E_T, alpha_T, delta_T, nu_T):
    """
    Calculate thermal stress.

    References:
        DOI: 10.1007/s10853-013-7569-1 (Title: "Room temperature mechanical properties of natural-mineral-based
        thermoelectrics")

    Args:
        E_T: (float) temperature-dependent Young's modulus
        alpha_T: (float) temperature-dependent thermal expansion coefficient (K^(-1))
        delta_T: (float) temperature difference (K)
        nu_T: (float) temperature-dependent Poisson's ratio

    Returns: (float) thermal stress induced by thermal gradients or thermal transients

    """
    return (E_T * alpha_T * delta_T)/(1 - nu_T)

if __name__ == "__main__":
    print vickers_hardness1(3, 2)