from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EngineeringCase(models.Model):
	_name = "engineering.case"
	_description = "Engineering Cases"
	_order = "case_id desc, date_created desc"

	case_id = fields.Char('Name', required=True)
	title = fields.Char('Title', required=True)
	requested_by_id = fields.Many2one("hr.employee", string='Requested By', default=lambda self: self.env.user.employee_id.id, required=True)
	case_details = fields.Char('Case Details', required=True)
	case_comments = fields.Char('Case Comments')
	status = fields.Selection([('in_progress','In Progress'),('pending_approval','Pending Approval'),('completed','Completed'),('pending_assignment','Pending Assignment'),('on_hold','On Hold'),('evaluated','Evaluated'),('new', 'New'), ('pending_acknowledgement','Pending Acknowledgement')], index=True, required=True, default='new')
	expected_completion = fields.Datetime('Expected Completion Date')
	case_type = fields.Selection([('internal_automation', 'Internal Automation Support'),('internal_software', 'Internal Software Support'),('survey_boq', 'Survey & BOQ Support'),('rnd', 'Research & Development'),('meter_verification', 'Meter Verification'),('internal_training', 'Internal Training'),('commercial_training', 'Commercial Training'),('project_support', 'Project Support Task'),('other', 'Other Task')], index=True)
	assigned_to_id = fields.Many2one("hr.employee", string='Assigned To')
	approver_id = fields.Many2one("hr.employee", string='Approver')
	kpi_weight = fields.Integer('KPI Weight', default=1)
	work_done = fields.Char('Work Done')
	date_created = fields.Datetime('Date Created', default=fields.Datetime.now)
	approver_comments = fields.Char("Approver's Comments")
	date_assigned = fields.Datetime('Date Assigned')
	date_acknowledged = fields.Datetime('Date Acknowledged')
	deadline = fields.Datetime('Deadline')
	actual_completion = fields.Datetime('Actual Completion Date')
	rating = fields.Integer('Rate Us! How Satisfied Are You?', default=1)
	feedback = fields.Char('Requestor Feedback')
	active = fields.Boolean('Active', default=True)


	_sql_constraints = [ 
		('rate', 'CHECK(rating is NULL OR (rating >= 1 AND rating <= 5))', 'The rating must be between 1 and 5.'),
		('kpi_weight', 'CHECK(kpi_weight is NULL OR (kpi_weight >= 1 AND kpi_weight <= 5))', 'KPI Weight is between 1 and 5.')
	]

	def action_submit_case(self):
		for record in self:
			record.status = 'pending_acknowledgement'
		return True

	@api.constrains('deadline')
	def check_deadline(self):
		for record in self:
			if record.deadline:
				if record.deadline < fields.Datetime.now():
					raise ValidationError("The deadline cannot be set in the past.")

