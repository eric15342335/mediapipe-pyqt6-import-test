"""Test MediaPipe only in isolation."""

import sys
import traceback


def test_mediapipe_only():
    print("=" * 50)
    print("MediaPipe Standalone Test")
    print("=" * 50)

    try:
        print("Step 1: Importing MediaPipe...")
        import mediapipe as mp

        print(f"[+] MediaPipe imported successfully!")
        print(f"  MediaPipe version: {mp.__version__}")

        print("\nStep 2: Testing MediaPipe solutions...")
        solutions = mp.solutions
        print(f"[+] MediaPipe solutions loaded: {type(solutions)}")

        print("\nStep 3: Testing specific solutions...")
        # Test hands solution
        hands = solutions.hands
        print(f"[+] Hands solution: {type(hands)}")

        # Test pose solution
        pose = solutions.pose
        print(f"[+] Pose solution: {type(pose)}")

        # Test face detection solution
        face_detection = solutions.face_detection
        print(f"[+] Face detection solution: {type(face_detection)}")

        print("\nStep 4: Testing MediaPipe drawing utilities...")
        drawing = solutions.drawing_utils
        print(f"[+] Drawing utilities: {type(drawing)}")

        print("\nStep 5: Testing MediaPipe hands initialization...")
        # Try to create a hands detector (this often reveals deeper issues)
        hands_detector = hands.Hands(
            static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5
        )
        print("[+] Hands detector created successfully!")

        print("\nStep 6: Testing MediaPipe pose initialization...")
        pose_detector = pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
        print("[+] Pose detector created successfully!")

        print("\n" + "=" * 50)
        print("[+] MediaPipe standalone test PASSED!")
        print("[+] All MediaPipe functionality working correctly")
        print("=" * 50)

        return True

    except Exception as e:
        print(f"\n[x] MediaPipe standalone test FAILED: {e}")
        print("\nFull traceback:")
        traceback.print_exc()

        print("\n" + "=" * 50)
        print("[x] MediaPipe standalone test FAILED!")
        print("=" * 50)

        return False


if __name__ == "__main__":
    success = test_mediapipe_only()
    sys.exit(0 if success else 1)
