"""Génère les pages de la maquette (accueil, page secteur, page cas d'usage).

Usage : python3 -I tools/build.py   (depuis la racine du dépôt)
L'en-tête, le menu et le pied de page sont communs : on les modifie ici une seule fois.
Source des secteurs et cas d'usage : V2 d'Anne-Cécile (« Irritants par secteurs - V2.xlsx », 25/11/2026).
"""
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = "assets/images/"

# Pages réellement rédigées dans la maquette ; les autres liens affichent « page à venir ».
PAGE_SECTEUR = "seconde-main-reemploi.html"
PAGE_CAS = "synchroniser-stocks-marketplaces.html"

# Menu « Secteurs d'activité » : secteurs puis besoins, à la suite, au même niveau (décision du 25/11).
# (nom, description courte pour l'accueil, [titres des cas d'usage], page secteur)
ENTREES = [
    ("Seconde main & Réemploi", "Stocks, estimation et prix de revente d'articles uniques",
     ["Synchroniser vos stocks sur toutes vos marketplaces", "Fiabiliser et accélérer l'estimation de vos articles",
      "Fixer le juste prix de revente"], PAGE_SECTEUR),
    ("Négoce & Vin", "Vente directe, commandes et tarifs pros",
     ["Développer la vente directe sans alourdir votre logistique", "Centraliser vos commandes et vos stocks",
      "Gérer des tarifs et catalogues distincts pour pros et particuliers", "Équiper vos commerciaux terrain"], None),
    ("Santé", "Des ressources qui aident vos publics à décider",
     ["Transformer vos ressources en outil d'aide à la décision", "Répondre automatiquement aux questions récurrentes"], None),
    ("Gestion de patrimoine", "Pièces justificatives, échéances et reporting",
     ["Simplifier la collecte des pièces justificatives", "Anticiper les échéances clés de vos clients",
      "Consolider toutes vos sources de données dans un reporting fiable",
      "Préparer vos rendez-vous et comptes rendus plus rapidement"], None),
    ("Services aux entreprises & à la personne", "Plannings, suivi des prestations et facturation",
     ["Automatiser la planification de vos intervenants", "Suivre les prestations réalisées en temps réel",
      "Facturer à partir des interventions réellement réalisées"], None),
    ("Retail & Logistique", "Stocks, reprise en magasin, expéditions et inventaires",
     ["Synchroniser les stocks de vos magasins et de votre site", "Fluidifier la reprise de produits en magasin",
      "Suivre vos préparations et expéditions en temps réel", "Piloter le réassort à partir de vos données de vente",
      "Simplifier vos inventaires"], None),
    ("Comptabilité & Contrôle de gestion", "Saisie, reportings et facturation électronique",
     ["Automatiser la saisie des commandes et factures partenaires", "Automatiser vos reportings et tableaux de bord",
      "Préparer le passage à la facturation électronique"], None),
    ("Organismes publics & Gestion de dossiers", "Candidatures, instruction et bilans",
     ["Centraliser la réception des candidatures", "Tracer chaque étape de l'instruction",
      "Automatiser la vérification de l'éligibilité", "Automatiser les relances des dossiers incomplets",
      "Informer les usagers de l'avancement de leur dossier", "Générer automatiquement vos bilans pour les financeurs"], None),
    ("Connecter ses outils", "Des outils qui se parlent, sans double saisie",
     ["Connecter vos outils de vente, de gestion et de comptabilité", "Partager des données à jour avec vos partenaires",
      "Surveiller les échanges de données entre vos outils"], None),
    ("De la ressource à la décision", "Transformer vos contenus en outils d'aide à la décision",
     ["Transformer vos ressources en outil d'aide à la décision", "Proposer une réponse personnalisée à chaque utilisateur",
      "Passer du contenu générique à l'évaluation sur mesure", "Valoriser vos données de référence",
      "Fournir des arguments chiffrés pour convaincre"], None),
    ("Espaces clients & accès sécurisés", "Documents et informations partagés en sécurité",
     ["Partager vos documents confidentiels en toute sécurité", "Offrir à chaque client un espace dédié"], None),
    ("Outils sur mesure & IA", "Remplacer vos Excel critiques, retrouver l'information",
     ["Remplacer vos fichiers Excel critiques par une application",
      "Retrouver instantanément l'information dans vos documents"], None),
]
CAS_PAGES = {"Synchroniser vos stocks sur toutes vos marketplaces": PAGE_CAS}

