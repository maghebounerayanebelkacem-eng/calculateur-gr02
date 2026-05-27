def calculer_tva(prix_ht :float) -> float:
    return prix_ht *1.20


prix_ttc = calculer_tva(100)
print(f"PrixTTC: {prix_ttc}")