from odoo import api, fields, models


class Vehicle(models.Model):
	_name = "transport.vehicle"
	_description = "Company Vehicles"
	_order = "vehicle_reg asc"

	vehicle_id = fields.Char("ID", required=True)
	assignee = fields.Boolean('Assign to an Employee?')
	assigned_employee_id = fields.Many2one("hr.employee", string='Assigned Employee')
	assigned_bu_id = fields.Many2one("hr.employee", string='Assigned Business Unit')
	vehicle_reg = fields.Char('Vehicle Registration No.', required=True)
	mileage = fields.Char('Mileage')	
	make = fields.Char('Make', required=True)
	car_model = fields.Char('Model', required=True)
	color = fields.Char('Colour', required=True)
	active = fields.Boolean('Active', default=True)
	date_acquired = fields.Datetime('Date Acquired', default=fields.Datetime.now)
	status = fields.Selection([('new','New'),('pending_approval','Pending Approval'),('verified','Verified'),('repairs','Being Repaired'),('sold','Sold'),('in_use','In Use')], default='new')

	def action_submit_new_vehicle(self):
		for record in self:
			record.status= 'pending_approval'
		return True

		

