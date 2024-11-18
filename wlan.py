import speedtest
import socket
import requests
import subprocess

def get_ip_info():
    # Define the command to display the private IP addresses for a specific network interface
    command = "ip addr show | grep 192.168"

    # Execute the command and capture the output
    private_ip = subprocess.check_output(command, shell=True)

    loopback_address = socket.gethostbyname(socket.gethostname())
    public_ip = requests.get('https://api.ipify.org').text
    return private_ip, loopback_address, public_ip

def get_internet_service_provider():
    response = requests.get('https://ipinfo.io')
    return response.json().get('org')

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1e9  # Convert to Gbps
    upload_speed = st.upload() / 1e9      # Convert to Gbps
    return download_speed, upload_speed
def main():
    private_ip, loopback_address, public_ip = get_ip_info()
    isp = get_internet_service_provider()
    download_speed, upload_speed = test_speed()
    print(f"Loopback Address: {loopback_address}")
    print(f"Public IP Address: {public_ip}")
    print(f"Private IP Address: {private_ip.decode()}")
    print(f"Internet Service Provider: {isp}")
    print(f"Download Speed: {download_speed:.2f} Gbps")
    print(f"Upload Speed: {upload_speed:.2f} Gbps")


if __name__ == "__main__":
    main()
