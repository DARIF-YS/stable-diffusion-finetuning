import nbformat

# Charger le notebook
nb = nbformat.read("training.ipynb", as_version=5)

# Supprimer ou corriger les widgets
for cell in nb.cells:
    if "widgets" in cell.metadata:
        # Option 1 : Supprimer
        del cell.metadata["widgets"]
        # Option 2 : ou ajouter state vide
        # cell.metadata["widgets"] = {"state": {}}

# Sauvegarder le notebook corrigé
nbformat.write(nb, "training.ipynb")
