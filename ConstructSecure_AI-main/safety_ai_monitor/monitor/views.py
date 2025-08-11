import os
import base64
import io
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from ultralytics import YOLO
from PIL import Image

# Load YOLO model once at startup
MODEL_PATH = os.path.join(settings.BASE_DIR, 'monitor', 'ml_models', 'best.pt')
model = YOLO(MODEL_PATH)

def index(request):
    return render(request, 'monitor/index.html')

def detection_view(request):
    return render(request, 'monitor/detection.html')

def about(request):
    return render(request, 'monitor/about.html')


def detect_frame(request):
    """
    Receives base64 webcam frame from frontend and runs YOLO detection
    """
    if request.method == 'POST':
        try:
            import json
            body = json.loads(request.body)
            image_data = body.get('image_data')

            if not image_data:
                return JsonResponse({'success': False, 'error': 'No image data provided'}, status=400)

            # Decode base64 image
            image_data = image_data.split(",")[1]  # remove 'data:image/jpeg;base64,'
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))

            # Save temporarily
            temp_path = os.path.join(settings.MEDIA_ROOT, 'temp_frame.jpg')
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            image.save(temp_path)

            # Run YOLO prediction
            results = model(temp_path)

            # Extract detection results
            detections = []
            for box in results[0].boxes:
                cls_id = int(box.cls[0])
                cls_name = model.names[cls_id]
                conf = float(box.conf[0])
                detections.append({
                    'class': cls_name,
                    'confidence': round(conf, 3)
                })

            # Decide success/failure based on your PPE classes
            required_classes = {'helmet', 'vest'}  # example PPE items
            detected_classes = {d['class'] for d in detections}
            success = required_classes.issubset(detected_classes)

            return JsonResponse({
                'success': success,
                'detections': detections
            })

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)