LOGOS = [("ZKXaG2qKl1zM7pU6GG9JiWYRn3o-a2ef5525.png", "LiLi"), ("v5L5MorYoWn4pubcFEKABcY4JkM-5a79a53f.svg", "Deuzio"),
         ("LWA2Cx0kVVmJQ7oSs67TfETCH3Y-5a79a53f.svg", "Cultura"), ("M1oRkj8JQTGtmff1zTWPbCEtmn8-5a79a53f.svg", "Persephone"),
         ("ltalIZYC4vKRznlCVgFI4pFXyUM-ef92bd29.png", "D. Balaresque"), ("01J1lyfAaBJtv4nTGsQaRLKk80-8890641d.png", "OFQJ"),
         ("unBwaFVmJr0pu088MTjqXsdfkU-5a79a53f.svg", "Butrfly")]

TODO = lambda t: f'<em class="todo">À compléter : {escape(t)}</em>'


def slug(i):
    return f"e{i}"


def header():
    entries = "\n".join(
        f'<li><a href="{p or "#"}" data-entry="{slug(i)}"{"" if p else " class=" + chr(34) + "soon" + chr(34)}>{escape(n)}</a></li>'
        for i, (n, _, _, p) in enumerate(ENTREES))
    panels = []
    for i, (n, _, cas, p) in enumerate(ENTREES):
        items = "".join(
            f'<li><a href="{CAS_PAGES[c]}">{escape(c)}</a></li>' if c in CAS_PAGES
            else f'<li><a href="#" class="soon">{escape(c)}</a></li>' for c in cas)
        voir = (f'<a class="link-arrow" href="{p}">Voir la page {escape(n)} →</a>' if p
                else '<a class="link-arrow soon" href="#">Voir la page →</a>')
        panels.append(f'<div data-panel="{slug(i)}"{"" if i == 0 else " hidden"}><h3>{escape(n)}</h3><ul>{items}</ul>{voir}</div>')
    return f"""
<div class="maquette-bar"><strong>Maquette de travail</strong> · non publiée · seules les pages « Seconde main &amp; Réemploi » sont rédigées</div>
<header class="site-header">
  <div class="wrap header-in">
    <a class="logo" href="index.html" aria-label="Code4Good, accueil"><img src="{IMG}uL8eRIjgOnqQc4gBAYPUlRA2rA.svg" alt="Code4Good" width="129" height="52"></a>
    <button class="burger" data-burger aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Navigation principale">
      <div class="nav-zone">
        <button type="button" data-mega-btn aria-expanded="false" aria-controls="mega">Secteurs d'activité<span class="chev">▾</span></button>
        <div class="mega" id="mega" hidden>
          <div class="wrap mega-in">
            <ul class="mega-list">{entries}</ul>
            <div class="mega-panel">{"".join(panels)}</div>
          </div>
        </div>
      </div>
      <a href="#" class="soon">Services</a>
      <a href="#" class="soon">Réalisations</a>
      <a href="#" class="soon">Ressources</a>
      <a class="btn" href="contact.html">Rencontrer un expert</a>
    </nav>
  </div>
</header>
<div id="toast" class="toast" role="status" hidden>Cette page n'est pas encore rédigée dans la maquette.</div>
"""


FOOTER = f"""
<footer class="site-footer">
  <div class="wrap footer-in">
    <div>
      <img src="{IMG}uL8eRIjgOnqQc4gBAYPUlRA2rA.svg" alt="Code4Good" width="129" height="52">
      <p>Agence d'outils métier sur mesure à Bordeaux. On comprend votre métier, puis on construit l'outil.</p>
      <p>Bureau 3D, 200 cours Balguerie-Stuttenberg<br>33000 Bordeaux</p>
    </div>
    <div>
      <h4>Le site</h4>
      <ul>
        <li><a href="{PAGE_SECTEUR}">Secteurs d'activité</a></li>
        <li><a href="#" class="soon">Services</a></li>
        <li><a href="#" class="soon">Réalisations</a></li>
        <li><a href="#" class="soon">Ressources</a></li>
      </ul>
    </div>
    <div>
      <h4>Nous contacter</h4>
      <ul>
        <li><a href="contact.html">Rencontrer un expert</a></li>
        <li>contact@code4good.fr</li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>© 2026 Code4Good</span>
    <a href="politique.html">Politique de confidentialité</a>
  </div>
</footer>
<script src="assets/maquette.js"></script>
"""


