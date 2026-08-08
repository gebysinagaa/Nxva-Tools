#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ███╗   ██╗██╗  ██╗██╗   ██╗ █████╗                  ║
║   ████╗  ██║╚██╗██╔╝██║   ██║██╔══██╗                 ║
║   ██╔██╗ ██║ ╚███╔╝ ██║   ██║███████║                 ║
║   ██║╚██╗██║ ██╔██╗ ╚██╗ ██╔╝██╔══██║                 ║
║   ██║ ╚████║██╔╝ ██╗ ╚████╔╝ ██║  ██║                 ║
║   ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝                 ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

Author : Arszlnxva
Version: 1.0
Github : https://github.com/gebysinagaa/nxva-v1
"""

import os
import sys
import time
import subprocess
import platform
from datetime import datetime
import json
import shutil

# ============================================
# KONFIGURASI WARNA
# ============================================

class Colors:
    """Warna untuk tampilan di Termux"""
    # Warna dasar
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Warna terang
    LIGHT_RED = '\033[91;1m'
    LIGHT_GREEN = '\033[92;1m'
    LIGHT_YELLOW = '\033[93;1m'
    LIGHT_BLUE = '\033[94;1m'
    LIGHT_MAGENTA = '\033[95;1m'
    LIGHT_CYAN = '\033[96;1m'
    LIGHT_WHITE = '\033[97;1m'
    
    # Gaya
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Background
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    END = '\033[0m'

# ============================================
# FUNGSI UTILITY
# ============================================

def clear_screen():
    """Bersihkan layar terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation(text="Loading", duration=2):
    """Animasi loading sederhana"""
    chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{Colors.CYAN}{chars[i % len(chars)]}{Colors.END} {text}...')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * 50 + '\r')

def print_banner():
    """Tampilkan banner NXVA"""
    clear_screen()
    banner = f"""
{Colors.LIGHT_CYAN}╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   {Colors.LIGHT_BLUE}███╗   ██╗██╗  ██╗██╗   ██╗ █████╗ {Colors.LIGHT_CYAN}                 ║
║   {Colors.LIGHT_BLUE}████╗  ██║╚██╗██╔╝██║   ██║██╔══██╗{Colors.LIGHT_CYAN}                 ║
║   {Colors.LIGHT_BLUE}██╔██╗ ██║ ╚███╔╝ ██║   ██║███████║{Colors.LIGHT_CYAN}                 ║
║   {Colors.LIGHT_BLUE}██║╚██╗██║ ██╔██╗ ╚██╗ ██╔╝██╔══██║{Colors.LIGHT_CYAN}                 ║
║   {Colors.LIGHT_BLUE}██║ ╚████║██╔╝ ██╗ ╚████╔╝ ██║  ██║{Colors.LIGHT_CYAN}                 ║
║   {Colors.LIGHT_BLUE}╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝{Colors.LIGHT_CYAN}                 ║
║                                                          ║
║        {Colors.LIGHT_YELLOW}🚀 NXVA v1{Colors.LIGHT_CYAN}                                ║
║        {Colors.LIGHT_WHITE}Termux Tools Premium{Colors.LIGHT_CYAN}                      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝{Colors.END}

{Colors.LIGHT_GREEN}    Author{Colors.END} : {Colors.WHITE}Nama Kamu{Colors.END}
{Colors.LIGHT_GREEN}    Version{Colors.END} : {Colors.WHITE}1.0{Colors.END}
{Colors.LIGHT_GREEN}    Github{Colors.END}  : {Colors.WHITE}https://github.com/username/nxva-v1{Colors.END}
{Colors.LIGHT_GREEN}    Time{Colors.END}   : {Colors.WHITE}{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}{Colors.END}

{Colors.LIGHT_CYAN}┌──────────────────────────────────────────────────────┐
│ {Colors.BOLD}MENU UTAMA NXVA{Colors.END}{Colors.LIGHT_CYAN}                         │
├──────────────────────────────────────────────────────┤
│ {Colors.LIGHT_GREEN}1.{Colors.END} 📱 Info Sistem NXVA                 │
│ {Colors.LIGHT_GREEN}2.{Colors.END} 🌐 Cek Koneksi Internet             │
│ {Colors.LIGHT_GREEN}3.{Colors.END} 📊 Speed Test Network               │
│ {Colors.LIGHT_GREEN}4.{Colors.END} 🔍 Scan Port Lokal                  │
│ {Colors.LIGHT_GREEN}5.{Colors.END} 💾 Info Storage & Memory            │
│ {Colors.LIGHT_GREEN}6.{Colors.END} 🧹 Bersihkan Cache & Sampah         │
│ {Colors.LIGHT_GREEN}7.{Colors.END} 🔄 Update NXVA Tools               │
│ {Colors.LIGHT_GREEN}8.{Colors.END} ⚙️  Custom Command                  │
│ {Colors.LIGHT_GREEN}9.{Colors.END} 🛡️  Security Check                 │
│ {Colors.LIGHT_GREEN}10.{Colors.END}📦 Install Packages                │
│ {Colors.LIGHT_GREEN}0.{Colors.END} {Colors.LIGHT_RED}Keluar NXVA{Colors.END}                     │
├──────────────────────────────────────────────────────┤
│ {Colors.LIGHT_YELLOW}Pilih menu (0-10):{Colors.END}                     │
└──────────────────────────────────────────────────────┘
    """
    print(banner)

