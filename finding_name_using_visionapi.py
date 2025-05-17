from google.cloud import vision

def detect_top_celebrity_name(image_path):
    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.web_detection(image=image)

    web_detection = response.web_detection

    if web_detection.web_entities:
        top_entity = web_detection.web_entities[0]
        print(f"Most likely person: {top_entity.description} (Score: {top_entity.score:.2f})")
    else:
        print("No known person recognized.")

# Replace this with the path to your image
detect_top_celebrity_name("/Users/suryadeepsinhjadeja/Desktop/Tom Cruise.webp")