def page(fichier, titre, description, corps):
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(titre)}</title>
<meta name="description" content="{escape(description)}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{IMG}i0iI4dwEwzHPl2a9XzsiJ7Wu9g.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/maquette.css">
</head>
<body>
{header()}
<main>
{corps}
</main>
{FOOTER}
</body>
</html>
"""
    with open(os.path.join(ROOT, fichier), "w", encoding="utf-8") as f:
        f.write(html)
    print("ok", fichier)


def cta_final(titre="Parlons de votre projet"):
    return f"""
<section class="section"><div class="wrap">
  <div class="cta-final">
    <h2>{titre}</h2>
    <p class="lead" style="margin-inline:auto">30 minutes avec un expert pour faire le point sur votre besoin. C'est offert, et sans engagement.</p>
    <div class="btns" style="justify-content:center"><a class="btn" href="contact.html">Rencontrer un expert</a></div>
  </div>
</div></section>"""


def faq(items):
    return "<div class=\"faq\">" + "".join(
        f"<details><summary>{escape(q)}</summary><div><p>{a}</p></div></details>" for q, a in items) + "</div>"


# ---------------------------------------------------------------- Accueil
def accueil():
    logos = "".join(f'<img src="{IMG}{f}" alt="{escape(a)}" loading="lazy">' for f, a in LOGOS)
    tuiles = "".join(
        f'<a class="card tile" href="{p}"><h3>{escape(n)}</h3><p>{escape(d)}</p></a>' if p else
        f'<a class="card tile soon" href="#" title="Page pas encore rédigée dans la maquette"><h3>{escape(n)}</h3><p>{escape(d)}</p></a>'
        for n, d, _, p in ENTREES)
    equipe = [("URpUUtbpxxPMsmURqDiZD1YC9dg-4df7a85c.png", "Anne-Cécile Mechin", "Développeuse et cheffe de projet"),
              ("b64INtLlqg57Vno3S8nrbBWnXk-4df7a85c.png", "Florent Legeron", "Développeur web fullstack"),
              ("yf5LZplfyxSWV44cVdx8exTXc10-4df7a85c.png", "Julien Durandet", "Expert marketing digital"),
              ("pmi13gzZYCRmnZEOYX0PwPCoxQ-4df7a85c.png", "Claudine Pradal", "Product owner, experte analyse des gestes métiers"),
              ("GGb7MwXu1fCDaq7Ohm8amCCPj4-a58e9fa9.png", "Hugo Marty", "Designer")]
    team = "".join(f'<div><img src="{IMG}{f}" alt="{escape(n)}" loading="lazy"><strong>{escape(n)}</strong><span>{escape(r)}</span></div>'
                   for f, n, r in equipe)
    corps = f"""
<section class="hero center"><div class="wrap">
  <span class="kicker">Pour les entreprises responsables et à la recherche d'impact.</span>
  <h1>Et si vos <span class="green">solutions digitales</span> comprenaient vraiment vos <span class="green">enjeux métier</span>&nbsp;?</h1>
  <p class="lead">On sait que la technique peut sembler obscure. Nous vous accompagnons dans le développement de vos outils métiers, en parlant votre langue, pas seulement celle des développeurs.</p>
  <div class="btns"><a class="btn" href="contact.html">Rencontrer un expert</a><a class="btn light" href="#realisations">Voir nos réalisations</a></div>
</div></section>
<div class="pattern" role="presentation"></div>

<section class="section center"><div class="wrap">
  <span class="kicker">Ils nous font confiance</span>
  <h2>Nous avons réalisé des projets pour eux</h2>
  <div class="logos">{logos}</div>
</div></section>

<section class="section soft center" id="secteurs"><div class="wrap">
  <span class="kicker">Secteurs d'activité</span>
  <h2>On connaît votre métier</h2>
  <p class="lead">Choisissez votre secteur ou votre besoin : on vous montre les problèmes qu'on a résolus pour des entreprises comme la vôtre.</p>
  <div class="grid g4" style="text-align:left">{tuiles}</div>
