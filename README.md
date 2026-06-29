# KAdouane

Module Odoo de suivi des dossiers douane, transport, import et export.

Le module centralise les demandes export et import, les clients, fournisseurs, transporteurs, DN, factures, marchandises, remorques, documents douaniers, rapports de transport et de transit.

## Objectif fonctionnel

Piloter les dossiers douane et transport depuis la creation de la demande jusqu'a l'archivage.

Le module permet de :

- creer une demande export ;
- creer une demande import ;
- suivre les etapes transport, picking, facturation et douane ;
- gerer les clients, fournisseurs et transporteurs ;
- importer ou controler des fichiers Excel ;
- rattacher les DN, factures, marchandises et documents ;
- suivre les valeurs transport et transit ;
- gerer les validations import ;
- suivre les DUM, mainlevees, cautions et tickets de paiement ;
- imprimer les rapports de transit et transport ;
- archiver les dossiers termines ;
- tracer les changements dans le chatter.

## Roles fonctionnels

### ADV / demandeur export

L'utilisateur ADV cree les demandes export et renseigne les donnees client.

Il peut :

- creer une demande ;
- renseigner le client, incoterm, ship-to et bill-to ;
- ajouter les DN et factures ;
- planifier le picking ;
- suivre l'expedition.

### Logistique / transport

La logistique pilote les informations de transport.

Elle peut :

- choisir le transporteur ;
- renseigner le type de transport ;
- renseigner les couts transport ;
- confirmer les etapes transport et picking ;
- suivre les expeditions.

### Douane / transit

Le service douane gere le transit et les documents associes.

Il peut :

- renseigner le transitaire ;
- suivre la DUM ;
- ajouter les documents douaniers ;
- gerer mainlevee et fiche d'imputation ;
- archiver le dossier.

### Finance / management

Finance et management interviennent sur les validations et les indicateurs de paiement.

### Administrateur

L'administrateur gere les referentiels, groupes, vues et rapports.

## Flux export

Les etats export principaux sont :

- `Nouvelle demande`
- `Attente Transport`
- `Attente picking`
- `Attente Facturation`
- `Attente Transit`
- `Attente DUM`
- `Attente F imputation`
- `Attente main levee`
- `Archive`
- `Corbeille`

Flux standard export :

1. `Nouvelle demande`
2. `Attente Transport`
3. `Attente picking`
4. `Attente Facturation`
5. `Attente Transit`
6. `Attente DUM`
7. `Attente F imputation`
8. `Attente main levee`
9. `Archive`

## Flux import

Les etats import principaux sont :

- `Nouvelle demande`
- `Attente Transport`
- `Validation Manager Log`
- `Validation Manager FI`
- `Validation MD`
- `Attente pick-up`
- `Envoi OT`
- `Facture Freight`
- `BAD`
- `DUM`
- `Ticket paiement`
- `Attente caution`
- `Attente Reception`
- `Archive`
- `Corbeille`

## Donnees gerees

Le module gere notamment :

- clients ;
- fournisseurs ;
- transporteurs ;
- DN ;
- DN avec piece jointe ;
- references expedition ;
- factures ;
- remorques ;
- marchandises ;
- inventaires ;
- BOM ;
- documents supplementaires export ;
- documents supplementaires import ;
- categories export et import ;
- documentation interne.

## Documents

Les documents peuvent couvrir notamment :

- transport ;
- transitaire ;
- DUM ;
- facture ;
- CMR ;
- fiche d'imputation ;
- mainlevee ;
- photo ;
- BAD ;
- devis transport ;
- devis transitaire ;
- fiche liquidation ;
- autre.

## Rapports

Le module fournit plusieurs rapports QWeb :

- rapport principal ;
- ordre de transit ;
- ordre de transport ;
- ordre de transit import.

Fichiers principaux :

- `reports/report.xml`
- `reports/order_transit.xml`
- `reports/order_transport.xml`
- `reports/order_transit_import.xml`

## Modeles principaux

- `kadouane.kadouane`
- `kadouane.dmdimport`
- `kadouane.client`
- `kadouane.supplier`
- `kadouane.transporteur`
- `kadouane.dn`
- `kadouane.dnwithatachement`
- `kadouane.refexp`
- `kadouane.inv`
- `kadouane.remorque`
- `kadouane.marchandise`
- `kadouane.autresdocs`
- `kadouane.autresdocsimport`
- `kadouane.documentation`

## Structure du module

- `security/security.xml`
- `security/ir.model.access.csv`
- `data/kadouanesequ.xml`
- `views/views.xml`
- `views/viewssupp.xml`
- `views/client.xml`
- `views/documentation.xml`
- `views/calendarexp.xml`
- `views/calendarImp.xml`
- `views/templates.xml`
- `reports/report.xml`
- `reports/order_transit.xml`
- `reports/order_transport.xml`
- `reports/order_transit_import.xml`
- `models/models.py`
- `models/modelsImport.py`
- `models/documentation.py`
- `static/src/js/kadouane_calendar_drag.js`
- `static/src/scss/kadouane_calendar.scss`

## Installation

1. Copier le module dans le dossier addons Odoo.
2. Redemarrer le serveur Odoo si necessaire.
3. Mettre a jour la liste des applications.
4. Installer le module.
5. Configurer les groupes douane, transport, logistique, finance et management.
6. Creer les clients, fournisseurs et transporteurs.
7. Tester un dossier export.
8. Tester un dossier import.
9. Verifier les rapports.

## Maintenance fonctionnelle

Lorsqu'une procedure douane ou transport change, verifier aussi :

- les etats export ;
- les etats import ;
- les vues calendrier ;
- les rapports ;
- les groupes de securite ;
- les traitements Excel ;
- les documents obligatoires ;
- ce README.
