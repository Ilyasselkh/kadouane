# KAdouane

Module Odoo de suivi douane, transport, import et export. Il centralise les demandes, les documents, les transporteurs, les clients, les fournisseurs, les DN, les factures, les marchandises, les remorques et les rapports associes.

## Objectif

Cette documentation explique le perimetre fonctionnel du module, les roles utilisateurs, le workflow, la configuration et les principaux objets techniques.

## Utilisateurs concernes

- Demandeur logistique ou export
- Responsable transport
- Responsable douane ou transit
- Finance et management
- Administrateur Odoo

## Workflow metier

1. Export: nouvelle demande
2. Attente transport
3. Attente picking
4. Attente facturation
5. Attente transit ou douane
6. Attente DUM
7. Fiche imputation
8. Main levee
9. Archive ou corbeille
10. Import: nouvelle demande, validations logistique/finance/MD, pick-up, freight, OT, DUM, caution, reception

## Fonctionnement operationnel

- Creer une demande depuis le menu KAdouane.
- Renseigner client ou fournisseur, transporteur, dates et documents.
- Ajouter DN, factures, remorques, marchandises et pieces jointes.
- Utiliser les boutons de workflow pour changer de statut.
- Suivre les compteurs par statut.
- Archiver le dossier termine.

## Configuration recommandee

- Configurer les clients, fournisseurs et transporteurs.
- Verifier les sequences dans data/kadouanesequ.xml.
- Configurer les groupes de securite.
- Verifier les rapports QWeb de transport et transit.

## Dependances Odoo

- `base`
- `mail`
- `web`
- `website`

## Modeles principaux

- `kadouane.kadouane`
- `kadouane.dmdimport`
- `kadouane.client`
- `kadouane.supplier`
- `kadouane.transporteur`
- `kadouane.dn`
- `kadouane.inv`
- `kadouane.remorque`
- `kadouane.marchandise`
- `kadouane.documentation`

## Structure importante du module

- `security/ir.model.access.csv`
- `security/security.xml`
- `data/kadouanesequ.xml`
- `views/calendarexp.xml`
- `views/calendarImp.xml`
- `views/client.xml`
- `views/documentation.xml`
- `views/templates.xml`
- `views/views.xml`
- `views/viewssupp.xml`
- `reports/order_transit.xml`
- `reports/order_transit_import.xml`
- `reports/order_transport.xml`
- `reports/report.xml`
- `models/__init__.py`
- `models/documentation.py`
- `models/models.py`
- `models/modelsImport.py`

## Securite

Les droits sont geres par les fichiers du dossier `security`. Il faut verifier les groupes, les regles enregistrement et les acces CSV apres installation ou modification du module.

## Notifications et suivi

Les modules qui dependent de `mail` utilisent le chatter Odoo pour tracer les changements. Les templates mail presents dans le dossier `data` servent a notifier les acteurs concernes par les transitions.

## Installation

1. Copier le module dans le dossier addons Odoo.
2. Redemarrer le serveur Odoo si necessaire.
3. Mettre a jour la liste des applications.
4. Installer ou mettre a jour le module.
5. Verifier les droits utilisateurs et tester un dossier de bout en bout.

## Maintenance

- Ajouter toute nouvelle etape a la fois dans le modele Python, les vues XML, les droits et les notifications.
- Tester les workflows avec plusieurs roles utilisateurs.
- Mettre a jour les rapports et templates mail quand la procedure interne change.
- Eviter de modifier les donnees de production sans sauvegarde.
- Documenter toute evolution fonctionnelle dans ce README.
