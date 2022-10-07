def front3(txt):
  return str(txt) * 3 if len(str(txt)) < 3 else str(txt)[:3]*3 if len(str(txt)) > 1 else " "