import argparse
import os
import sys

# Add the parent directory of CyberMegaTool to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules import scanner, osint, exploits, password_ai

def main():
    parser = argparse.ArgumentParser(description="CyberMegaTool - The Ultimate Ethical Hacking Toolkit")
    parser.add_argument("-s", "--scan", help="AI-Powered Vulnerability Scan on a target URL", type=str)
    parser.add_argument("-o", "--osint", help="Perform OSINT reconnaissance on a domain", type=str)
    parser.add_argument("-e", "--exploit", help="Find exploitable vulnerabilities on a website", type=str)
    parser.add_argument("-p", "--password", help="Analyze password strength using AI", type=str)
    parser.add_argument("-r", "--report", help="Generate PDF report from results", action="store_true")

    args = parser.parse_args()

    if args.scan:
        scanner.scan_target(args.scan)
    elif args.osint:
        osint.gather_info(args.osint)
    elif args.exploit:
        exploits.find_exploits(args.exploit)
    elif args.password:
        password_ai.analyze_password(args.password)
    elif args.report:
        print("🔹 Generating PDF report... (Feature coming soon!)")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()