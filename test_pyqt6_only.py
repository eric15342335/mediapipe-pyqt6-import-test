"""Test PyQt6 only in isolation."""

import sys
import traceback


def test_pyqt6_only():
    print("=" * 50)
    print("PyQt6 Standalone Test")
    print("=" * 50)

    try:
        print("Step 1: Importing PyQt6 core modules...")
        import PyQt6
        from PyQt6.QtCore import PYQT_VERSION_STR, QT_VERSION_STR

        print(f"[+] PyQt6 core imported successfully!")
        print(f"  Qt version: {QT_VERSION_STR}")
        print(f"  PyQt6 version: {PYQT_VERSION_STR}")

        print("\nStep 2: Importing PyQt6 widgets...")
        from PyQt6.QtWidgets import QApplication, QLabel, QWidget

        print("[+] PyQt6 widgets imported successfully!")

        print("\nStep 3: Creating QApplication...")
        app = QApplication(sys.argv)
        print("[+] QApplication created successfully!")

        print("\nStep 4: Creating a simple widget...")
        widget = QWidget()
        label = QLabel("PyQt6 Test Widget")
        print("[+] Simple widgets created successfully!")

        print("\nStep 5: Testing Qt functionality...")
        # Test some basic Qt functionality
        widget.setWindowTitle("PyQt6 Test")
        widget.resize(200, 100)
        print("[+] Qt functionality test passed!")

        print("\n" + "=" * 50)
        print("[+] PyQt6 standalone test PASSED!")
        print("[+] All PyQt6 functionality working correctly")
        print("=" * 50)

        return True

    except Exception as e:
        print(f"\n[x] PyQt6 standalone test FAILED: {e}")
        print("\nFull traceback:")
        traceback.print_exc()

        print("\n" + "=" * 50)
        print("[x] PyQt6 standalone test FAILED!")
        print("=" * 50)

        return False


if __name__ == "__main__":
    success = test_pyqt6_only()
    sys.exit(0 if success else 1)
