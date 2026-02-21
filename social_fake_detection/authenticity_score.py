import random

def calculate_authenticity(bot_probability, behavioral_consistency):
    """
    Calculates the final authenticity score based on 
    ML model outputs and behavioral signals.
    """
    # Inverse logic: Higher bot probability means lower authenticity
    base_score = 100 - bot_probability
    
    # Weighting the behavioral consistency (0.0 to 1.0)
    final_score = (base_score * 0.7) + (behavioral_consistency * 30)
    
    return round(max(0, min(100, final_score)), 2)

def get_risk_level(score):
    """Categorizes the score for the UI status indicator."""
    if score > 80:
        return "Trusted", "#00ffa3"
    elif score > 50:
        return "Suspicious", "#ffcc00"
    else:
        return "High Risk", "#ff4d4d"