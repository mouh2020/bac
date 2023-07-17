# dz_bac_bot
A script to get student's informations from bac.onec.dz without passing captcha.

**How to use:**
- Clonse the repository.
- Install libraries by entering in shell :
```bash
  pip install -r requirements 
```
- Basic example : 
```bash
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
## Return if the student succeed or not (True if succed)
succeed = student.check_condidate_success()
print(succeed)

```
