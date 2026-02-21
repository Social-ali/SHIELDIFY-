# video_deepfake/__init__.py

from .face_analysis import analyze_face_artifacts
from .video_classifier import classify_video

__all__ = ['analyze_face_artifacts', 'classify_video']