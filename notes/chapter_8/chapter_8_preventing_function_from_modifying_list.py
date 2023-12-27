def print_models(unprinted_designs, completed_models):
    """Simulate printing each design until none are left
    Move each design to completed_models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design.title()}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were completed"""
    print(f"\nThe following models have been completed:")
    for completed_model in completed_models:
        print(completed_model.title())


unprinted_designs = ['phone case', 'robot pendant', 'millennium falcon']
completed_models = []

# use a slice to make a copy of a list instead
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
