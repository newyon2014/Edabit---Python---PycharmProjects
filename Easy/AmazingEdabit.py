def amazing_edabit(s):
  return s if str(s).__contains__("edabit") else "{} is {} amazing.".format(str(s)[0:str(s).index("is") - 1], "not")