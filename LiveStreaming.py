import cv2
import easyocr

vid = cv2.VideoCapture(1)

reader = easyocr.Reader(['en'], gpu=False)

interval = 2

while True:
    ret, frame = vid.read()

    cv2.imshow("frame", frame)

    # Perform OCR on the frame
    results = reader.readtext(frame)

    for detection in results:

        bbox = detection[0]
        text = detection[1]

        x_min, y_min = [int(val) for val in bbox[0]]
        x_max, y_max = [int(val) for val in bbox[2]]

        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)


        cv2.putText(frame, text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
