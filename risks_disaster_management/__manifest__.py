{
    'name' :'risk_disaster_management',
    'version':'1.1',
    'summary':'different type of risks',
    'catagory':'project','website'
    'sequence':10,
    'depends':["hr","crm","sms","base","mail","website","base_geolocalize", "website_partner", "im_livechat","project","website_google_map","stock"],
    'data':[
        'security/ir.model.access.csv',
        'security/notification_group_security.xml',
        'data/activity_notify.xml',
        'views/risk_view.xml',
        'views/super_observer_action.xml',
        'views/risk_config_view.xml',
        'views/risk_project_view.xml',
        'views/risks_dashboard_views.xml',
        'views/menus.xml',
        'views/cantatct_company.xml',
        'views/comunication_action.xml',
        'views/external_ressource_view.xml',
        'views/view.xml',
        'views/res_company.xml',
        'views/wizard.xml',
        'views/risk_activity.xml',
        'views/risk_dashboard.xml',
        'report/risk_management_report.xml',
        'report/risk_management_template.xml',
        'views/stock_damage_view.xml',




    ],
    # 'images': ['static/description/src/banner.jpg',
    #            'static/description/src/car-marlon.jpg',
    #            'static/description/src/icon1.png',
    #            'static/description/src/img-1..jpeg',
    #            'static/description/src/img-2.jpg',
    #            'static/description/src/img-3.jpg'
    #            ],
    'qweb': [
            'static/description/src/index.html',

        ],
    'license': 'AGPL-3',
    'auto_install': False,
    'installable': True,
    'application': True,





}