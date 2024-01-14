import os
import cv2
from matplotlib import pyplot as plt
from ultralytics import YOLO


def show_img_bbox(img, coords, show_img=True):
    x, y, w, z = coords[0], coords[1], coords[2], coords[3]
    img = cv2.rectangle(img, (int(x), int(y)),
                        (int(w), int(z)), (255, 0, 0), 2)
    if not show_img:
        return img
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


def load_model():
    # return YOLO("yolov8l.pt")
    return YOLO("yolov8s.pt")


def analyse_results(img, result):
    boxs = result.boxes
    for box in boxs:
        obj = result.names[box.cls[0].item()]
        coords = box.xyxy[0].tolist()
        prob = box.conf[0].item()

        print("Object type:", obj)
        print("Coordinates:", coords)
        print("Probability:", prob)

        img = show_img_bbox(img, coords, False)

    return img


def main():
    filename = input('file path:')
    try:
        img = cv2.imread(filename)
    except Exception as e:
        print(f'Error reading file -> {e}')
        raise e

    model = load_model()
    results = model.predict(filename)
    img = analyse_results(img,results[0])
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print(os.getcwd())
    main()
