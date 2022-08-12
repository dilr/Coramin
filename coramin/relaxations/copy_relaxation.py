from .mccormick import PWMcCormickRelaxationData, PWMcCormickRelaxation
from .univariate import PWXSquaredRelaxationData, PWUnivariateRelaxationData, PWArctanRelaxationData, \
    PWCosRelaxationData, PWSinRelaxationData
from .univariate import PWXSquaredRelaxation, PWUnivariateRelaxation, PWArctanRelaxation, \
    PWCosRelaxation, PWSinRelaxation
from .alphabb import AlphaBBRelaxation, AlphaBBRelaxationData
from .multivariate import MultivariateRelaxationData, MultivariateRelaxation
from pyomo.core.expr.visitor import replace_expressions
from coramin.utils.coramin_enums import FunctionShape


def copy_relaxation_with_local_data(rel, old_var_to_new_var_map):
    """
    This function copies a relaxation object with new variables.
    Note that only what can be set through the set_input and build
    methods are copied. For example, piecewise partitioning points
    are not copied.

    Parameters
    ----------
    rel: coramin.relaxations.relaxations_base.BaseRelaxationData
        The relaxation to be copied
    old_var_to_new_var_map: dict
        Map from the original variable id to the new variable

    Returns
    -------
    rel: coramin.relaxations.relaxations_base.BaseRelaxationData
        The copy of rel with new variables
    """

    return rel.copy_relaxation_with_local_data(old_var_to_new_var_map)
    #if isinstance(rel, PWXSquaredRelaxationData):
    #    pass
    #elif isinstance(rel, PWArctanRelaxationData):
    #    pass
    #elif isinstance(rel, PWSinRelaxationData):
    #    pass
    #elif isinstance(rel, PWCosRelaxationData):
    #    pass
    #elif isinstance(rel, PWUnivariateRelaxationData):
    #    pass
    #elif isinstance(rel, PWMcCormickRelaxationData):
    #    pass
    #elif isinstance(rel, AlphaBBRelaxationData):
    #    pass
    #elif isinstance(rel, MultivariateRelaxationData):
    #    pass
    #elif isinstance(rel, SOCEdgeCutsData):
    #    pass
    #else:
    #    raise ValueError('Unrecognized relaxation: {0}'.format(str(type(rel))))

