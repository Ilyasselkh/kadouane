# -*- coding: utf-8 -*-

from odoo import models, fields, api
import openpyxl
import base64
from io import BytesIO
from odoo import exceptions 
import collections
import math
from odoo.exceptions import ValidationError


class kadouaneSupplier(models.Model):
    _name = 'kadouane.supplier'
    _description = 'kadouane.supplier'
    _order = "create_date desc"



    name = fields.Char(tracking=True)
    
    vendor = fields.Integer(tracking=True)
    adress = fields.Char(tracking=True)

    incoterm = fields.Char(tracking=True)
    transportmanagement = fields.Boolean(tracking=True)
    transitmanagement = fields.Boolean(tracking=True)
    arnetwork = fields.Boolean(tracking=True)
    domicilation = fields.Selection([('SG', 'SAHAM BANQUE'),('Attijari', 'attijariwafa bank')] ,string="domiciliation",tracking=True)

class kadouaneSupplier(models.Model):
    _name = 'kadouane.marchandise'
    _description = 'kadouane.marchandise'


    #CFACTURE => complement de facture au cas ou la meme facture avec plusieurs regimes
    typetransport = fields.Selection([('COLIS', 'COLIS'),('CARTON', 'CARTON'),('PALETTE', 'PALETTE'),('CFacture', 'CFacture')] ,string="Type de la marchandise",tracking=True)
    nbr = fields.Float(tracking=True,string="nombre")
    poids = fields.Float(tracking=True,string="Poids NET en KG")
    valeur = fields.Float(tracking=True,string="Valeur")
    Long = fields.Float(tracking=True,string="Longeur en 'cm'")
    Largeur = fields.Float(tracking=True,string="Largeur en 'cm'")
    hauteur = fields.Float(tracking=True,string="hauteur en 'cm'")
    Volume = fields.Float(tracking=True,string="Volume 'm3'")
    FactureN = fields.Char(tracking=True,string="Num Facture")
    BlN = fields.Char(tracking=True,string="Num BL")
    DUMN = fields.Char(tracking=True,string="DUM")
    regime = fields.Selection([('010', '010'),('051', '051'),('311', '311'),('022', '022'),('037', '037'),('047', '047'),('082', '082'),('sans', 'sans')] ,string="Regime",tracking=True)
     # Different tables for each attachment
    dn_attachment_ids = fields.Many2many('ir.attachment', 
                                          'relationship_dn_attachments',  # Use a unique relationship name
                                          'marchandise_id', 
                                          'attachment_id', 
                                          string='Attachments DN')

    invoice_attachment_ids = fields.Many2many('ir.attachment', 
                                               'relationship_invoice_attachments',  # Use another unique relationship name
                                               'marchandise_id', 
                                               'attachment_id', 
                                               string='Attachments Invoice')

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._fix_attachment_ownership()
        return records

    def write(self, vals):
        res = super().write(vals)
        self._fix_attachment_ownership()
        return res

    def _fix_attachment_ownership(self):
        for record in self:
            for att in record.dn_attachment_ids | record.invoice_attachment_ids:
                att.write({'res_model': record._name, 'res_id': record.id})
        return self

    commentairedanslorderdetransit = fields.Char(tracking=True,string="commentaire OT")
    commentaireinterne = fields.Char(tracking=True,string="commentaire interne")
    @api.constrains('poids', 'valeur', 'Long', 'Largeur', 'hauteur', 'Volume','DUMN')
    def _check_positive_values(self):
        for record in self:
            if record.poids <= 0:
                raise ValidationError("Le poids NET doit être supérieur à 0.")
            if record.valeur <= 0:
                raise ValidationError("La valeur doit être supérieure à 0.")
            if record.Long <= 0:
                raise ValidationError("La longueur doit être supérieure à 0.")
            if record.Largeur <= 0:
                raise ValidationError("La largeur doit être supérieure à 0.")
            if record.hauteur <= 0:
                raise ValidationError("La hauteur doit être supérieure à 0.")
            if record.DUMN:   
                if len(record.DUMN) < 17:
                    raise ValidationError("Le numéro DUM est erroné.")
            

            
            
    @api.constrains('dn_attachment_ids', 'invoice_attachment_ids')
    def _check_attachments(self):
        for record in self:
            if not record.dn_attachment_ids:
                raise ValidationError("Au moins un fichier doit être fourni pour les Bon de Livraison (Attachments DN).")
            if not record.invoice_attachment_ids:
                raise ValidationError("Au moins un fichier doit être fourni pour les Factures (Attachments Invoice).")
    dmd_id = fields.Many2one('kadouane.dmdimport', string='dmnd')   

