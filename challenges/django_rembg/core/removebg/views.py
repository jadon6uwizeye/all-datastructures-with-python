# from django.shortcuts import render
# from rembg import remove
# from PIL import Image
# from django.http import HttpResponse
# import os

# # Create your views here.

# def remove_image(request):
#     print(request.body)
#     try:
#         input_path = os.path.join(os.path.dirname(__file__), 'images/image_1.png')
#         output_path = os.path.join(os.path.dirname(__file__), 'images/image_2.png')

#         input = Image.open(input_path)
#         output = remove(input)
#         output.save(output_path)
#         return HttpResponse("done")
#     except Exception as e:
#         print(e)
#         return HttpResponse(e)


from io import BytesIO

from PIL import Image

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import rembg

@csrf_exempt
def remove_background(request):
    try:
        print(request)
        if request.method == 'POST':
            print("inside here")
            image_file = request.FILES.get('image')  # 'image' should be the name of the file input field in the HTML form
            img = Image.open(image_file)
            print("image opened")
            output = rembg.remove(img)
            print("image removed")
            response = HttpResponse(content_type='image/png')
            output.save(response, 'PNG')
            response['Content-Disposition'] = 'attachment; filename="output.png"'
            print(response)
            return response
        else:
            print("here")
            return HttpResponse("Unsupported method")
    except Exception as e:
        print("error : ",e)
        return HttpResponse(e)