# KAdouane


> Documentation fonctionnelle et technique du module de suivi douane, transport, import et export.


## Vue d?ensemble

KAdouane centralise les dossiers douane et transport pour les flux export et import. Le module permet de cr?er des demandes, suivre leur avancement op?rationnel, rattacher les documents n?cessaires, g?rer les transporteurs, clients, fournisseurs, DN, factures, remorques, marchandises et rapports associ?s. Il sert de point de suivi entre les ?quipes logistique, transport, finance, douane et management.

## Utilisateurs concern?s

- Demandeur logistique/export : cr?e et compl?te les dossiers.
- Responsable transport : renseigne les informations transporteur et exp?dition.
- Responsable douane/transit : suit les documents douaniers, DUM, mainlev?e et caution.
- Finance/management : intervient sur les validations et le suivi documentaire.
- Administrateur : configure les acc?s, listes de base et s?quences.

## Workflow m?tier

1. Export : nouvelle demande
2. Attente transport
3. Attente picking
4. Attente facturation
5. Attente transit/douane
6. Attente DUM
7. Fiche d'imputation
8. Main lev?e
9. Archive ou corbeille

## Workflow compl?mentaire

1. Import : nouvelle demande
2. Attente transport
3. Validation manager logistique
4. Validation manager finance
5. Validation MD
6. Attente pick-up
7. Facture freight
8. Envoi OT
9. BAD/DUM/ticket paiement/caution
10. R?ception puis archive

## Fonctionnement op?rationnel

- Cr?er une demande depuis le menu KAdouane.
- Renseigner les informations de client/fournisseur, transporteur, dates et documents.
- Ajouter les DN, factures, remorques, marchandises ou pi?ces jointes n?cessaires.
- Utiliser les boutons de workflow pour passer au statut suivant.
- Suivre les compteurs par statut dans les vues cat?gories/tableaux de bord.
- Archiver le dossier lorsque le flux est termin?.

## Configuration recommand?e

- Cr?er les clients, fournisseurs et transporteurs utilis?s par les demandes.
- V?rifier les s?quences charg?es dans data/kadouanesequ.xml.
- Configurer les groupes de s?curit? selon les responsabilit?s.
- V?rifier les rapports QWeb li?s aux ordres de transit et transport.

## D?pendances Odoo

- `base`
- `mail`
- `web`

## Mod?les techniques

- `kadouane.documentation` : Documentation (`models/documentation.py`)
- `kadouane.kadouane` : kadouane.kadouane (`models/models.py`)
- `kadouane.dn` (`models/models.py`)
- `kadouane.dnwithatachement` (`models/models.py`)
- `kadouane.client` : kadouane.client (`models/models.py`)
- `kadouane.transporteur` : kadouane.transporteur (`models/models.py`)
- `kadouane.refexp` : kadouane.refexp (`models/models.py`)
- `kadouane.dechargeexportngp` : kadouane.dechargeexportngp (`models/models.py`)
- `kadouane.remorque` : kadouane.remorque (`models/models.py`)
- `kadouane.bom` : kadouane.bom (`models/models.py`)
- `kadouane.inv` : kadouane.inv (`models/models.py`)
- `kadouane.autresdocs` : kadouane.autresdocs (`models/models.py`)
- `kadouane.categoryex` : kadouane.categoryex (`models/models.py`)
- `kadouane.supplier` : kadouane.supplier (`models/modelsImport.py`)
- `kadouane.marchandise` : kadouane.marchandise (`models/modelsImport.py`)
- `kadouane.autresdocsimport` : kadouane.autresdocsimport (`models/modelsImport.py`)
- `kadouane.categoryimport` : kadouane.categoryimport (`models/modelsImport.py`)
- `kadouane.dmdimport` : kadouane.dmdimport (`models/modelsImport.py`)

## ?tats d?tect?s dans le code

