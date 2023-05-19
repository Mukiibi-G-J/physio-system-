from main.models import PhysioSessionAdmission
import random

# def generate_random_code(patient_no):
#     # define the characters to use
#     chars = "0123456789"

#     # keep generating codes until we find one that hasn't been used before
#     while True:
#         # code = ''.join(random.choice(chars) for _ in range(length))
        
#         if not PhysioSessionAdmission.objects.filter(admission_no=admission_no).exists():
#             break

#     return code