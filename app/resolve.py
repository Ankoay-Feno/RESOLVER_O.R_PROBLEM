from pyomo.environ import *

def resolve(problem_details: dict):
    # Check if required keys are present in problem_details
    required_keys = ['objective', 'variables', 'constraints']
    for key in required_keys:
        if key not in problem_details:
            raise KeyError(f"Key '{key}' is missing in problem_details.")

    # Extract objective, variables, and constraints from problem_details
    objective = problem_details['objective']
    variables = problem_details['variables']
    constraints = problem_details['constraints']

    # Create a ConcreteModel instance
    model = ConcreteModel()

    # Define variables in the model with NonNegativeReals domain
    model.variables = Var(variables, domain=NonNegativeReals)
    
    # Create a dictionary to map variable names to Pyomo variable objects
    var_dict = {var: model.variables[var] for var in variables}

    def evaluate_expression(expression):
        # Replace variable names with their Pyomo variable objects
        for var in variables:
            expression = expression.replace(var, f"var_dict['{var}']")
        # Use eval in a secure environment to evaluate the expression
        return eval(expression, {}, {'var_dict': var_dict})

    # Add constraints to the model
    for constraint in constraints:
        expr = evaluate_expression(constraint['expression'])
        model.add_component(constraint['name'], Constraint(expr=expr))

    # Evaluate the objective expression
    objective_expr = evaluate_expression(objective['expression'])
    
    # Define the objective in the model (either maximize or minimize)
    model.objective = Objective(expr=objective_expr, sense=maximize if objective['sense'] == 'maximize' else minimize)

    # Choose the solver (first try GLPK, then CBC if GLPK is not available)
    solver = SolverFactory('glpk')
    if not solver.available():
        solver = SolverFactory('cbc')
        if not solver.available():
            raise RuntimeError("Install GLPK or CBC solver.")

    # Solve the model
    result = solver.solve(model)
    
    # Check solver status and termination condition
    if result.solver.status == SolverStatus.ok and result.solver.termination_condition == TerminationCondition.optimal:
        # Extract variable values and objective value from the solved model
        results = {v: model.variables[v].value for v in variables}
        results['objective_value'] = model.objective()
        return results
    else:
        raise RuntimeError("Optimal solution not found.")
