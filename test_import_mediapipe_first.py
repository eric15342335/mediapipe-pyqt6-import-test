"""Test MediaPipe first, then PyQt6 import order."""

import sys
import traceback


def test_imports():
    print("=" * 50)
    print("Testing import order: MediaPipe first, then PyQt6")
    print("=" * 50)

    # Test 1: Import MediaPipe first
    try:
        print("Step 1: Importing MediaPipe...")
        import mediapipe as mp

        print(f"[+] MediaPipe imported successfully!")
        print(f"  MediaPipe version: {mp.__version__}")

        # Test some MediaPipe functionality
        print("  Testing MediaPipe solutions...")
        solutions = mp.solutions
        print(f"    [+] MediaPipe solutions available: {type(solutions)}")

        # Test a specific solution
        hands = solutions.hands
        print(f"    [+] MediaPipe hands solution: {type(hands)}")

    except Exception as e:
        print(f"[x] Failed to import MediaPipe: {e}")
        traceback.print_exc()
        return False

    print()

    # Test 2: Import PyQt6 after MediaPipe
    try:
        print("Step 2: Importing PyQt6...")
        import PyQt6
        from PyQt6.QtCore import PYQT_VERSION_STR, QT_VERSION_STR
        from PyQt6.QtWidgets import QApplication

        print(f"[+] PyQt6 imported successfully!")
        print(f"  Qt version: {QT_VERSION_STR}")
        print(f"  PyQt6 version: {PYQT_VERSION_STR}")

        # Try to create a QApplication to test functionality
        app = QApplication(sys.argv)
        print("  [+] QApplication created successfully")

    except Exception as e:
        print(f"[x] Failed to import PyQt6: {e}")
        traceback.print_exc()
        return False

    print()
    print("=" * 50)
    print("[+] All imports successful! No conflict detected.")
    print("=" * 50)
    return True


if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)
