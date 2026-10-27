"""Brew Beans — préparation des ventes d'un groupe (depuis la racine du dépôt)."""
from pathlib import Path
import pandas as pd

GROUPE = "groupe1"  # Remplacer 1 par le numéro de votre groupe.
source = Path("data/reference/ventes_reference.csv")
livraison = Path(f"data/{GROUPE}/livraison_corrigee.csv")
sortie = Path(f"data/{GROUPE}/ventes.csv")

for fichier in (source, livraison):
    if not fichier.is_file():
        raise SystemExit(f"ERREUR : fichier absent : {fichier}")

historique = pd.read_csv(source)
nouvelles_ventes = pd.read_csv(livraison)
ventes = pd.concat([historique, nouvelles_ventes], ignore_index=True)
if ventes.empty:
    raise SystemExit("ERREUR : aucune vente")
ventes["montant_eur"] = pd.to_numeric(ventes["montant_eur"], errors="raise")
ventes.to_csv(sortie, index=False)

print(f"OK : {len(ventes)} transactions")
print(f"Chiffre d'affaires : {ventes['montant_eur'].sum():.2f} EUR")
print(f"Fichier généré : {sortie}")
