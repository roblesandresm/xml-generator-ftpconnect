import pandas as pd
import xml.etree.ElementTree as ET

# Función para convertir un DataFrame a elementos XML con nombres de etiquetas personalizados
def dataframe_to_xml(df, root_name='vivino-product-list', row_name='product', column_names=None):
    root = ET.Element(root_name)
    for _, row in df.iterrows():
        item = ET.SubElement(root, row_name)
        for col_name, value in row.items():
            # Usa nombres de etiquetas personalizados si están proporcionados
            tag_name = column_names.get(col_name, col_name) if column_names else col_name
            child = ET.SubElement(item, tag_name)
            child.text = str(value)
    return root

# ruta de archivos
xlsx_file_path = './Articles-30.xls'
xml_file_path = 'products-list.xml'

# Lee el archivo Excel
df = pd.read_excel('./Articles-30.xls')

# Nombres de etiquetas personalizados
custom_column_names = {
    'Nombre_Columna_1': 'CustomName1',
    'Nombre_Columna_2': 'CustomName2',
    # Agrega más nombres de columna según sea necesario
}

# Convierte el DataFrame a elementos XML con nombres de etiquetas personalizados
root_element = dataframe_to_xml(df)

# Crea un objeto ElementTree y guarda el XML en un archivo
tree = ET.ElementTree(root_element)
tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

print(f'Se ha creado el archivo XML en: {xml_file_path}')
