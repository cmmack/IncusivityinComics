import locale

import io

grandcomics = 'grandcomics.sql' 

#Def for guessing the encoding of the SQL file

def guess_encoding(grandcomics):

    """guess the encoding of the given file"""

    with io.open("grandcomics.sql", "rb") as f:

        data = f.read(5)

    if data.startswith(b"\xEF\xBB\xBF"):  # UTF-8 with a "BOM"

        return "utf-8-sig"

    elif data.startswith(b"\xFF\xFE") or data.startswith(b"\xFE\xFF"):

        return "utf-16"

    else:  # guessing utf-8 doesn't work in Windows, so we just give it a try:

        try:

            with io.open("grandcomics.sql", encoding="utf-8") as f:

                return "utf-8"

        except:

            return locale.getdefaultlocale()[1]
        
import textwrap

#def for creating query string

def create_query_string(grandcomics):

    with open(grandcomics, 'r', encoding=guess_encoding(grandcomics)) as f_in:

        lines = f_in.read()

        # remove common leading whitespace from all lines    

        query_string = textwrap.dedent("""{}""".format(lines))

        return query_string

print('Found the file and created a converted string.')
