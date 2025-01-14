# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2021-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    "name": "Vista Backend Theme V14",
    "description": """Minimalist and elegant backend theme for Odoo 14, Backend Theme, Theme""",
    "summary": "Vista Backend Theme V14 is an attractive theme for backend",
    "category": "Themes/Backend",
    "version": "14.0.1.0.0",
    'author': 'Frontware, Cybrosys Techno Solutions',
    'company': 'Frontware, Cybrosys Techno Solutions',
    'maintainer': 'Frontware, Cybrosys Techno Solutions',
    'website': "https://github.com/Frontware/CybroAddons",
    "depends": ['base', 'web', 'mail', 'web_responsive'],
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.gif',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/icons.xml',
        'views/layout.xml',
        'views/theme.xml',
        'data/theme_data.xml',
    ],
    "qweb": [
        'static/src/xml/sidebar.xml',
        'static/src/xml/styles.xml',
        'static/src/xml/top_bar.xml',
        'static/src/xml/systray.xml',
    ],
    'license': 'LGPL-3',
    'pre_init_hook': 'test_pre_init_hook',
    'post_init_hook': 'test_post_init_hook',
    'installable': True,
    'application': False,
    'auto_install': False,
}