- `models/models.py` : `nouvelle` (Nouvelle demande), `transport` (Attente Transport), `picking` (Attente picking), `facturation` (Attente Facturation), `douane` (Attente Transit), `Cloture` (Attente DUM), `done` (Attente F imputation), `mainlevee` (Attente main levee), `archive` (Archive), `corbeille` (Corbeille)
- `models/modelsImport.py` : `nouvelle` (Nouvelle demande), `transport` (Attente Transport), `validationMlog` (val manager Log), `validationMFi` (val manager FI), `validationMD` (Val MD), `picking` (Attente pick-up), `douane` (Envoi OT), `factureFreight` (facture Freight), `bad` (BAD), `attenteDUM` (DUM), `ticketPaiment` (ticketPaiment), `caution` (Att de caution), `livraison` (Att de Reception), `archive` (Archive), `corbeille` (Corbeille)

## Actions serveur principales

- `action_transport` (`models/models.py`)
- `action_nouvelle` (`models/models.py`)
- `action_supprimer` (`models/models.py`)
- `action_facturation` (`models/models.py`)
- `action_picking` (`models/models.py`)
- `action_douane` (`models/models.py`)
- `action_exp` (`models/models.py`)
- `action_dedouane` (`models/models.py`)
- `action_Cloture` (`models/models.py`)
- `action_done` (`models/models.py`)
- `action_expdone` (`models/models.py`)
- `action_Cloture_done` (`models/models.py`)
- `action_nouvelle` (`models/models.py`)
- `action_transport` (`models/modelsImport.py`)
- `action_nouvelle` (`models/modelsImport.py`)
- `action_archive` (`models/modelsImport.py`)
- `action_supprimer` (`models/modelsImport.py`)
- `action_managerlog` (`models/modelsImport.py`)
- `action_respdouane` (`models/modelsImport.py`)
- `action_picking` (`models/modelsImport.py`)
- `action_freight` (`models/modelsImport.py`)
- `action_bad` (`models/modelsImport.py`)
- `action_dum` (`models/modelsImport.py`)
- `action_ticket` (`models/modelsImport.py`)
- `action_caution` (`models/modelsImport.py`)
- `action_liv` (`models/modelsImport.py`)
- `action_nouvelle` (`models/modelsImport.py`)

## Fichiers charg?s par le manifest

- `security/security.xml`
- `security/ir.model.access.csv`
- `views/views.xml`
- `views/viewssupp.xml`
- `views/client.xml`
- `views/documentation.xml`
- `views/calendarexp.xml`
- `views/calendarImp.xml`
- `views/templates.xml`
- `data/kadouanesequ.xml`
- `reports/report.xml`
- `reports/order_transit.xml`
- `reports/order_transport.xml`
- `reports/order_transit_import.xml`

## S?curit? et droits

Le module s?appuie sur les fichiers suivants pour d?finir les groupes, r?gles d?enregistrement et droits d?acc?s :

- `security/ir.model.access.csv`
- `security/security.xml`

## Rapports

- `reports/order_transit.xml`
- `reports/order_transit_import.xml`
- `reports/order_transport.xml`
- `reports/report.xml`

## Assets et interface

- `static/src/js/kadouane_calendar_drag.js`
- `static/src/scss/kadouane_calendar.scss`
- `static/src/scss/kadouane_dashboard.scss`

## Bonnes pratiques d?utilisation

- V?rifier que chaque utilisateur Odoo est li? au bon employ? lorsque le module d?pend de `hr.employee`.
- Tester le workflow avec un dossier de test avant utilisation en production.
- Contr?ler les groupes de s?curit? apr?s installation afin que seuls les bons r?les voient les boutons de validation.
- Garder les templates e-mail et rapports align?s avec les proc?dures internes.
- Sauvegarder la base avant toute modification structurelle du module.

## Maintenance

- Les ?volutions fonctionnelles doivent ?tre ajout?es dans les mod?les Python, les vues XML et les r?gles de s?curit? correspondantes.
- Apr?s modification des vues, mettre ? jour le module depuis Odoo ou red?marrer le serveur selon le type de changement.
- Apr?s modification des assets, vider le cache navigateur et recompiler les assets si n?cessaire.
- Toute nouvelle ?tape de workflow doit ?tre accompagn?e des droits, boutons, notifications et filtres correspondants.
