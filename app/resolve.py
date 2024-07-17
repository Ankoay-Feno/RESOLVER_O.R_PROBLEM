from pyomo.environ import *

def resolve(problem_details:dict):
    required_keys = ['objective', 'variables', 'constraints']
    for key in required_keys:
        if key not in problem_details:
            raise KeyError(f"La clé '{key}' est introuvable.")

    objective = problem_details['objective']
    variables = problem_details['variables']
    constraints = problem_details['constraints']

    model = ConcreteModel()
    model.variables = Var(variables, domain=NonNegativeReals)
    
    var_dict = {var: model.variables[var] for var in variables}

    def evaluate_expression(expression):
        # Remplacer les noms des variables par leurs objets Pyomo
        for var in variables:
            expression = expression.replace(var, f"var_dict['{var}']")
        # Utiliser eval dans un environnement sécurisé
        return eval(expression, {}, {'var_dict': var_dict, 'value': value})

    # Ajouter les contraintes au modèle
    for constraint in constraints:
        expr = evaluate_expression(constraint['expression'])
        model.add_component(constraint['name'], Constraint(expr=expr))

    # Évaluer l'expression de l'objectif
    objective_expr = evaluate_expression(objective['expression'])
    
    # Définir l'objectif dans le modèle
    model.objective = Objective(expr=objective_expr, sense=maximize if objective['sense'] == 'maximize' else minimize)

    # Choisir le solveur
    solver = SolverFactory('glpk')
    if not solver.available():
        solver = SolverFactory('cbc')
        if not solver.available():
            raise RuntimeError("Installez le package GLPK ou CBC.")
    
    # Résoudre le modèle
    result = solver.solve(model)
    
    # Vérifier le statut du solveur
    if result.solver.status == SolverStatus.ok and result.solver.termination_condition == TerminationCondition.optimal:
        results = {v: model.variables[v].value for v in variables}
        results['objective_value'] = model.objective()
        return results
    else:
        raise RuntimeError("La solution optimale n'a pas été trouvée.")
