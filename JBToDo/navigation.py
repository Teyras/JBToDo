from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator

nav = Nav()

nav.register_element('top', Navbar(
    'JBToDo',
    View('Task list', 'index'),
    View('New task', 'new')
))
