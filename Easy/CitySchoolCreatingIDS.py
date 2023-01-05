def create_id(firstname, lastname):
  return "{0}{1}{2}".format(str(firstname)[0].lower(), str(lastname)[0].upper(), str(lastname)[1:3].lower())