</div></section>

<section class="section center" id="realisations"><div class="wrap">
  <span class="kicker">Nos réalisations</span>
  <h2>Des outils qui ont changé leur quotidien</h2>
  <div class="grid g3" style="text-align:left">
    <a class="card case" href="{PAGE_CAS}"><img class="case-logo" src="{IMG}ZKXaG2qKl1zM7pU6GG9JiWYRn3o-a2ef5525.png" alt="LiLi"><span class="sector">Seconde main &amp; Réemploi</span><h3>Synchroniser les stocks sur toutes les marketplaces</h3><span class="stat-line">{TODO("chiffre clé LiLi")}</span><span class="link-arrow">Voir le cas d'usage →</span></a>
    <a class="card case soon" href="#"><img class="case-logo" src="{IMG}01J1lyfAaBJtv4nTGsQaRLKk80-8890641d.png" alt="OFQJ"><span class="sector">Organismes publics</span><h3>Centraliser la réception des candidatures</h3><span class="stat-line">{TODO("chiffre clé OFQJ")}</span><span class="link-arrow">Voir le cas d'usage →</span></a>
    <a class="card case soon" href="#"><span class="case-logo" style="display:block;font-family:'Archivo Black',sans-serif;font-size:1.3rem;color:var(--ink)">La Maison Gabin</span><span class="sector">Négoce &amp; Vin</span><h3>Développer la vente directe sans alourdir la logistique</h3><span class="stat-line">{TODO("chiffre clé Maison Gabin")}</span><span class="link-arrow">Voir le cas d'usage →</span></a>
  </div>
</div></section>

<section class="section soft"><div class="wrap split">
  <div>
    <span class="kicker">Notre approche</span>
    <h2>D'abord votre métier, ensuite l'outil</h2>
    <p>Chez Code4Good, nous concevons des outils numériques sur mesure qui s'intègrent aux métiers de nos clients pour répondre à leurs défis concrets. Notre objectif : améliorer efficacité, clarté et autonomie grâce à des solutions utiles et durables.</p>
    <p>Nous commençons toujours par comprendre vos besoins, vos enjeux et votre fonctionnement. Notre approche repose sur trois piliers :</p>
    <ul class="ticks">
      <li>une <strong>écoute active</strong> pour capter vos besoins métiers ;</li>
      <li>un <strong>design centré utilisateur</strong> pour des outils intuitifs ;</li>
      <li>un <strong>développement sur mesure</strong>, mêlant code et no-code, pour plus de flexibilité.</li>
    </ul>
    <a class="btn" href="contact.html">Rencontrer un expert</a>
  </div>
  <img class="photo" src="{IMG}b4ReNNDkwihWKORYXXnjHwDCRg-40ed77f3.jpg" alt="L'équipe Code4Good en atelier" loading="lazy">
</div></section>

<section class="section center"><div class="wrap">
  <span class="kicker">Témoignages</span>
  <h2>Ceux qui en parlent le mieux, c'est encore nos clients</h2>
  <div class="quote-card">
    <img src="{IMG}CBjcR7gocBgw1KcBRlJpOeLsiDI-7f2fdac3.jpg" alt="Manuela, CEO de Butrfly" loading="lazy">
    <div>
      <div class="stars" aria-label="5 étoiles sur 5">★★★★★</div>
      <blockquote>« L'agence Code4Good a les capacités humaines et les compétences techniques pour la réussite des projets. Un accompagnement super professionnel pour des résultats ultra positifs. Je recommande et j'encourage. Foncez ! »
        <footer><strong>Manuela</strong>, CEO de Butrfly</footer></blockquote>
    </div>
  </div>
</div></section>

<section class="section soft center"><div class="wrap">
  <span class="kicker">Nos processus</span>
  <h2>Des effets mesurables pour nos clients</h2>
  <div class="stats">
    <div><img src="{IMG}cUTvKsaQjbRyifUk2bpBFFz4jrM-ba2733b0.png" alt="20+"><strong>Projets livrés</strong><span>Outils métier, internes et externes, ou applications web.</span></div>
    <div><img src="{IMG}npHi3CejlQe1hsIuhmZg1TEMzsM-ab4a97a9.png" alt="100 %"><strong>Clients satisfaits</strong><span>Parce que nous tenons nos engagements, nos clients reviennent et recommandent.</span></div>
    <div><img src="{IMG}npHi3CejlQe1hsIuhmZg1TEMzsM-ab4a97a9.png" alt="100 %"><strong>Responsive</strong><span>Tous nos projets sont testés et compatibles sur tous les formats.</span></div>
    <div><img src="{IMG}ZZVWck9BSEsj3w8c8zaJB9TRsf0-025857f0.png" alt="x2"><strong>Gain de temps</strong><span>Une hausse de performance constatée sur les processus métiers.</span></div>
  </div>