class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    @api.model
    def _read_attachment(self, attachment):
        # Allow any user in kadouane.moduleacces to read attachments
        if self.env.user.has_group('kadouane.moduleacces'):
            return True
        return super(IrAttachment, self)._read_attachment(attachment)
        
class kadouaneautreDocsimport(models.Model):
    _name = 'kadouane.autresdocsimport'
    _description = 'kadouane.autresdocsimport'



  
    docu_id = fields.Many2one('kadouane.dmdimport', string='dn')
    
    namedoc = fields.Char(string="Nom document",tracking=True)
    typedoc = fields.Selection([('BAD', 'BAD'),('devistransitaire', 'devis transitaire'),('devistranport', 'devis transport'),('DUM', 'DUM'), ('FactureFreight', 'Facture Freight'), ('CMR', 'CMR'), ('photo', 'photo'),('ficheliquidation', "Fiche liquidation"),('mainlevee', "Mainlevée"),('autre', "autre")], required=True)
    attachment_fichier_ids  = fields.Binary(string="Fichier",attachment=True)

    commentaire = fields.Char(string="Commentaire",tracking=True)
    anomalie = fields.Boolean(string="Anomalie",tracking=True)





class kadouane(models.Model):
    _name = 'kadouane.categoryimport'
    _description = 'kadouane.categoryimport'



    title = fields.Char(tracking=True)
    color = fields.Char(tracking=True)
    fieldname = fields.Char(tracking=True)
    countnvl = fields.Integer(compute='_get_count_rec',default=0)
    counttransport = fields.Integer(compute='_get_count_rec',default=0)
    countlogman = fields.Integer(compute='_get_count_rec',default=0)

    countfiman = fields.Integer(compute='_get_count_rec',default=0)
    countmd = fields.Integer(compute='_get_count_rec',default=0)
    countpicking = fields.Integer(compute='_get_count_rec',default=0)
    countot= fields.Integer(compute='_get_count_rec',default=0)
    countfreight = fields.Integer(compute='_get_count_rec',default=0)
    countbad = fields.Integer(compute='_get_count_rec',default=0)

    countdum = fields.Integer(compute='_get_count_rec',default=0)
    countticketpaiment = fields.Integer(compute='_get_count_rec',default=0)
    countattcaution = fields.Integer(compute='_get_count_rec',default=0)
    countrecp = fields.Integer(compute='_get_count_rec',default=0)
    countArchive = fields.Integer(compute='_get_count_rec',default=0)
    countArchiveOK = fields.Integer(compute='_get_count_rec',default=0)
    countcorbeille = fields.Integer(compute='_get_count_rec',default=0)
    
    statename = fields.Selection([('nouvelle', 'Nouvelle demande'),('transport', 'Attente Transport'),('validationMlog', 'val manager Log'), ('validationMFi', 'val manager FI'), ('validationMD', 'Val MD'), ('picking', 'Attente pick-up'), ('douane', 'Envoi OT'),('factureFreight', 'facture Freight'),  ('bad', 'BAD'),('attenteDUM', 'DUM'),  ('ticketPaiment', 'ticketPaiment'), ('caution', 'Att de caution'),('livraison', 'Att de Reception'), ('archive', 'Archive'), ('corbeille', 'Corbeille')], default ='nouvelle' ,string="Status",tracking=True)
   
    def get_stock_picking_action_picking_type1(self):
        return self._get_action('kadouane.action_window2')
    
    def get_create_nouvelledemande_form_action(self):
        return {
            'res_model' : 'kadouane.dmdimport',
            'type' :  'ir.actions.act_window',
            'view_mode' : 'form',
            'view_type' : 'form',
            'view_id' : self.env.ref("kadouane.view_dmd_imp_form").id,
            'target' : 'self'
        }

    def _get_count_rec(self):
        for rec in self:
            rec.countnvl = self.env['kadouane.dmdimport'].search_count([('state','=','nouvelle')])
            rec.counttransport = self.env['kadouane.dmdimport'].search_count([('state','=','transport')])
            rec.countlogman = self.env['kadouane.dmdimport'].search_count([('state','=','validationMlog')])
            rec.countfiman = self.env['kadouane.dmdimport'].search_count([('state','=','validationMFi')])    
            rec.countmd = self.env['kadouane.dmdimport'].search_count([('state','=','validationMD')])
            rec.countpicking = self.env['kadouane.dmdimport'].search_count([('state','=','picking')])
            rec.countot = self.env['kadouane.dmdimport'].search_count([('state','=','douane')])
            rec.countfreight = self.env['kadouane.dmdimport'].search_count([('state','=','factureFreight')])
            rec.countbad = self.env['kadouane.dmdimport'].search_count([('state','=','bad')])
            rec.countdum = self.env['kadouane.dmdimport'].search_count([('state','=','attenteDUM')])
            rec.countticketpaiment = self.env['kadouane.dmdimport'].search_count([('state','=','ticketPaiment')])
            rec.countattcaution = self.env['kadouane.dmdimport'].search_count([('state','=','caution')])
            rec.countrecp = self.env['kadouane.dmdimport'].search_count([('state','=','livraison')])
            rec.countArchive = self.env['kadouane.dmdimport'].search_count([('state','=','archive')])
            rec.countcorbeille = self.env['kadouane.dmdimport'].search_count([('state','=','corbeille')])


    def _get_action(self, action_xmlid):
        action = self.env["ir.actions.actions"]._for_xml_id(action_xmlid)
        if self:
            action['display_name'] = self.display_name

        return action

    



