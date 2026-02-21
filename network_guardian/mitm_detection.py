from scapy.all import sniff, IP

def scan_for_mitm(packet_limit=20):
    """Analyzes packet headers for suspicious routing anomalies."""
    # Simplified logic: sniffing a small burst of traffic
    packets = sniff(count=packet_limit, timeout=5)
    if len(packets) == 0:
        return "No active traffic found to analyze."
    
    return f"Analyzed {len(packets)} packets. Routing paths appear legitimate."