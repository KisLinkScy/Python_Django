from django.shortcuts import render
# from .models import User

def myprofile(request):      #, pipol_id
    return render(request, 'main/myprofile.html')
# def myprofile(request, pipol_id):
#     pipol = get_object_or_404(User, pk=pipol_id)
#     data = {
#         'id': pipol.id,
#         'image': pipol.image,
#         'familiya': pipol.last_name,
#         'name': pipol.first_name,
#         'otchestvo': pipol.otchestvo,
#         'telefone': pipol.telefone,
#         'email': pipol.email,
#         'nomer_kvartir': pipol.nomer_kvartir,
#         'birthday': pipol.birthday,
        
#     }     #Piople.objects.all()
#     return render(request, 'main/myprofile.html', data)
#