
zones = ["A", "B", "C", "D"]
constraints = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")]
soluce = ['n', 'n', 'n', 'n']

def Resolve(tab_soluce):
    retour = True
    for i in range(len(tab_soluce)):
        if tab_soluce[i] == 'n':
            retour = False
    return retour


def Found_More_Constraint(tab_constraint)
    counts = []





