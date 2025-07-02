# MediaPipe PyQt6 Import Conflict Test

This repository contains a GitHub Actions workflow designed to reproduce and test potential import conflicts between MediaPipe and PyQt6 on Windows systems.

## Purpose

The goal is to identify and reproduce import conflicts that occur when using MediaPipe and PyQt6 together, particularly when importing PyQt6 first and then MediaPipe.

## How It Works

The GitHub Actions workflow automatically:

1. Tests on Windows 2022 and Windows 2025 with Python 3.8-3.12
2. Installs PyQt6 first, then MediaPipe
3. Runs multiple test scenarios to reproduce the conflict
4. Provides detailed error logs and system information

## Test Scripts

- `test_import_conflict.py` - Tests PyQt6 first, then MediaPipe (main conflict scenario)
- `test_import_mediapipe_first.py` - Tests MediaPipe first, then PyQt6
- `test_pyqt6_only.py` - Tests PyQt6 in complete isolation
- `test_mediapipe_only.py` - Tests MediaPipe in complete isolation
