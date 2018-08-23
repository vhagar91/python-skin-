
from PyQt4.QtGui import QStandardItem
from config.loader import GCLIENT_DB_PATH
from pysqlcipher import dbapi2 as sqlcipher

try:
    db = sqlcipher.connect(GCLIENT_DB_PATH)
    # db.executescript('pragma key="12345678123456781234567812345678"; pragma kdf_iter=64000;')
except Exception as e:
    print e.message


class Component:

    def __init__(self, title, columns, rows):
        self.title = title
        self.columns = columns
        self.rows = rows


inventory = {
    'hardware': [
                {'table': 'microprocessor',
                 'title': 'Microprocessor',
                 'headers': ['Serial Number', 'Version', 'Speed', 'Family'],
                 'columns': [3, 4, 6, 8]},
                {'table': 'motherboard',
                 'title': 'Motherboard',
                 'headers': ['Serial Number', 'Product', 'Manufacturer', 'Version'],
                 'columns': [7, 4, 3, 5]},
                {'table': 'storagedevice',
                 'title': 'Storage Device',
                 'headers': ['Serial Number', 'Model', 'Interface', 'Capacity'],
                 'columns': [3, 6, 5, 4]},
                {'table': 'ram',
                 'title': 'RAM',
                 'headers': ['Serial Number', 'Type', 'Size', 'Manufacturer'],
                 'columns': [9, 3, 4, 7]},
                {'table': 'cdrom',
                 'title': 'CDROM',
                 'headers': ['Type', 'Model', 'Interface', 'Serial Number'],
                 'columns': [6, 5, 4, 3]},
                {'table': 'keyboard',
                 'title': 'Keyboard',
                 'headers': ['Family', 'Product', 'Supplier', 'Interface'],
                 'columns': [4, 6, 5, 3]},
                {'table': 'mouse',
                 'title': 'Mouse',
                 'headers': ['Family', 'Product', 'Supplier', 'Interface'],
                 'columns': [4, 6, 5, 3]},
                {'table': 'printer',
                 'title': 'Printer',
                 'headers': ['Product', 'Supplier', 'Interface'],
                 'columns': [5, 4, 3]},
                {'table': 'scanner',
                 'title': 'Scanner',
                 'headers': ['Product', 'Supplier', 'Interface'],
                 'columns': [5, 4, 3]},
                {'table': 'monitor',
                 'title': 'Monitor',
                 'headers': ['Serial Number', 'Manufacturer', 'Model'],
                 'columns': [5, 3, 4]},
               ],
    'software': [
                {'table': 'computer',
                 'title': 'Computer',
                 'headers': ['Name', 'Domain'],
                 'columns': [4, 3]},
                {'table': 'antivirus',
                 'title': 'Antivirus',
                 'headers': ['Name', 'Active?', 'Updated?'],
                 'columns': [7, 5, 6]},
                {'table': 'operatingsystem',
                 'title': 'Operating System',
                 'headers': ['Name', 'Version'],
                 'columns': [4, 3]},
                # {'table': 'systemuser',
                #  'title': 'User',
                #  'headers': ['Name', 'Local?', 'Logged?'],
                #  'columns': [4, 3, 5]}
                ]}


def get_all():
    components = {'hardware': [], 'software': []}
    for key, ls_compts in inventory.iteritems():
        for comp in ls_compts:
            query = get_query(comp['table'])
            rows = []
            for cursor in query:
                row = []
                for idx in comp['columns']:
                    row.append(QStandardItem(str(cursor[idx])))
                rows.append(row)
            components[key].append(Component(comp['title'], comp['headers'], rows))
    return components


def get_query(component):
    return db.execute('select * from %s;' % component).fetchall()


if __name__ == '__main__':
    get_all()
