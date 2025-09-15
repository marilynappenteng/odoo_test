{
	'name': 'Transport',
	'depends': [
		'base',
		'hr'
	],
	'data': [
		'security/ir.model.access.csv',

		'views/vehicle_views.xml',
		'views/transport_menus.xml'
	],
	'installable': True,
	'application': True,
	'auto-install': True
}
