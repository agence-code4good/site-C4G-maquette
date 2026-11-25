# Maquette du nouveau site Code4Good

Exemple de pages (accueil, page secteur, page cas d'usage) à faire valider par l'équipe avant de rédiger tout le site.
Ce n'est **pas** le site en ligne : celui-ci est dans le dépôt `agence-code4good/site-C4G` (www.code4good.fr).

- Point de départ : copie du site statique actuel (novembre 2026).
- Pages non indexées par Google (balise `noindex` sur chaque page + `robots.txt`).
- Adresse : https://agence-code4good.github.io/site-C4G-maquette/

## Pages de l'exemple « Seconde main & Réemploi »
- `index.html` : accueil (page actuelle + nouveau menu « Secteurs d'activité »)
- `seconde-main-reemploi.html` : page secteur
- `synchroniser-stocks-marketplaces.html` : page cas d'usage
- Les emplacements surlignés en jaune « À compléter » attendent les vrais faits clients (pas de faux chiffres).

Ces 3 pages sont générées par `python3 -I tools/build.py` (en-tête, menu et pied de page communs) ; styles dans `assets/maquette.css`, menu dans `assets/maquette.js`. Les autres fichiers HTML (contact, équipe…) sont encore la copie du site actuel.
