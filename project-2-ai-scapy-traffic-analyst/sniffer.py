from scapy.all import sniff
import time

packets_buffer = []

def capture_packet(pkt):
    try:
        if pkt.haslayer("IP"):
            packets_buffer.append(pkt)
    except:
        pass

def start_sniffing(duration=10):
    global packets_buffer
    packets_buffer = []

    sniff(iface="lo", prn=capture_packet, timeout=duration)

    return packets_buffer
