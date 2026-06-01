# KAdouane

Module Odoo de suivi des opérations douane, transport, import et export.

## Objectif

Ce module organise les demandes liées aux flux douane et transport. Il couvre les dossiers export, les dossiers import, les documents associés, les transporteurs, clients/fournisseurs, marchandises, DN, factures, remorques, BOM et pièces jointes.

## Dépendances

- `base`
- `mail`
- `web`

## Modèles principaux

- `kadouane.kadouane` : demande export principale.
- `kadouane.dmdimport` : demande import principale.
- `kadouane.categoryex` et `kadouane.categoryimport` : tableaux de bord par statut.
- `kadouane.client` : clients.
- `kadouane.supplier` : fournisseurs.
- `kadouane.transporteur` : transporteurs.
- `kadouane.dn`, `kadouane.dnwithatachement`, `kadouane.inv`, `kadouane.refexp`, `kadouane.remorque`, `kadouane.marchandise` : lignes et documents opérationnels.
- `kadouane.documentation` : documentation métier.

## Workflow export

La demande export suit notamment les étapes suivantes :

1. `nouvelle` : nouvelle demande.
2. `transport` : attente transport.
3. `picking` : attente picking.
4. `facturation` : attente facturation.
5. `douane` : attente transit.
6. `Cloture` : attente DUM.
7. `done` : attente fiche d'imputation.
8. `mainlevee` : attente main levée.
9. `archive` : dossier archivé.
10. `corbeille` : dossier supprimé logiquement.

## Workflow import

La demande import suit notamment les étapes suivantes :

1. `nouvelle` : nouvelle demande.
2. `transport` : attente transport.
3. `validationMlog` : validation manager logistique.
4. `validationMFi` : validation manager finance.
5. `validationMD` : validation MD.
6. `picking` : attente pick-up.
7. `factureFreight` : facture freight.
8. `douane` : envoi OT.
9. `bad`, `attenteDUM`, `ticketPaiment`, `caution`, `livraison` : suivi documentaire et livraison.
10. `archive` ou `corbeille`.

## Fonctionnement

- Les références sont générées automatiquement par séquence.
- Les actions de workflow déplacent les dossiers entre les statuts métier.
- Les pièces jointes sont liées aux documents DN, factures, transport, transit et autres documents.
- Les tableaux de bord calculent le nombre de dossiers par statut.
- Des vues calendrier permettent de suivre les dates opérationnelles.
- Le chatter permet le suivi des modifications et échanges.

## Rapports

Le module fournit des rapports pour les ordres de transit, transport et transit import.

## Sécurité

Les groupes et droits d'accès sont définis dans :

- `security/security.xml`
- `security/ir.model.access.csv`

## Assets

Des assets backend ajoutent des comportements calendrier et du style :

- `static/src/js/kadouane_calendar_drag.js`
- `static/src/scss/kadouane_calendar.scss`

