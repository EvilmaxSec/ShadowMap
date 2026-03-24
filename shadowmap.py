#!/usr/bin/env python3
import requests
import json
import os
import sys
import time
import shutil
from datetime import datetime
from colorama import init, Fore, Style, Back

# Initialize colorama for colored output
init(autoreset=True)

# Color constants
class Colors:
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    MAGENTA = Fore.MAGENTA
    RESET = Style.RESET_ALL

class ShadowMap:
    def __init__(self):
        self.ip = None
        self.data = {}
        self.results_dir = "results"
        self.author = "EvilmaxSec"
        self.terminal_width = self.get_terminal_width()
        
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
    
    def get_terminal_width(self):
        """Get terminal width for responsive display"""
        try:
            width = shutil.get_terminal_size().columns
            return min(width, 80)  
        except:
            return 60  
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_banner(self):
        """Display matrix-style banner without borders"""
        banner = f"""
{Colors.GREEN} ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗███╗   ███╗ █████╗ ██████╗ 
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║████╗ ████║██╔══██╗██╔══██╗
 ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║██╔████╔██║███████║██████╔╝
 ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
 ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚═╝ ██║██║  ██║██║     
 ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
{Colors.RESET}
{Colors.RED}═══════════════════════════════════════════════════════════════════════════════{Colors.RESET}
{Colors.YELLOW}           ADVANCED IP GEOLOCATION INTELLIGENCE | SECURITY RESEARCH{Colors.RESET}
{Colors.CYAN}═══════════════════════════════════════════════════════════════════════════════{Colors.RESET}
{Colors.WHITE}  🚀 Author: {Colors.GREEN}EvilmaxSec{Colors.WHITE} | Cyber Ninja{Colors.WHITE}
{Colors.WHITE}  🔗 GitHub: {Colors.BLUE}https://github.com/EvilmaxSec/ShadowMap{Colors.WHITE}
{Colors.WHITE}  ⚠️  DISCLAIMER: {Colors.RED}For Educational & Authorized Testing Only{Colors.WHITE}
{Colors.CYAN}═══════════════════════════════════════════════════════════════════════════════{Colors.RESET}
"""
        print(banner)
    
    def get_ip(self):
        """Get IP address from user"""
        while True:
            print(f"\n{Colors.GREEN}[{Colors.RED}▶{Colors.GREEN}] {Colors.YELLOW}Enter target IP:{Colors.RESET} ", end="")
            self.ip = input().strip()
            
            
            parts = self.ip.split('.')
            if len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
                return True
            else:
                print(f"\n{Colors.RED}[!] Invalid IP format. Example: 8.8.8.8{Colors.RESET}")
                time.sleep(1)
    
    def fetch_location(self):
        """Fetch geolocation data from multiple APIs for accuracy"""
        print(f"\n{Colors.YELLOW}[*] Tracking IP: {self.ip}{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Querying intelligence databases...{Colors.RESET}")
        
       
        apis = [
            f'http://ip-api.com/json/{self.ip}?fields=status,country,countryCode,region,regionName,city,lat,lon,zip,timezone,isp,org,as,mobile,proxy,hosting',
            f'https://ipapi.co/{self.ip}/json/',
            f'http://ipwho.is/{self.ip}'
        ]
        
        for api_url in apis:
            try:
                response = requests.get(api_url, timeout=10)
                data = response.json()
                
                
                if 'status' in data and data.get('status') == 'success':                   
                    self.data = {
                        'ip': self.ip,
                        'country': data.get('country', 'N/A'),
                        'country_code': data.get('countryCode', 'N/A'),
                        'region': data.get('regionName', 'N/A'),
                        'city': data.get('city', 'N/A'),
                        'latitude': data.get('lat', 'N/A'),
                        'longitude': data.get('lon', 'N/A'),
                        'postal': data.get('zip', 'N/A'),
                        'timezone': data.get('timezone', 'N/A'),
                        'isp': data.get('isp', 'N/A'),
                        'org': data.get('org', 'N/A'),
                        'asn': data.get('as', 'N/A'),
                        'mobile': data.get('mobile', False),
                        'proxy': data.get('proxy', False),
                        'hosting': data.get('hosting', False)
                    }
                    print(f"{Colors.GREEN}[✓] Location acquired successfully!{Colors.RESET}")
                    return True
                    
                elif 'country' in data and data.get('country_name'):                    
                    self.data = {
                        'ip': self.ip,
                        'country': data.get('country_name', 'N/A'),
                        'country_code': data.get('country_code', 'N/A'),
                        'region': data.get('region', 'N/A'),
                        'city': data.get('city', 'N/A'),
                        'latitude': data.get('latitude', 'N/A'),
                        'longitude': data.get('longitude', 'N/A'),
                        'postal': data.get('postal', 'N/A'),
                        'timezone': data.get('timezone', 'N/A'),
                        'isp': data.get('org', 'N/A'),
                        'org': data.get('org', 'N/A'),
                        'asn': data.get('asn', 'N/A'),
                        'mobile': data.get('mobile', False),
                        'proxy': data.get('proxy', False),
                        'hosting': data.get('hosting', False)
                    }
                    print(f"{Colors.GREEN}[✓] Location acquired successfully!{Colors.RESET}")
                    return True
                    
                elif 'success' in data and data.get('success'):                   
                    self.data = {
                        'ip': self.ip,
                        'country': data.get('country', 'N/A'),
                        'country_code': data.get('country_code', 'N/A'),
                        'region': data.get('region', 'N/A'),
                        'city': data.get('city', 'N/A'),
                        'latitude': data.get('latitude', 'N/A'),
                        'longitude': data.get('longitude', 'N/A'),
                        'postal': data.get('postal', 'N/A'),
                        'timezone': data.get('timezone', {}).get('id', 'N/A'),
                        'isp': data.get('connection', {}).get('isp', 'N/A'),
                        'org': data.get('connection', {}).get('org', 'N/A'),
                        'asn': data.get('connection', {}).get('asn', 'N/A'),
                        'mobile': False,
                        'proxy': data.get('security', {}).get('proxy', False),
                        'hosting': data.get('connection', {}).get('type') == 'hosting'
                    }
                    print(f"{Colors.GREEN}[✓] Location acquired successfully!{Colors.RESET}")
                    return True
                    
            except requests.exceptions.RequestException:
                continue
            except Exception:
                continue
        
        print(f"{Colors.RED}[✗] Failed to fetch location data{Colors.RESET}")
        return False
    
    def generate_google_maps_url(self):
        """Generate Google Maps URL for coordinates"""
        lat = self.data.get('latitude')
        lon = self.data.get('longitude')
        
        if lat != 'N/A' and lon != 'N/A':
            return f"https://www.google.com/maps?q={lat},{lon}"
        return None
    
    def print_output(self):
        """Display formatted results without borders for small terminals"""
        print(f"\n{Colors.CYAN}═══════════ IP GEOLOCATION REPORT ═══════════{Colors.RESET}")
        
        print(f"\n{Colors.GREEN}[+] TARGET IP: {Colors.WHITE}{self.data.get('ip', 'N/A')}{Colors.RESET}")
        
        print(f"\n{Colors.YELLOW}📍 LOCATION INFORMATION{Colors.RESET}")
        print(f"   Country   : {self.data.get('country', 'N/A')} ({self.data.get('country_code', 'N/A')})")
        print(f"   Region    : {self.data.get('region', 'N/A')}")
        print(f"   City      : {self.data.get('city', 'N/A')}")
        print(f"   Coord     : {self.data.get('latitude', 'N/A')}, {self.data.get('longitude', 'N/A')}")
        print(f"   Postal    : {self.data.get('postal', 'N/A')}")
        print(f"   Timezone  : {self.data.get('timezone', 'N/A')}")
        
        print(f"\n{Colors.BLUE}🌐 NETWORK INFORMATION{Colors.RESET}")
        print(f"   ISP       : {self.data.get('isp', 'N/A')}")
        print(f"   Org       : {self.data.get('org', 'N/A')}")
        print(f"   ASN       : {self.data.get('asn', 'N/A')}")
        
        # Additional flags
        flags = []
        if self.data.get('mobile'):
            flags.append("📱 Mobile")
        if self.data.get('proxy'):
            flags.append("🕵️ Proxy")
        if self.data.get('hosting'):
            flags.append("☁️ Hosting")
        
        if flags:
            print(f"\n{Colors.MAGENTA}⚡ ADDITIONAL INFO{Colors.RESET}")
            print(f"   {', '.join(flags)}")
        
        # Google Maps Link
        maps_url = self.generate_google_maps_url()
        if maps_url:
            print(f"\n{Colors.GREEN}🗺️  GOOGLE MAPS{Colors.RESET}")
            print(f"   {maps_url}")
            print(f"   {Colors.YELLOW}[Copy URL to view exact location]{Colors.RESET}")
        
        print(f"\n{Colors.CYAN}═══════════════════════════════════════════{Colors.RESET}")
    
    def save_output(self):
        """Save results to text file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.results_dir}/{self.ip}_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("═" * 50 + "\n")
                f.write("SHADOWMAP - IP GEOLOCATION REPORT\n")
                f.write(f"Author: EvilmaxSec | GitHub: https://github.com/EvilmaxSec\n")
                f.write("═" * 50 + "\n\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Target IP: {self.data.get('ip', 'N/A')}\n\n")
                
                f.write("📍 LOCATION INFORMATION\n")
                f.write("-" * 30 + "\n")
                f.write(f"Country:      {self.data.get('country', 'N/A')} ({self.data.get('country_code', 'N/A')})\n")
                f.write(f"Region:       {self.data.get('region', 'N/A')}\n")
                f.write(f"City:         {self.data.get('city', 'N/A')}\n")
                f.write(f"Coordinates:  {self.data.get('latitude', 'N/A')}, {self.data.get('longitude', 'N/A')}\n")
                f.write(f"Postal Code:  {self.data.get('postal', 'N/A')}\n")
                f.write(f"Timezone:     {self.data.get('timezone', 'N/A')}\n\n")
                
                f.write("🌐 NETWORK INFORMATION\n")
                f.write("-" * 30 + "\n")
                f.write(f"ISP:          {self.data.get('isp', 'N/A')}\n")
                f.write(f"Organization: {self.data.get('org', 'N/A')}\n")
                f.write(f"ASN:          {self.data.get('asn', 'N/A')}\n\n")
                
                # Google Maps Link
                maps_url = self.generate_google_maps_url()
                if maps_url:
                    f.write("🗺️ GOOGLE MAPS LOCATION\n")
                    f.write("-" * 30 + "\n")
                    f.write(f"URL: {maps_url}\n\n")
                
                f.write("═" * 50 + "\n")
                f.write("DISCLAIMER: For educational & authorized testing only\n")
                f.write("Report generated by ShadowMap - EvilmaxSec\n")
            
            print(f"\n{Colors.GREEN}[✓] Saved: {filename}{Colors.RESET}")
            return filename
            
        except Exception as e:
            print(f"\n{Colors.RED}[✗] Save failed: {e}{Colors.RESET}")
            return None
    
    def ask_continue(self):
        """Ask user if they want to track another IP"""
        while True:
            print(f"\n{Colors.GREEN}[?] Track another IP? (y/n): {Colors.RESET}", end="")
            choice = input().strip().lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print(f"{Colors.RED}[!] Enter 'y' or 'n'{Colors.RESET}")
    
    def run(self):
        """Main execution loop"""
        while True:
            self.clear_screen()
            self.print_banner()
            
            # Get IP from user
            self.get_ip()
            
            # Fetch location data
            if self.fetch_location():
                # Print to console
                self.print_output()
                
                # Save to file
                self.save_output()
                
                
                if not self.ask_continue():
                    print(f"\n{Colors.GREEN}[+] Thanks for using ShadowMap!{Colors.RESET}")
                    print(f"{Colors.CYAN}[+] Stay stealthy - EvilmaxSec | Cyber Ninja{Colors.RESET}\n")
                    time.sleep(1)
                    break
            else:
                print(f"\n{Colors.YELLOW}[!] Press Enter to retry...{Colors.RESET}", end="")
                input()

def main():
    """Entry point"""
    try:
        tool = ShadowMap()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}[!] Interrupted{Colors.RESET}")
        print(f"{Colors.CYAN}[+] Stay stealthy - EvilmaxSec | Cyber Ninja{Colors.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}[!] Error: {e}{Colors.RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()