</div></section>

<section class="section center"><div class="wrap">
  <span class="kicker">La team</span>
  <h2>Rencontrez la team derrière Code4Good</h2>
  <p class="lead">Nous sommes une équipe de développeurs, designers et chefs de projet au service de votre vision et d'un monde plus équitable et responsable.</p>
  <div class="team" style="text-align:left">{team}</div>
</div></section>

<section class="section soft center"><div class="wrap">
  <span class="kicker">FAQ</span>
  <h2>On nous demande souvent</h2>
  {faq([
    ("Combien coûte un projet avec Code4Good ?", "Chaque projet est unique, et notre rôle, c'est de vous proposer la solution la plus adaptée à vos enjeux et à vos moyens. Que ce soit en no-code, avec un Excel bien pensé, ou via des technologies robustes et éprouvées, on trouve toujours un point de départ viable, testable et pérenne. On vous aide à prioriser, pour avancer avec l'essentiel et poser des bases solides pour la suite."),
    ("Est-ce que vous travaillez avec des petites structures ?", "Oui ! Nous accompagnons aussi bien des startups, des associations ou des PME que des structures plus grandes. Tant qu'il y a un besoin métier et une envie de co-construire, nous sommes là. Nous adaptons notre approche selon vos moyens et vos ressources."),
    ("Est-ce que vous êtes une agence web ?", "Oui, mais pas comme les autres. Code4Good est une agence spécialisée dans la conception de solutions numériques sur mesure. Notre différence ? Nous plongeons dans votre métier pour concevoir des outils qui s'alignent sur vos pratiques, vos utilisateurs et vos objectifs. Pas de solutions génériques : chaque projet est pensé sur mesure, avec une vraie logique de partenariat."),
    ("Faites-vous du no-code ou du développement classique ?", "Les deux ! Nous utilisons le no-code quand cela permet d'aller plus vite et de réduire les coûts, et le développement sur mesure quand les besoins sont plus spécifiques. Nous mixons souvent les deux, pour offrir le meilleur compromis entre performance, agilité et budget."),
    ("Comment se passe un projet avec Code4Good ?", "Dès le démarrage, on avance ensemble et en toute transparence. Une fois le projet lancé, nous organisons un rendez-vous chaque semaine pour suivre l'avancement, faire des démonstrations, ajuster les priorités ou répondre à vos questions. Et on parle votre langue : vous savez toujours où on en est, ce qu'on fait, pourquoi on le fait, et ce que ça change pour vous et vos utilisateurs."),
    ("Est-ce que vous travaillez à distance ?", "Oui, mais pas uniquement. Nous avons une agence à Bordeaux et sommes toujours ravis de rencontrer nos clients en personne. En parallèle, nous avons l'habitude de travailler à distance de façon fluide et structurée : points réguliers en visio, outils collaboratifs, réactivité."),
  ])}
</div></section>
{cta_final("Discutons de votre projet")}
"""
    page("index.html", "Code4Good · Agence d'outils métier sur mesure à Bordeaux",
         "Code4Good conçoit des outils métier sur mesure pour les PME : on comprend votre métier, puis on construit l'outil.", corps)


# ---------------------------------------------------------------- Page secteur
def secteur():
    corps = f"""
