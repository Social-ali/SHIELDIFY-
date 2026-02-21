def classify_video(analysis_results):
    """
    Returns the final authenticity score and risk label.
    """
    if not analysis_results:
        return 0, "No Input", "#888"
    
    # Simple weighted average for simulation
    score = (analysis_results["landmarks_consistency"] + analysis_results["texture_score"]) / 2
    
    if score > 90:
        return round(score, 1), "Authentic", "#00ffa3"
    elif score > 70:
        return round(score, 1), "Suspicious", "#ffcc00"
    else:
        return round(score, 1), "Deepfake Detected", "#ff4d4d"