import scapy.all as scapy
import optparse

def get_ipaddress():
    parse = optparse.OptionParser()
    parse.add_option("-i", "--ipaddress", dest="ipaddress", help="IP address for you want scanning.")
    (options, arguments) = parse.parse_args()
    if not options.ipaddress:
        parse.error("Please specify an ip address")
    else:
        return options


def start_scan():
  options = get_ipaddress()

  arp_request_packet = scapy.ARP(pdst=options.ipaddress)
  broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

  combined_packet = broadcast_packet/arp_request_packet
  (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1, verbose=False)
  answered_list.summary()

if __name__ == "__main__":
    start_scan()