<section class="hero"><div class="wrap">
  <nav class="breadcrumb" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a><span>›</span>Secteurs d'activité<span>›</span>Seconde main &amp; Réemploi</nav>
  <span class="kicker">Seconde main &amp; Réemploi</span>
  <h1>Des outils sur mesure pour la <span class="green">seconde main</span> et le <span class="green">réemploi</span></h1>
  <p class="lead">Articles uniques, estimations au cas par cas, ventes sur plusieurs canaux : votre métier ne rentre pas dans les logiciels standards. On construit l'outil qui suit votre façon de travailler.</p>
  <div class="btns"><a class="btn" href="contact.html">Rencontrer un expert</a><a class="btn light" href="#realisations">Voir nos réalisations</a></div>
  <div class="logos" style="justify-content:flex-start;margin-top:44px">
    <img src="{IMG}ZKXaG2qKl1zM7pU6GG9JiWYRn3o-a2ef5525.png" alt="LiLi"><img src="{IMG}v5L5MorYoWn4pubcFEKABcY4JkM-5a79a53f.svg" alt="Deuzio">
  </div>
</div></section>

<section class="section soft"><div class="wrap">
  <div class="narrow">
    <span class="kicker">Votre métier, tel qu'on l'a compris</span>
    <h2>La seconde main, un commerce pas comme les autres</h2>
    <p>Revendre des livres, des jeux, des vêtements ou des objets d'occasion, ce n'est pas du commerce classique. Chaque article est unique, son état change tout, et son prix dépend du marché du moment. Pour vendre, il faut aussi être présent partout : en boutique, sur votre site et sur les marketplaces.</p>
  </div>
  <div class="grid g3">
    <div class="card"><h3>Chaque article est unique</h3><p>Pas de référence créée une fois pour toutes : chaque pièce a son état, ses photos et sa fiche. La saisie prend vite des heures.</p></div>
    <div class="card"><h3>L'estimation repose sur l'expérience</h3><p>Combien racheter ce lot ? À quel prix le revendre ? La réponse dépend souvent d'une ou deux personnes, et elle prend du temps.</p></div>
    <div class="card"><h3>Un article, plusieurs vitrines</h3><p>Vous vendez en boutique, sur votre site et sur plusieurs marketplaces. Mais un article unique ne peut être vendu qu'une fois.</p></div>
  </div>
  <p class="narrow" style="margin-top:36px">Les logiciels de caisse et de boutique en ligne sont pensés pour des produits fabriqués en série. Résultat : les équipes de la seconde main jonglent entre fichiers Excel, ressaisies et vérifications à la main. C'est ce temps-là qu'on vous rend.</p>
</div></section>

<section class="section"><div class="wrap">
  <span class="kicker">Ce qu'on fait pour vous</span>
  <h2>Trois problèmes qu'on résout pour vous</h2>
  <div class="grid g3">
    <a class="card" href="{PAGE_CAS}"><h3>Synchroniser vos stocks sur toutes vos marketplaces</h3><p class="problem">Un article vendu sur une marketplace reste en vente sur les autres.</p><span class="link-arrow">Découvrir →</span></a>
    <a class="card soon" href="#"><h3>Fiabiliser et accélérer l'estimation de vos articles</h3><p class="problem">L'estimation des articles dépend de l'expérience de chacun et prend un temps considérable.</p><span class="link-arrow">Découvrir →</span></a>
    <a class="card soon" href="#"><h3>Fixer le juste prix de revente</h3><p class="problem">Je fixe mes prix de revente sans référence fiable.</p><span class="link-arrow">Découvrir →</span></a>
  </div>
</div></section>

<section class="section soft" id="realisations"><div class="wrap">
  <span class="kicker">Nos réalisations</span>
  <h2>Ils l'ont fait avec nous</h2>
  <div class="grid g2">
    <a class="card case" href="{PAGE_CAS}"><img class="case-logo" src="{IMG}ZKXaG2qKl1zM7pU6GG9JiWYRn3o-a2ef5525.png" alt="LiLi"><h3>LiLi</h3><p>{TODO("qui est LiLi en une phrase (activité, taille)")}</p><p>{TODO("ce qu'on a construit pour LiLi, en une phrase")}</p><span class="stat-line">{TODO("chiffre clé")}</span><span class="link-arrow">Voir le cas d'usage →</span></a>
    <a class="card case soon" href="#"><img class="case-logo" src="{IMG}v5L5MorYoWn4pubcFEKABcY4JkM-5a79a53f.svg" alt="Deuzio"><h3>Deuzio</h3><p>{TODO("qui est Deuzio en une phrase (activité, taille)")}</p><p>{TODO("ce qu'on a construit pour Deuzio, en une phrase")}</p><span class="stat-line">{TODO("chiffre clé")}</span><span class="link-arrow">Voir la réalisation →</span></a>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <span class="kicker">Comment on travaille</span>
  <h2>On commence toujours par votre métier</h2>
  <div class="grid g4 steps">
    <div class="step"><h3>On observe</h3><p>On regarde comment vous travaillez au quotidien, avec vos équipes : la réception des articles, la saisie, la vente.</p></div>
    <div class="step"><h3>On priorise</h3><p>On repère ce qui vous fait perdre le plus de temps, et on commence par là.</p></div>
    <div class="step"><h3>On construit</h3><p>Par petites étapes, avec un point chaque semaine pour vous montrer l'avancement et ajuster.</p></div>
    <div class="step"><h3>On reste là</h3><p>On forme vos équipes, et on fait évoluer l'outil avec votre activité.</p></div>
  </div>
