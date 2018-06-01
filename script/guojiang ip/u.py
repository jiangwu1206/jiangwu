import win32api, win32con, win32gui 
from ctypes import * 
import os

global host_num
global s_ip



# 
# Device change events (WM_DEVICECHANGE wParam) 
# 
DBT_DEVICEARRIVAL = 0x8000 
DBT_DEVICEQUERYREMOVE = 0x8001 
DBT_DEVICEQUERYREMOVEFAILED = 0x8002 
DBT_DEVICEMOVEPENDING = 0x8003 
DBT_DEVICEREMOVECOMPLETE = 0x8004 
DBT_DEVICETYPESSPECIFIC = 0x8005 
DBT_CONFIGCHANGED = 0x0018 
# 
# type of device in DEV_BROADCAST_HDR 
# 
DBT_DEVTYP_OEM = 0x00000000 
DBT_DEVTYP_DEVNODE = 0x00000001 
DBT_DEVTYP_VOLUME = 0x00000002 
DBT_DEVTYPE_PORT = 0x00000003 
DBT_DEVTYPE_NET = 0x00000004 
# 
# media types in DBT_DEVTYP_VOLUME 
# 
DBTF_MEDIA = 0x0001 
DBTF_NET = 0x0002 
WORD = c_ushort 
DWORD = c_ulong 
class DEV_BROADCAST_HDR (Structure): 
 _fields_ = [ 
   ("dbch_size", DWORD), 
   ("dbch_devicetype", DWORD), 
   ("dbch_reserved", DWORD) 
 ] 
class DEV_BROADCAST_VOLUME (Structure): 
 _fields_ = [ 
   ("dbcv_size", DWORD), 
   ("dbcv_devicetype", DWORD), 
   ("dbcv_reserved", DWORD), 
   ("dbcv_unitmask", DWORD), 
   ("dbcv_flags", WORD) 
 ] 
def drive_from_mask (mask): 
 n_drive = 0 
 while 1: 
   if (mask & (2 ** n_drive)): return n_drive 
   else: n_drive += 1 
class Notification: 
 def __init__(self): 
   message_map = { 
     win32con.WM_DEVICECHANGE : self.onDeviceChange 
   } 
   wc = win32gui.WNDCLASS () 
   hinst = wc.hInstance = win32api.GetModuleHandle (None) 
   wc.lpszClassName = "DeviceChangeDemo" 
   wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW; 
   wc.hCursor = win32gui.LoadCursor (0, win32con.IDC_ARROW) 
   wc.hbrBackground = win32con.COLOR_WINDOW 
   wc.lpfnWndProc = message_map 
   classAtom = win32gui.RegisterClass (wc) 
   style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU 
   self.hwnd = win32gui.CreateWindow ( 
     classAtom, 
     "Device Change Demo", 
     style, 
     0, 0, 
     win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 
     0, 0, 
     hinst, None 
   ) 
 def onDeviceChange (self, hwnd, msg, wparam, lparam): 
   # 
   # WM_DEVICECHANGE: 
   #  wParam - type of change: arrival, removal etc. 
   #  lParam - what's changed? 
   #    if it's a volume then... 
   #  lParam - what's changed more exactly 
   # 
   dev_broadcast_hdr = DEV_BROADCAST_HDR.from_address (lparam) 
   if wparam == DBT_DEVICEARRIVAL: 
     print ("Something's arrived")
     if dev_broadcast_hdr.dbch_devicetype == DBT_DEVTYP_VOLUME: 
       print ("It's a volume!")
       global host_num
       global s_ip
       global s_file
       global n_ip
       if(255 > host_num):
        with open(s_file,"r+") as f:
            
         ip=f.read()
         d_ip=n_ip+str(host_num)+"/16"
         f.seek(0)
         f.write(ip.replace(s_ip,d_ip))
         host_num=host_num+1
         print(d_ip)
         #os.system("pause")
        os.system("dos2unix %s"%(s_file))
        print("请换卡")
        
       dev_broadcast_volume = DEV_BROADCAST_VOLUME.from_address (lparam) 
       if dev_broadcast_volume.dbcv_flags == DBTF_MEDIA: 
         print ("with some media" )
         drive_letter = drive_from_mask (dev_broadcast_volume.dbcv_unitmask) 
         print ("in drive", chr (ord ("A") + drive_letter)) 
		 
   return 1 
if __name__=='__main__':
 global host_num
 global s_ip
 global s_file
 global n_ip
 print("请输入新主机号")
 host_num = input()
 host_num=int(host_num)
 print("请输入新的前三位网络号\n如：10.0.0.")
 n_ip=input()
 print("需要修改的源IP CRID格式\n如：192.168.1.2/16")
 s_ip=input()
 print("请输入IP文件绝对路径\n如:f:/ip")
 s_file=input()
 w = Notification () 
 win32gui.PumpMessages ()