class KadouaneImportDmd(models.Model):
    _name = 'kadouane.dmdimport'
    _description = 'kadouane.dmdimport'
    _inherit = [ 'mail.thread', 'mail.activity.mixin']

    personneactontacternom = fields.Char(tracking=True,string="Personne a contacter")
    personneactontactertel = fields.Char(tracking=True,string="Tel")
    personneactontactemail = fields.Char(tracking=True,string="Email")
    referenceID = fields.Char( readonly=True, required=True, copy=False, default='Nouvelle demande') 

    state = fields.Selection([('nouvelle', 'Nouvelle demande'),('transport', 'Attente Transport'),('validationMlog', 'val manager Log'), ('validationMFi', 'val manager FI'), ('validationMD', 'Val MD'), ('picking', 'Attente pick-up'), ('douane', 'Envoi OT'),('factureFreight', 'facture Freight'),  ('bad', 'BAD'),('attenteDUM', 'DUM'),  ('ticketPaiment', 'ticketPaiment'), ('caution', 'Att de caution'),('livraison', 'Att de Reception'), ('archive', 'Archive'), ('corbeille', 'Corbeille')], default ='nouvelle' ,string="Status",tracking=True)
  
    name = fields.Char(string="Désignation",compute="get_name_calendar", tracking=True)
    name = fields.Char(string="Designation", compute="get_name_calendar", search="_search_name", tracking=True)
    attachment_imp_docs_ids = fields.One2many('kadouane.autresdocsimport', 'docu_id', string='autres documents',tracking=True)

    @api.depends('supplier_id')
    def get_name_calendar(self):
        for rec in self:
                rec.name = rec.supplier_id.name

    def _search_name(self, operator, value):
        return [('supplier_id.name', operator, value)]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('referenceID', 'Nouvelle demande') in [False, 'New', 'Nouvelle demande']:
                vals['referenceID'] = self.env['ir.sequence'].next_by_code(
                    'kadouane.dmdimport.sequence'
                ) or 'New'
        return super().create(vals_list)

    ismanager = fields.Boolean(string="ismanager", compute='get_user_grp')
    dateoperation =  fields.Datetime(string="Date d'operation",tracking=True)
    daterisk =  fields.Datetime(string="date de risque",tracking=True)
    pickingETD =  fields.Datetime(string="ETA",tracking=True)
    pickingETA =  fields.Datetime(string="ETD",tracking=True)

    pickingETDok = fields.Datetime(string="ETA validé",tracking=True)
    pickingETAok = fields.Datetime(string="ETD validé",tracking=True)

    trackingNumber =  fields.Char(string="Tracking number",tracking=True)

    customizedSupplier  = fields.Boolean(string="Autre fournisseur",tracking=True)
    customizedSupplier_RaisonSociale = fields.Char(string="Raison Sociale",tracking=True)
    customizedSupplier_Adresse = fields.Char(string="Adresse",tracking=True)
    customizedSupplier_contactName = fields.Char(string="Nom Personne à contacter",tracking=True)
    customizedSupplier_contactEmail = fields.Char(string="Email du contact",tracking=True)
    customizedSupplier_contactTel = fields.Char(string="Telphone du contact",tracking=True)
    customizedSupplier_incoterm = fields.Char(string="incoterm",tracking=True)

    supplier_id = fields.Many2one('kadouane.supplier', string='supplier',tracking=True)
    incoterm = fields.Char(string="Incoterm", compute="get_supplier_data", store="True")
    code = fields.Char(string="Ship to" , compute="get_supplier_data", store="True")
    billto = fields.Char(string="Bill to" , compute="get_supplier_data", store="True")
    arnetwork = fields.Char(string="AR network?" , compute="get_supplier_data", store="True")
    transitmanagement = fields.Boolean(string="Transit management",compute="get_supplier_data", store="True")

    datereception = fields.Datetime(string="Date de reception physique",tracking=True)


    @api.depends('ismanager')
    def get_user_grp(self):
        res_user = self.env['res.users'].search([('id', '=', self._uid)])
        if res_user.has_group('kadouane.group_resadv') or res_user.has_group('kadouane.group_log_manager'):
            self.ismanager = True
        else:
            self.ismanager = False
    typetransit = fields.Char(string="Type de transit",tracking=True)
    transitvalue = fields.Float(string="valeur du dossier",tracking=True)
    transitvalueExp = fields.Float(string="valeur des couts exceptionnels",tracking=True)
    transitvalueokpayment  = fields.Boolean(string="OK pour paiement",tracking=True)

    commentaireTransport = fields.Char(string="Commantaire",tracking=True)
    commentaireBL = fields.Char(string="Commantaire",tracking=True)
    commentairegen = fields.Char(string="Commantaire",tracking=True)
    commentaireinv = fields.Char(string="Commantaire",tracking=True)
    commentairetransaire = fields.Char(string="Commantaire",tracking=True)
    commentairetranautres = fields.Char(string="Commantaire",tracking=True)
    commentaireprepa = fields.Char(string="Commantaire PREPA",tracking=True)
    commentaireexp = fields.Char(string="Commantaire Reception",tracking=True)
    commentaireAdv = fields.Char(string="Commantaire demandeur",tracking=True)
    typetransport = fields.Selection([('ROUTIER', 'ROUTIER'),('AERIEN', 'AERIEN'),('MARITIME', 'MARITIME'),('FERROVIAIRE', 'FERROVIAIRE')] ,string="Type du transport",tracking=True)

    archivedone  = fields.Boolean(string="Dossier archivé",tracking=True)
    customsvaluefile = fields.Binary(string="Customs value", attachment=True)
    customsvalue = fields.Float(string="Customs value",tracking=True)

    transitaire = fields.Selection([('Gazet', 'Gazet'),('Timar','TIMAR')], default ='Timar',tracking=True)
    transitairereq  = fields.Char(compute="_is_tra_req", default="F") 

    
    @api.depends('state','supplier_id')
    def _is_tra_req(self):
        for rec in self:
            if rec.arnetwork == "True" or rec.state in ['douane', 'Cloture', 'done','mainlevee','archive']:
                rec.transitairereq = "T"
            else :
                rec.transitairereq = "F"


    @api.depends('supplier_id')
    def get_supplier_data(self):
        self.incoterm = self.supplier_id.incoterm
        self.billto = self.supplier_id.vendor
        self.arnetwork = self.supplier_id.arnetwork
        self.transitmanagement = self.supplier_id.transitmanagement

    valeurTransport = fields.Float(string="Valuer transport",tracking=True)
    valeurTransportExp = fields.Float(string="Autres frais",tracking=True)
    CURTransport = fields.Selection([('MAD', 'MAD'),('EUR', 'EUR'),('USD', 'USD')],tracking=True )
    valeurTransportok = fields.Float(string="Valuer transport facture",tracking=True)
    transportvalueokpayment  = fields.Boolean(string="OK pour paiement",tracking=True)

    transport_id = fields.Many2one('kadouane.transporteur', string='transporteur',tracking=True)


    transporteurReqNvlDmd = fields.Char(compute="_is_trans_req_nvl_dmd", default="F")
    transporteurReqNvlDmdred = fields.Char(compute="_is_trans_req_nvl_dmd", default="F")

    marchandise_ids = fields.One2many('kadouane.marchandise', 'dmd_id', string='Marchandise',tracking=True)

   
    
    def action_transport(self):
            if len(self.marchandise_ids) < 1:
                raise exceptions.UserError('Merci de rensigner minumum une operation dans la zone "Marchandise"')
            else:
                self.state = 'transport'
    
    def action_nouvelle(self):
        self.state = 'nouvelle'

    def action_archive(self):
        self.state = 'archive'

    def action_supprimer(self):
        self.state = 'corbeille'
    
    def action_managerlog(self):
        if all(record.typedoc != "devistranport" for record in self.attachment_imp_docs_ids):
                    raise ValidationError("Merci d'attacher les devis de transport.")
        else:
            self.state = 'validationMlog'

    def action_respdouane(self):
        self.state = 'picking'

    def action_picking(self):
        self.state = 'factureFreight'

    def action_freight(self):
        self.state = 'douane'

    def action_bad(self):
        if all(record.typedoc != "FactureFreight" for record in self.attachment_imp_docs_ids):
                    raise ValidationError("Merci d'attacher le documment Facture Freight.")
        else:
            self.state = 'bad'

    def action_dum(self):
        if all(record.typedoc != "BAD" for record in self.attachment_imp_docs_ids):
                    raise ValidationError("Merci d'attacher le documment BAD.")
        else:
            self.state = 'attenteDUM'

    def action_ticket(self):
        if all(record.typedoc != "DUM" for record in self.attachment_imp_docs_ids):
            raise ValidationError("Merci d'attacher le documment DUM.")
        if len(self.marchandise_ids) < 1:
                raise exceptions.UserError('Merci de rensigner minumum une operation dans la zone "Marchandise"')
        if any( not record.DUMN for record in self.marchandise_ids):
            raise ValidationError("Merci de renseigner le numero DUM pour chaque ligne.")
        else: 
            self.state = 'ticketPaiment'

    def action_caution(self):
        if  any(record.regime == "010" for record in self.marchandise_ids):
            if all(record.typedoc != "ficheliquidation" for record in self.attachment_imp_docs_ids):
                    raise ValidationError("Merci d'attacher le fichier de liquidation.")
            else:    
                self.state = 'caution'
        else:    
            self.state = 'caution'
        

    def action_liv(self):
        if all(record.typedoc != "mainlevee" for record in self.attachment_imp_docs_ids):
                    raise ValidationError("Merci d'attacher le fichier mainlevée ou l'email de transitaire.")
        else:
            self.state = 'livraison'      

    nbrpalletsadv = fields.Integer(string="Nbr palettesa expidier",tracking=True)
    nbrpalletcolis = fields.Integer(string="Nbr colis a expidier",tracking=True)
    nbrpalletcolisadvok = fields.Char(default="F", compute="_get_nbrpalstatus")
    @api.depends("nbrpalletsadv","nbrpalletcolis" )
    def _get_nbrpalstatus(self):
        for rec in self:
            if rec.nbrpalletsadv < 1 and rec.nbrpalletcolis <1:
                rec.nbrpalletcolisadvok = "F"
            else :
                rec.nbrpalletcolisadvok = "T"


    type = fields.Selection([('COLIS', 'COLIS'),('PALETTE', 'PALETTE'),('TC', 'TC')] ,string="Type d'expidition",tracking=True)
    typedmd = fields.Selection([('Normal', 'Normal'),('Express', 'Express'),('exceptionnelle', 'exceptionnelle'),('projet', 'projet')] ,string="Type de la demande",tracking=True)

    
    def action_nouvelle(self):
        self.state = 'nouvelle'