</div></section>

<section class="section soft center"><div class="wrap">
  <span class="kicker">FAQ</span>
  <h2>Vos questions sur la seconde main</h2>
  {faq([
    ("Pouvez-vous repartir de nos fichiers Excel actuels ?", "Oui. On part de vos fichiers existants pour ne rien perdre, puis l'outil prend le relais. Vos équipes retrouvent leurs repères dès le premier jour."),
    ("Faut-il changer de logiciel de caisse ou de boutique en ligne ?", "Pas forcément. On peut construire un outil qui se connecte à ceux que vous utilisez déjà, pour qu'ils travaillent enfin ensemble."),
    ("Travaillez-vous avec les ressourceries et les associations ?", "Oui. Nous accompagnons aussi bien des associations que des PME, et nous adaptons chaque projet à vos moyens et à vos ressources."),
  ])}
</div></section>
{cta_final("Parlons de votre activité")}
"""
    page(PAGE_SECTEUR, "Outils sur mesure pour la seconde main et le réemploi · Code4Good",
         "Stocks synchronisés sur vos marketplaces, estimation et prix de revente : Code4Good construit les outils métier de la seconde main et du réemploi.", corps)


# ---------------------------------------------------------------- Page cas d'usage
def cas():
    corps = f"""
<section class="hero"><div class="wrap">
  <nav class="breadcrumb" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a><span>›</span><a href="{PAGE_SECTEUR}">Seconde main &amp; Réemploi</a><span>›</span>Synchroniser vos stocks</nav>
  <span class="kicker">Seconde main &amp; Réemploi</span>
  <h1>Synchroniser vos stocks sur toutes vos <span class="green">marketplaces</span></h1>
  <p class="lead problem" style="font-size:1.3rem">Un article vendu sur une marketplace reste en vente sur les autres.</p>
  <p class="lead">On relie vos canaux de vente : un article vendu quelque part disparaît partout.</p>
  <div class="btns"><a class="btn" href="contact.html">Rencontrer un expert</a><a class="btn light" href="#preuve">Voir la réalisation LiLi</a></div>
</div></section>

<section class="section soft"><div class="wrap">
  <div class="narrow">
    <span class="kicker">Le problème</span>
    <h2>Un article unique, vendu deux fois</h2>
    <p>Quand vous vendez des pièces uniques sur plusieurs plateformes, chaque vente doit être reportée à la main sur toutes les autres. Tant que ce n'est pas fait, l'article reste en vente ailleurs.</p>
  </div>
  <div class="grid g3">
    <div class="card"><h3>Des ventes à annuler</h3><p>Le même article est acheté deux fois. Il faut annuler, rembourser et s'excuser auprès du client.</p></div>
    <div class="card"><h3>Des notes qui baissent</h3><p>Les annulations pèsent sur votre réputation et sur votre visibilité dans les marketplaces.</p></div>
    <div class="card"><h3>Des heures perdues</h3><p>Mettre à jour chaque plateforme à la main, tous les jours, c'est du temps en moins pour trier, estimer et vendre.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap split">
  <div>
    <span class="kicker">Notre réponse</span>
    <h2>Un seul stock, à jour partout</h2>
    <p>On construit un outil qui rassemble votre stock et le partage avec toutes vos vitrines.</p>
    <ul class="ticks">
      <li><strong>Un seul stock pour tous vos canaux.</strong> Vos articles sont enregistrés une fois. Boutique, site et marketplaces s'appuient sur la même liste.</li>
      <li><strong>Vendu ici, retiré partout.</strong> Dès qu'un article est vendu, il est retiré automatiquement des autres plateformes.</li>
      <li><strong>Une vue claire de vos ventes.</strong> Vous voyez en un coup d'œil ce qui est en vente, où, et ce qui s'est vendu.</li>
    </ul>
  </div>
  <img class="photo" src="{IMG}y2fa3Uu8d9owfbe9zi9Vi4xs-1a384588.jpg" alt="Un développeur de l'équipe Code4Good au travail" loading="lazy">
