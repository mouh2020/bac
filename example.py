from bac.bac import Bac

student = Bac(matricule="12345678",
              code="123")

## Return student informations
result = student.condidate_result_json()
print(result['الاسم'])
print(result['اللقب'])
print(result['المعدل'])
print(result['الملاحظة'])
print(result['الشعبة'])
print(result['رقم التسجيل'])
## Return if the student succeed or not (True if succeed)
succeed = student.check_condidate_success()
## Return if the student succeed or not (True if succeed)
