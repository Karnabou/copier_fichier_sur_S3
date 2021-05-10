#  Filtrer les éléments - version 1.0
#  Importer les modules pour obtenir le type de fichier

import os
import mimetypes

# Importer la bibliotèque datetime
import arrow

additional_file_types = {
    '.md': 'text/markdown'
}

# Focntion date
def datetimeformat(date_str):
    dt = arrow.get(date_str)
    return dt.humanize(locale='fr')

# Focntion inspecter le fichier pour obtenir son type 
def file_type(key):
    file_info = os.path.splitext(key)
    file_extension = file_info[1]
    try:
        return mimetypes.types_map[file_extension]
    except KeyError:
        filetype = 'Inconnu'
        if file_info[0].startswith('.') and file_extension == '':
            filetype = 'text'

        if file_extension in additional_file_types.keys():
            filetype = additional_file_types[file_extension]

        return filetype
