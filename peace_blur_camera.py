import cv2
import mediapipe as mp

# ----------------------------------------------------------------------
# Inisialisasi MediaPipe Hands
# ----------------------------------------------------------------------
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands_detector = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,          # maksimal 2 tangan terdeteksi
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6,
)

FINGER_TIPS = {
    "thumb": 4,
    "index": 8,
    "middle": 12,
    "ring": 16,
    "pinky": 20,
}
FINGER_PIPS = {
    "thumb": 3,
    "index": 6,
    "middle": 10,
    "ring": 14,
    "pinky": 18,
}


def is_finger_extended(landmarks, finger_name, handedness_label):
    """
    Mengecek apakah suatu jari dalam keadaan lurus/terangkat.
    Untuk jari selain jempol: jari dianggap lurus jika ujung (tip)
    lebih tinggi (nilai y lebih kecil) dibanding titik PIP-nya.
    """
    tip_y = landmarks[FINGER_TIPS[finger_name]].y
    pip_y = landmarks[FINGER_PIPS[finger_name]].y
    return tip_y < pip_y  # y lebih kecil = lebih ke atas di gambar


def is_peace_sign(landmarks, handedness_label):
   
    index_up = is_finger_extended(landmarks, "index", handedness_label)
    middle_up = is_finger_extended(landmarks, "middle", handedness_label)
    ring_down = not is_finger_extended(landmarks, "ring", handedness_label)
    pinky_down = not is_finger_extended(landmarks, "pinky", handedness_label)

    return index_up and middle_up and ring_down and pinky_down


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Tidak bisa mengakses kamera. Pastikan webcam tersedia dan tidak dipakai aplikasi lain.")
        return

    print("Kamera aktif. Tunjukkan gesture ✌️✌️ (dua tangan) untuk mengaktifkan blur.")
    print("Tekan 'q' untuk keluar.")

    while True:
        success, frame = cap.read()
        if not success:
            print("Gagal membaca frame dari kamera.")
            break

        frame = cv2.flip(frame, 1)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands_detector.process(rgb_frame)

        peace_count = 0  # menghitung berapa tangan yang membentuk peace sign

        if results.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                handedness_label = "Unknown"
                if results.multi_handedness:
                    handedness_label = results.multi_handedness[idx].classification[0].label



                if is_peace_sign(hand_landmarks.landmark, handedness_label):
                    peace_count += 1

        is_double_peace = peace_count >= 2

        if is_double_peace:
            frame = cv2.GaussianBlur(frame, (55, 55), 0)
            cv2.putText(
                frame,
                "BLUR AKTIF: Gesture VV (Peace x2) terdeteksi",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2,
            )
        else:
            status_text = f"Tangan dengan peace sign terdeteksi: {peace_count}/2"
            cv2.putText(
                frame,
                status_text,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

        cv2.imshow("Kamera Auto-Blur (Peace Sign x2)", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