def get_input(prompt):
    """Ambil input user dengan handling error"""
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print(f"\n{Colors.LIGHT_RED}❌ Dibatalkan oleh user!{Colors.END}")
        return None
    except Exception as e:
        print(f"\n{Colors.LIGHT_RED}❌ Error: {e}{Colors.END}")
        return None

# ============================================
# FITUR-FITUR NXVA
# ============================================

def nxva_info_sistem():
    """Fitur 1: Info Sistem"""
    loading_animation("Mengambil info sistem", 1)
    
    print(f"\n{Colors.LIGHT_CYAN}╔══════════════════════════════════════╗")
    print(f"║     📱 INFO SISTEM NXVA            ║")
    print(f"╚══════════════════════════════════════╝{Colors.END}\n")
    
    # Info dasar
    print(f"{Colors.LIGHT_GREEN}  • {Colors.END}User          : {Colors.WHITE}{os.getlogin()}{Colors.END}")
    print(f"{Colors.LIGHT_GREEN}  • {Colors.END}Device        : {Colors.WHITE}{platform.node()}{Colors.END}")
    print(f"{Colors.LIGHT_GREEN}  • {Colors.END}OS            : {Colors.WHITE}{platform.system()} {platform.release()}{Colors.END}")
    print(f"{Colors.LIGHT_GREEN}  • {Colors.END}Architecture  : {Colors.WHITE}{platform.machine()}{Colors.END}")
    print(f"{Colors.LIGHT_GREEN}  • {Colors.END}Processor     : {Colors.WHITE}{platform.processor() or 'Unknown'}{Colors.END}")
    print(f"{Colors.LIGHT_GREEN}  • {Colors.END}Python        : {Colors.WHITE}{sys.version.split()[0]}{Colors.END}")
    print(f"{Colors.LIGHT_GREEN}  • {Colors.END}Terminal      : {Colors.WHITE}{os.environ.get('TERM', 'Unknown')}{Colors.END}")
    
    # Waktu
    now = datetime.now()
    print(f"{Colors.LIGHT_GREEN}  • {Colors.END}Tanggal       : {Colors.WHITE}{now.strftime('%A, %d %B %Y')}{Colors.END}")
    print(f"{Colors.LIGHT_GREEN}  • {Colors.END}Waktu         : {Colors.WHITE}{now.strftime('%H:%M:%S')}{Colors.END}")
    
    # Info uptime
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.read().split()[0])
            days = int(uptime_seconds // 86400)
            hours = int((uptime_seconds % 86400) // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            print(f"{Colors.LIGHT_GREEN}  • {Colors.END}Uptime        : {Colors.WHITE}{days}d {hours}h {minutes}m{Colors.END}")
    except:
        pass
    
    print(f"\n{Colors.LIGHT_CYAN}────────────────────────────────────────{Colors.END}")
    input(f"\n{Colors.LIGHT_YELLOW}Press Enter untuk kembali...{Colors.END}")

def nxva_cek_internet():
    """Fitur 2: Cek Koneksi"""
    loading_animation("Testing koneksi", 1)
    
    print(f"\n{Colors.LIGHT_CYAN}╔══════════════════════════════════════╗")
    print(f"║     🌐 CEK KONEKSI INTERNET        ║")
    print(f"╚══════════════════════════════════════╝{Colors.END}\n")
    
    sites = [
        ('Google', 'google.com'),
        ('GitHub', 'github.com'),
        ('Cloudflare', 'cloudflare.com'),
        ('YouTube', 'youtube.com'),
        ('WhatsApp', 'wa.me')
    ]
    
    for name, site in sites:
        try:
            result = subprocess.run(
                ['ping', '-c', '1', '-W', '2', site],
                capture_output=True,
                text=True,
                timeout=3
            )
            if result.returncode == 0:
                # Ambil waktu ping
                if 'time=' in result.stdout:
                    time_ms = result.stdout.split('time=')[-1].split(' ')[0]
                    print(f"  {Colors.LIGHT_GREEN}✅{Colors.END} {name:12} : {Colors.WHITE}Online ({time_ms}ms){Colors.END}")
                else:
                    print(f"  {Colors.LIGHT_GREEN}✅{Colors.END} {name:12} : {Colors.WHITE}Online{Colors.END}")
            else:
                print(f"  {Colors.LIGHT_RED}❌{Colors.END} {name:12} : {Colors.LIGHT_RED}Offline{Colors.END}")
        except subprocess.TimeoutExpired:
            print(f"  {Colors.LIGHT_RED}❌{Colors.END} {name:12} : {Colors.LIGHT_RED}Timeout{Colors.END}")
        except:
            print(f"  {Colors.LIGHT_RED}❌{Colors.END} {name:12} : {Colors.LIGHT_RED}Error{Colors.END}")
    
    print(f"\n{Colors.LIGHT_CYAN}────────────────────────────────────────{Colors.END}")
    input(f"\n{Colors.LIGHT_YELLOW}Press Enter untuk kembali...{Colors.END}")

def nxva_speed_test():
    """Fitur 3: Speed Test"""
    loading_animation("Running speed test", 2)
    
    print(f"\n{Colors.LIGHT_CYAN}╔══════════════════════════════════════╗")
    print(f"║     📊 SPEED TEST NETWORK           ║")
    print(f"╚══════════════════════════════════════╝{Colors.END}\n")
    
    print(f"{Colors.LIGHT_YELLOW}  Testing ping ke Google (4x)...{Colors.END}\n")
    
    try:
        result = subprocess.run(
            ['ping', '-c', '4', 'google.com'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            lines = result.stdout.split('\n')
            for line in lines:
                if 'avg' in line or 'rtt' in line:
                    # Parse hasil ping
                    parts = line.split('/')
                    if len(parts) >= 5:
                        min_ms = parts[3].strip()
                        avg_ms = parts[4].strip()
                        max_ms = parts[5].strip()
                        mdev_ms = parts[6].split()[0] if len(parts) > 6 else '0'
                        
                        print(f"{Colors.LIGHT_GREEN}  📊 Hasil Speed Test:{Colors.END}")
                        print(f"  {Colors.WHITE}┌─────────────────────────┐{Colors.END}")
                        print(f"  │ {Colors.LIGHT_GREEN}Minimum{Colors.END}  : {Colors.WHITE}{min_ms} ms{Colors.END}")
                        print(f"  │ {Colors.LIGHT_GREEN}Rata-rata{Colors.END} : {Colors.WHITE}{avg_ms} ms{Colors.END}")
                        print(f"  │ {Colors.LIGHT_GREEN}Maksimum{Colors.END} : {Colors.WHITE}{max_ms} ms{Colors.END}")
                        print(f"  │ {Colors.LIGHT_GREEN}Deviasi{Colors.END}  : {Colors.WHITE}{mdev_ms} ms{Colors.END}")
                        print(f"  {Colors.WHITE}└─────────────────────────┘{Colors.END}")
                    break
        else:
            print(f"  {Colors.LIGHT_RED}❌ Gagal melakukan speed test{Colors.END}")
    except subprocess.TimeoutExpired:
        print(f"  {Colors.LIGHT_RED}❌ Timeout!{Colors.END}")
    except Exception as e:
        print(f"  {Colors.LIGHT_RED}❌ Error: {e}{Colors.END}")
    
    print(f"\n{Colors.LIGHT_CYAN}────────────────────────────────────────{Colors.END}")
    input(f"\n{Colors.LIGHT_YELLOW}Press Enter untuk kembali...{Colors.END}")

def nxva_scan_port():
    """Fitur 4: Scan Port"""
    print(f"\n{Colors.LIGHT_CYAN}╔══════════════════════════════════════╗")
    print(f"║     🔍 SCAN PORT LOKAL             ║")
    print(f"╚══════════════════════════════════════╝{Colors.END}\n")
    
    print(f"{Colors.LIGHT_YELLOW}  Port yang umum digunakan:{Colors.END}")
    print(f"  {Colors.WHITE}22  - SSH")
    print(f"  80  - HTTP")
    print(f"  443 - HTTPS")
    print(f"  8080 - HTTP Alternate")
    print(f"  3306 - MySQL")
    print(f"  5432 - PostgreSQL{Colors.END}\n")
    
    port = input(f"{Colors.LIGHT_CYAN}  Masukkan port yang mau di-scan: {Colors.END}")
    if not port:
        return
    
    try:
        loading_animation(f"Scanning port {port}", 1)
        result = subprocess.run(
            ['netstat', '-tulpn'],
            capture_output=True,
            text=True
        )
        
        if port in result.stdout:
            # Cari detail port
            lines = result.stdout.split('\n')
            for line in lines:
                if port in line and 'LISTEN' in line:
                    print(f"\n  {Colors.LIGHT_GREEN}✅ Port {port} terbuka!{Colors.END}")
                    print(f"  {Colors.WHITE}Detail:{Colors.END}")
                    print(f"  {Colors.WHITE}{line.strip()}{Colors.END}")
                    break
            else:
                print(f"\n  {Colors.LIGHT_GREEN}✅ Port {port} terbuka{Colors.END}")
        else:
            print(f"\n  {Colors.LIGHT_YELLOW}⚠️ Port {port} tidak aktif{Colors.END}")
    except Exception as e:
        print(f"\n  {Colors.LIGHT_RED}❌ Error: {e}{Colors.END}")
    
    print(f"\n{Colors.LIGHT_CYAN}────────────────────────────────────────{Colors.END}")
    input(f"\n{Colors.LIGHT_YELLOW}Press Enter untuk kembali...{Colors.END}")

def nxva_info_storage():
    """Fitur 5: Info Storage & Memory"""
    loading_animation("Mengambil info storage", 1)
    
    print(f"\n{Colors.LIGHT_CYAN}╔══════════════════════════════════════╗")
    print(f"║     💾 INFO STORAGE & MEMORY       ║")
    print(f"╚══════════════════════════════════════╝{Colors.END}\n")
    
    # Storage info
    print(f"{Colors.LIGHT_GREEN}  📁 STORAGE:{Colors.END}")
    try:
        # Coba /sdcard dulu
        result = subprocess.run(['df', '-h', '/sdcard'], capture_output=True, text=True)
        lines = result.stdout.split('\n')
        for line in lines:
            if '/sdcard' in line:
                parts = line.split()
                if len(parts) >= 6:
                    print(f"    {Colors.WHITE}Total     : {parts[1]}{Colors.END}")
                    print(f"    {Colors.WHITE}Used      : {parts[2]}{Colors.END}")
                    print(f"    {Colors.WHITE}Available : {parts[3]}{Colors.END}")
                    print(f"    {Colors.WHITE}Used %    : {parts[4]}{Colors.END}")
                break
    except:
        # Fallback ke root
        try:
            result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            for line in lines[1:3]:
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 6:
                        print(f"    {Colors.WHITE}Total     : {parts[1]}{Colors.END}")
                        print(f"    {Colors.WHITE}Used      : {parts[2]}{Colors.END}")
                        print(f"    {Colors.WHITE}Available : {parts[3]}{Colors.END}")
                        print(f"    {Colors.WHITE}Used %    : {parts[4]}{Colors.END}")
                    break
        except:
            print(f"    {Colors.LIGHT_RED}❌ Gagal mengambil info storage{Colors.END}")
    
    # Memory info
    print(f"\n{Colors.LIGHT_GREEN}  🧠 MEMORY:{Colors.END}")
    try:
        result = subprocess.run(['free', '-h'], capture_output=True, text=True)
        lines = result.stdout.split('\n')
        for line in lines:
            if 'Mem:' in line:
                parts = line.split()
                if len(parts) >= 4:
                    print(f"    {Colors.WHITE}Total     : {parts[1]}{Colors.END}")
                    print(f"    {Colors.WHITE}Used      : {parts[2]}{Colors.END}")
                    print(f"    {Colors.WHITE}Available : {parts[3]}{Colors.END}")
                break
    except:
        print(f"    {Colors.LIGHT_RED}❌ Gagal mengambil info memory{Colors.END}")
    
    print(f"\n{Colors.LIGHT_CYAN}────────────────────────────────────────{Colors.END}")
    input(f"\n{Colors.LIGHT_YELLOW}Press Enter untuk kembali...{Colors.END}")

def nxva_bersihkan():
    """Fitur 6: Bersihkan Cache"""
    print(f"\n{Colors.LIGHT_CYAN}╔══════════════════════════════════════╗")
    print(f"║     🧹 BERSIHKAN CACHE & SAMPAH    ║")
    print(f"╚══════════════════════════════════════╝{Colors.END}\n")
    
    print(f"{Colors.LIGHT_YELLOW}  ⚠️ Peringatan: Ini akan menghapus cache Termux{Colors.END}")
    confirm = input(f"{Colors.LIGHT_RED}  Yakin? (y/n): {Colors.END}")
    
    if confirm.lower() != 'y':
        print(f"  {Colors.LIGHT_YELLOW}❌ Dibatalkan{Colors.END}")
        input(f"\n{Colors.LIGHT_YELLOW}Press Enter untuk kembali...{Colors.END}")
        return
    
    print(f"\n  {Colors.LIGHT_CYAN}Membersihkan cache...{Colors.END}")
    try:
        # Hapus cache Termux
        cache_dir = '/data/data/com.termux/cache'
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
            os.makedirs(cache_dir)
            print(f"  {Colors.LIGHT_GREEN}✅ Cache Termux dibersihkan{Colors.END}")
        else:
            print(f"  {Colors.LIGHT_YELLOW}⚠️ Cache directory tidak ditemukan{Colors.END}")
        
        # Hapus file .tmp
        home = os.path.expanduser('~')
        for root, dirs, files in os.walk(home):
            for file in files:
                if file.endswith('.tmp') or file.endswith('.log'):
                    try:
                        os.remove(os.path.join(root, file))
                    except:
                        pass
        
        print(f"  {Colors.LIGHT_GREEN}✅ File temporary dibersihkan{Colors.END}")
    except Exception as e:
        print(f"  {Colors.LIGHT_RED}❌ Error: {e}{Colors.END}")
    
    print(f"\n{Colors.LIGHT_CYAN}────────────────────────────────────────{Colors.END}")
    input(f"\n{Colors.LIGHT_YELLOW}Press Enter untuk kembali...{Colors.END}")

def nxva_update():
    """Fitur 7: Update Tools"""
    loading_animation("Checking updates", 1)
    
    print(f"\n{Colors.LIGHT_CYAN}╔══════════════════════════════════════╗")
    print(f"║     🔄 UPDATE NXVA TOOLS           ║")
    print(f"╚══════════════════════════════════════╝{Colors.END}\n")
    
    print(f"{Colors.LIGHT_YELLOW}  Menjalankan update packages...{Colors.END}\n")
    
    try:
        # Update pkg
        print(f"  {Colors.LIGHT_CYAN}1. Update package list...{Colors.END}")
        result = subprocess.run(['pkg', 'update', '-y'], capture_output=True, text=True)
        print(f"  {Colors.LIGHT_GREEN}✅ Selesai{Colors.END}")
        
        print(f"\n  {Colors.LIGHT_CYAN}2. Upgrade packages...{Colors.END}")
        result = subprocess.run(['pkg', 'upgrade', '-y'], capture_output=True, text=True)
        print(f"  {Colors.LIGHT_GREEN}✅ Selesai{Colors.END}")
        
        print(f"\n  {Colors.LIGHT_GREEN}✅ NXVA Tools telah diupdate!{Colors.END}")
    except Exception as e:
        print(f"\n  {Colors.LIGHT_RED}❌ Error: {e}{Colors.END}")
    
    print(f"\n{Colors.LIGHT_CYAN}────────────────────────────────────────{Colors.END}")
    input(f"\n{Colors.LIGHT_YELLOW}Press Enter untuk kembali...{Colors.END}")

def nxva_custom():
    """Fitur 8: Custom Command"""
    print(f"\n{Colors.LIGHT_CYAN}╔══════════════════════════════════════╗")
    print(f"║     ⚙️ CUSTOM COMMAND              ║")
    print(f"╚══════════════════════════════════════╝{Colors.END}\n")
    
    print(f"{Colors.LIGHT_YELLOW}  Contoh command:{Colors.END}")
    print(f"  {Colors.WHITE}• ping google.com")
    print(f"  • whoami")
    print(f"  • pwd")
    print(f"  • ls -la")
    print(f"  • python --version")
    print(f"  • neofetch (install dulu){Colors.END}\n")
    
    cmd = input(f"{Colors.LIGHT_CYAN}  Masukkan command: {Colors.END}")
    if not cmd:
        return
    
    print(f"\n{Colors.LIGHT_YELLOW}  ── Menjalankan: {cmd}{Colors.END}")
    print(f"{Colors.LIGHT_CYAN}────────────────────────────────────────{Colors.END}\n")
    
    try:
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(timeout=30)
        
        if stdout:
            print(stdout)
        if stderr:
            print(f"{Colors.LIGHT_RED}{stderr}{Colors.END}")
        
        if process.returncode != 0:
            print(f"\n{Colors.LIGHT_YELLOW}⚠️ Exit code: {process.returncode}{Colors.END}")
    except subprocess.TimeoutExpired:
        process.kill()
        print(f"{Colors.LIGHT_RED}❌ Timeout (30 detik){Colors.END}")
    except Exception as e:
        print(f"{Colors.LIGHT_RED}❌ Error: {e}{Colors.END}")
    
    print(f"\n{Colors.LIGHT_CYAN}────────────────────────────────────────{Colors.END}")
    input(f"\n{Colors.LIGHT_YELLOW}Press Enter untuk kembali...{Colors.END}")

def nxva_security():
    """Fitur 9: Security Check"""
    loading_animation("Running security check", 2)
    
    print(f"\n{Colors.LIGHT_CYAN}╔══════════════════════════════════════╗")
    print(f"║     🛡️ SECURITY CHECK               ║")
    print(f"╚══════════════════════════════════════╝{Colors.END}\n")
    
    issues = []
    
    # Cek root
    try:
        result = subprocess.run(['id'], capture_output=True, text=True)
        if 'uid=0' in result.stdout:
            issues.append(f"{Colors.LIGHT_RED}⚠️ Running as ROOT! Berbahaya!{Colors.END}")
        else:
            print(f"  {Colors.LIGHT_GREEN}✅ Running as normal user{Colors.END}")
    except:
        pass
    
    # Cek permission /data
    try:
        result = subprocess.run(['ls', '-la', '/data'], capture_output=True, text=True)
        if 'drwxrwx--x' in result.stdout or 'drwxrwxr-x' in result.stdout:
            print(f"  {Colors.LIGHT_GREEN}✅ Data permission aman{Colors.END}")
        else:
            issues.append(f"{Colors.LIGHT_YELLOW}⚠️ Data permission tidak standar{Colors.END}")
    except:
        pass
    
    # Cek package yang sudah diinstall
    try:
        result = subprocess.run(['pkg', 'list-installed'], capture_output=True, text=True)
        packages = result.stdout.count('\n')
        print(f"  {Colors.LIGHT_GREEN}✅ {packages} packages terinstall{Colors.END}")
    except:
        pass
    
    # Cek storage
    try:
        result = subprocess.run(['df', '-h', '/data'], capture_output=True, text=True)
        lines = result.stdout.split('\n')
        for line in lines:
            if '/data' in line:
                parts = line.split()
                if len(parts) >= 5:
                    used_percent = parts[4].replace('%', '')
                    if int(used_percent) > 90:
                        issues.append(f"{Colors.LIGHT_YELLOW}⚠️ Storage hampir penuh ({used_percent}%){Colors.END}")
                    else:
                        print(f"  {Colors.LIGHT_GREEN}✅ Storage usage: {used_percent}%{Colors.END}")
                break
    except:
        pass
    
    print(f"\n{Colors.LIGHT_CYAN}────────────────────────────────────────{Colors.END}")
    
    if issues:
        print(f"\n{Colors.LIGHT_YELLOW}📋 Issues ditemukan:{Colors.END}")
        for issue in issues:
            print(f"  {issue}")
    else:
        print(f"\n{Colors.LIGHT_GREEN}✅ Sistem aman!{Colors.END}")
    
    input(f"\n{Colors.LIGHT_YELLOW}Press Enter untuk kembali...{Colors.END}")

def nxva_install():
    """Fitur 10: Install Packages"""
    print(f"\n{Colors.LIGHT_CYAN}╔══════════════════════════════════════╗")
    print(f"║     📦 INSTALL PACKAGES             ║")
    print(f"╚══════════════════════════════════════╝{Colors.END}\n")
    
    print(f"{Colors.LIGHT_YELLOW}  Package yang tersedia:{Colors.END}")
    print(f"  {Colors.WHITE}1.  python       - Python 3")
    print(f"  2.  git          - Version control")
    print(f"  3.  nodejs       - Node.js")
    print(f"  4.  php          - PHP")
    print(f"  5.  mysql        - MySQL server")
    print(f"  6.  nginx        - Web server")
    print(f"  7.  vim          - Text editor")
    print(f"  8.  neofetch     - System info")
    print(f"  9.  htop         - Process viewer")
    print(f"  10. nmap         - Network scanner{Colors.END}")
    print(f"  {Colors.LIGHT_YELLOW}11. Custom package{Colors.END}\n")
    
    choice = input(f"{Colors.LIGHT_CYAN}  Pilih package (1-11): {Colors.END}")
    
    packages = {
        '1': 'python',
        '2': 'git',
        '3': 'nodejs',
        '4': 'php',
        '5': 'mysql',
        '6': 'nginx',
        '7': 'vim',
        '8': 'neofetch',
        '9': 'htop',
        '10': 'nmap'
    }
    
    if choice in packages:
        pkg = packages[choice]
        print(f"\n  {Colors.LIGHT_CYAN}Installing {pkg}...{Colors.END}")
        try:
            result = subprocess.run(['pkg', 'install', pkg, '-y'], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"  {Colors.LIGHT_GREEN}✅ {pkg} berhasil diinstall!{Colors.END}")
            else:
                print(f"  {Colors.LIGHT_RED}❌ Gagal install {pkg}{Colors.END}")
        except Exception as e:
            print(f"  {Colors.LIGHT_RED}❌ Error: {e}{Colors.END}")
    elif choice == '11':
        custom = input(f"  Masukkan nama package: {Colors.END}")
        if custom:
            print(f"\n  {Colors.LIGHT_CYAN}Installing {custom}...{Colors.END}")
            try:
                result = subprocess.run(['pkg', 'install', custom, '-y'], capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"  {Colors.LIGHT_GREEN}✅ {custom} berhasil diinstall!{Colors.END}")
                else:
                    print(f"  {Colors.LIGHT_RED}❌ Gagal install {custom}{Colors.END}")
            except Exception as e:
                print(f"  {Colors.LIGHT_RED}❌ Error: {e}{Colors.END}")
    else:
        print(f"  {Colors.LIGHT_RED}❌ Pilihan tidak valid{Colors.END}")
    
    print(f"\n{Colors.LIGHT_CYAN}────────────────────────────────────────{Colors.END}")
    input(f"\n{Colors.LIGHT_YELLOW}Press Enter untuk kembali...{Colors.END}")

def nxva_exit():
    """Keluar dari NXVA"""
    print(f"\n{Colors.LIGHT_CYAN}╔══════════════════════════════════════╗")
    print(f"║     👋 TERIMA KASIH!               ║")
    print(f"╚══════════════════════════════════════╝{Colors.END}\n")
    print(f"{Colors.LIGHT_YELLOW}  Sampai jumpa! Jangan lupa star repo ini! ⭐{Colors.END}")
    print(f"{Colors.LIGHT_CYAN}  https://github.com/username/nxva-v1{Colors.END}\n")
    sys.exit(0)

# ============================================
# MAIN PROGRAM
# ============================================

def main():
    """Main program NXVA v1"""
    while True:
        print_banner()
        choice = get_input(f"{Colors.LIGHT_YELLOW}└─> {Colors.END}")
        
        if choice == '0':
            nxva_exit()
        elif choice == '1':
            nxva_info_sistem()
        elif choice == '2':
            nxva_cek_internet()
        elif choice == '3':
            nxva_speed_test()
        elif choice == '4':
            nxva_scan_port()
        elif choice == '5':
            nxva_info_storage()
        elif choice == '6':
            nxva_bersihkan()
        elif choice == '7':
            nxva_update()
        elif choice == '8':
            nxva_custom()
        elif choice == '9':
            nxva_security()
        elif choice == '10':
            nxva_install()
        else:
            print(f"\n{Colors.LIGHT_RED}❌ Pilihan tidak valid! Silakan pilih 0-10{Colors.END}")
            time.sleep(1.5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.LIGHT_YELLOW}👋 Sampai jumpa!{Colors.END}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.LIGHT_RED}❌ Error: {e}{Colors.END}")
        sys.exit(1)
