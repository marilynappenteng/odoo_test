from odoo import fields, models



class EngineeringCase(models.Model):
	_name = "engineering.case"
	_description = "Engineering Cases"

	case_id = fields.Char('Name', required=True)
	title = fields.Char('Title', required=True)
