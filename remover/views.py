from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from PIL import Image
import numpy as np
from io import BytesIO
from rembg import remove

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def remove_bg(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']

        # Read image into numpy array
        img = Image.open(image_file).convert("RGBA")
        input_np = np.array(img)

        # Remove background
        output_np = remove(input_np)

        # Convert back to PIL Image
        output_img = Image.fromarray(output_np)

        # Save to memory buffer
        buffer = BytesIO()
        output_img.save(buffer, format='PNG')
        buffer.seek(0)

        # Save to storage
        filename = default_storage.save('processed_' + image_file.name.replace(".jpg", ".png").replace(".jpeg", ".png"), ContentFile(buffer.read()))
        result_url = default_storage.url(filename)

        return JsonResponse({
            'result_url': result_url,
            'download_url': result_url
        })

    return JsonResponse({'error': 'No file uploaded'}, status=400)
