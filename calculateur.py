def calculer_tva(prix_ht :float) -> float:
    return prix_ht *1.20
def convertir_euros_dollars(montant_euro:float) -> float:
    return montant_euro *1.08

prix_ttc = calculer_tva(100)
print(f"PrixTTC: {prix_ttc}")
