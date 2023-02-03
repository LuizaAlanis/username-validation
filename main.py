def lenghtIsValid(strParam):
  lenght = len(strParam)

  least = 4
  most = 25

  if least <= lenght <= most:
    return True


def isValidCharacters(strParam):
  if strParam.isalnum() or "_" in strParam:
    return True

def CodelandUsernameValidation(strParam):
  if lenghtIsValid(strParam) and strParam[0].isalpha() and isValidCharacters(strParam) and strParam[len(strParam) - 1] != "_":
    return True
  else:
    return False

# keep this function call here 
print(CodelandUsernameValidation(input()))
