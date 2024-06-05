from MacScanner import MacScanner

scanner: MacScanner
previous_macs = set()

def setup():
    endpoint = 'https://your/endpoint/url'
    ip_range = '192.168.66.0/24'
    global scanner
    scanner = MacScanner(endpoint, ip_range)


def loop():
    global previous_macs
    scan_output = scanner.scan()
    
    if scan_output == 0:
        current_macs = set(scanner.get_mac_addresses())  # Assuming get_mac_addresses() returns a list of MAC addresses
        changes_detected = False
        
        new_macs = current_macs - previous_macs
        lost_macs = previous_macs - current_macs
        
        if new_macs or lost_macs:
            changes_detected = True
            
        previous_macs = current_macs
        
        if changes_detected:
            upload_output = scanner.upload()
            if upload_output == 0:
                print(scanner.upload_result)
            else:
                print("[ERROR] Upload failed!")
        else:
            print("No changes in MAC addresses. Skipping upload.")
    else:
        print("[ERROR] Scan failed!")
    
    wait(10000)


def wait(ms):
    import time
    print("Waiting for {} ms".format(ms))
    time.sleep(ms / 1000)


def main():
    setup()
    while True:
        loop()


main()