</div></section>

<section class="section soft" id="preuve"><div class="wrap">
  <span class="kicker">La preuve</span>
  <h2>Ce qu'on a fait pour LiLi</h2>
  <div class="proof" style="margin-top:32px">
    <div>
      <img class="case-logo" src="{IMG}ZKXaG2qKl1zM7pU6GG9JiWYRn3o-a2ef5525.png" alt="LiLi">
      <blockquote>{TODO("citation d'un responsable de LiLi")}
        <footer>{TODO("prénom, fonction")}</footer></blockquote>
    </div>
    <dl>
      <dt>Avant</dt><dd>{TODO("comment LiLi gérait ses stocks et ses ventes avant (outils, temps passé, problèmes)")}</dd>
      <dt>Ce qu'on a construit</dt><dd>{TODO("l'outil livré, en 2 ou 3 phrases, sans techno")}</dd>
      <dt>Résultat</dt><dd>{TODO("1 ou 2 chiffres : temps gagné, ventes annulées en moins, nombre d'articles…")}</dd>
    </dl>
  </div>
  <p style="margin-top:24px">Nous avons aussi accompagné <strong>Deuzio</strong> sur ce sujet. {TODO("une phrase sur la mission Deuzio")}</p>
</div></section>

<section class="section"><div class="wrap">
  <span class="kicker">Comment ça se passe</span>
  <h2>De votre premier appel à un stock à jour</h2>
  <div class="grid g3 steps">
    <div class="step"><h3>Le diagnostic</h3><p>30 minutes, offertes, pour faire le point sur vos canaux de vente et votre façon de travailler.</p></div>
    <div class="step"><h3>La construction</h3><p>On relie vos plateformes par étapes, avec un point chaque semaine pour vous montrer l'avancement.</p></div>
    <div class="step"><h3>La mise en route</h3><p>On reprend votre stock actuel, on forme vos équipes, et on reste là pour faire évoluer l'outil.</p></div>
  </div>
</div></section>

<section class="section soft center"><div class="wrap">
  <span class="kicker">FAQ</span>
  <h2>Vos questions</h2>
  {faq([
    ("Quelles marketplaces pouvez-vous relier ?", f"{TODO('les plateformes déjà reliées pour LiLi et Deuzio')} Pour les autres, on vérifie ensemble pendant le diagnostic."),
    ("Faut-il changer de logiciel ou de site ?", "Non. On part de vos outils actuels et on les relie entre eux."),
    ("Que se passe-t-il si une plateforme ne répond plus ?", "L'outil vous prévient, pour qu'aucun article ne reste en vente par erreur."),
  ])}
</div></section>

<section class="section"><div class="wrap">
  <span class="kicker">Seconde main &amp; Réemploi</span>
  <h2>Les autres problèmes qu'on résout</h2>
  <div class="grid g2">
    <a class="card soon" href="#"><h3>Fiabiliser et accélérer l'estimation de vos articles</h3><p class="problem">L'estimation des articles dépend de l'expérience de chacun et prend un temps considérable.</p><span class="link-arrow">Découvrir →</span></a>
    <a class="card soon" href="#"><h3>Fixer le juste prix de revente</h3><p class="problem">Je fixe mes prix de revente sans référence fiable.</p><span class="link-arrow">Découvrir →</span></a>
  </div>
</div></section>
{cta_final("Vos stocks à jour partout, on en parle ?")}
"""
    page(PAGE_CAS, "Synchroniser vos stocks sur toutes vos marketplaces · Code4Good",
         "Un article vendu sur une marketplace reste en vente sur les autres ? Code4Good relie vos canaux de vente pour un stock à jour partout.", corps)


if __name__ == "__main__":
    accueil()
    secteur()
    cas()
