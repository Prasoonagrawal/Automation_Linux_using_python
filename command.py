import os
while(True):
	print("\n\nLinux Commands")
	print()
	print("press 1 For Service 'systemctl'")
	print("Press 2 For install any software")
	print("Press 3 TO see IP of any site")
	print("Press 4 TO Set up hadoop namenode ")
	print("Press 5 TO Set up hadoop datanode ")
	print("Press 6 TO RAM,CPU,Storage related query")
	print("Press 7 To see packet details")
	print("Press 8 For SSH and SCP services")
	print("Press 9 For Docker")
	print("Press 10 To set up web server")
	print("Press 11 for partition")
	print("Press 12 for LVM partition")
	a=input("Want you want: ")
	if(int(a)==1):
		print("\n\nService")
		print()
		print("Press 1 to see all daemon")
		print("Press 2 to to see all unit")
		print("Press 3 to see status of any unit")
		print("Press 4 to to see all runnng socket")
		print("Press 5 to see any service status")
		print("Press 6 to start any service")
		print("Press 7 to stop any service")
		print("Press 8 to start any service permanent")
		print("Press 9 to stop any service permanent")
		print("Press 10 to see service is active or not")
		print("Press 11 to see service is enable or not")
		print("Press 12 to see service is disable or not")
		print()
		n=input("Enter Number:  ")
		if(int(n)==1):
			os.system("systemctl")
		elif(int(n)==2):
			os.system("systemctl -l")
		elif(int(n)==3):
			c=input("Enter unit name: ")
			os.system("systemctl status "+c)
		elif(int(n)==4):
			os.system("systemctl -t socket")
		elif(int(n)==5):
			c=input("Enter service name: ")
			os.system("systemctl status "+c)
		elif(int(n)==6):
			c=input("Enter service name: ")
			os.system("systemctl start "+c)
		elif(int(n)==7):
			c=input("Enter service name: ")
			os.system("systemctl stop "+c)
		elif(int(n)==8):
			c=input("Enter service name: ")
			os.system("systemctl enable"+c)
		elif(int(n)==9):
			c=input("Enter service name: ")
			os.system("systemctl disable "+c)
		elif(int(n)==10):
			c=input("Enter service name: ")
			os.system("systemctl is-active "+c)
		elif(int(n)==11):
			c=input("Enter service name: ")
			os.system("systemctl is-enable "+c)
		elif(int(n)==12):
			c=input("Enter service name: ")
			os.system("systemctl is-disable "+c)


	elif(int(a)==2):
		print("\n\nFor install any software")
		print()
		print("Press 1 to know how to install any software" 'watprovides')
		print("Press 2 to install software using yum")
		print("Press 3 to remove software using yum")
		print("Press 4 to install software using yum")
		print("Press 5 to remove software using yum")
		print("Press 6 to install software using rpm")


		n=input("Enter Number:  ")
		if(int(n)==1):
			c=input("Enter software name")
			os.system("yum whatprovides "+c)		
		elif(int(n)==1):
			c=input("Enter software name")
			os.system("yum install "+c)
		elif(int(n)==2):
			c=input("Enter software name")
			os.system("yum remove "+c)
		elif(int(n)==3):
			c=input("Enter unit name: ")
			os.system("systemctl status "+c)
		elif(int(n)==4):
			c=input("Enter software name")
			os.system("dnf install "+c)
		elif(int(n)==5):
			c=input("Enter unit name: ")
			os.system("dnf remove "+c)
		elif(int(n)==6):
			c=input("Enter unit name: ")
			os.system("rpm -ivh  "+c)
	elif(int(a)==3):
		z=input("Enter website name for which you wnant to know IP: ")
		os.system("nslookup "+z)
	elif(int(a)==4):
			
		print()
		print("You are in namenode")
		print("press 1: to run jps command")
		print("press 2: to check your ip")
		print("press 3: to start namenode")
		print("press 4: to delete namenode")
		print("press 5: to create namenode")
		print("press 6: to check total datanode connected")
		print("press 7: to stop name node")
		print("press 8: to check uploaded file")
		print("press 9: to upload empty file in cluster")
		print("press 10: to format namenode")
		print("press 11: to stop safe mode in namenode")
		print("press 12: to upload file which you already have")
		print("press 13: to delete any file")


		c=input()
		if(int(c)==1):
			os.system("jps")

		if(int(c)==2):
			os.system("ifconfig")
		if(int(c)==3):
			os.system("hadoop-daemon.sh start namenode")
		if(int(c)==4):
			os.system("rm -r /nn")
		if(int(c)==5):
			os.system("mkdir /nn")
		if(int(c)==6):
			os.system("hadoop dfsadmin -report")
		if(int(c)==7):
			os.system("hadoop-daemon.sh start namenode")

		if(int(c)==8):
			os.system("hadoop fs -ls /")
		if(int(c)==9):
			z=input("Enter file name")
			print(type(z),z)
			os.system("hadoop fs -touchz /"+z)

		if(int(c)==10):
			os.system("hadoop namenode -format")

		if(int(c)==11):
			os.system("hadoop dfsadmin -safemode leave")
		if(int(c)==12):
			x=input("Enter file name")
			os.system("hadoop fs -put "+x+"/")

		if(int(c)==13):
			x=input("Enter file name")
			os.system("hadoop fs -rmr /"+x)


		
	elif(int(a)==5):
			
		print("press 1: to run jps command")
		print("press 2: to check your ip")
		print("press 3: to start datanode")
		print("press 4: to delete datanode")
		print("press 5: to stop datanode")
		print("press 6: to check uploaded file")
		print("press 7: to format namenode")

		print()


		c=input()
		if(int(c)==1):
			os.system("jps")

		if(int(c)==2):
			os.system("ifconfig")
		if(int(c)==3):
			os.system("hadoop-daemon.sh start datanode")
		if(int(c)==4):
			os.system("rm -r /dn")
		if(int(c)==5):
			os.system("hadoop-daemon.sh stop datanode")
		if(int(c)==6):
			os.system("hadoop fs -ls /")
		if(int(c)==7):
			os.system("hadoop datanode -format")

		

	elif(int(a)==6):
		print("press 1: to check RAM detial")
		print("press 2: to clean RAM or Caches")
		print("press 3: to all partition")
		print("press 4: to see CPU detial")
		print("press 5: to see all process with their state")
		print()


		c=input("What you want: ")
		if(int(c)==1):
			os.system("free -lh")
		elif(int(c)==2):
			os.system("echo 3 > /proc/sys/vm/drop_caches")	
		elif(int(c)==3):
			os.system("lsblk")
		elif(int(c)==4):
			os.system("lscpu")
		elif(int(c)==5):
			os.system("top")
		
	elif(int(a)==7):
		print("press 1: to check all packet detial")
		print("press 2: to check all packet detial in Hexadecimal")
		print("press 3: to store all packet detial in file")
		print("press 4: To convert file that contain packet detail in human read form")
		print()


		c=input("What you want: ")
		if(int(c)==1):
			os.system("tcpdump -i enp0s3 -n")
		elif(int(c)==2):
			os.system("tcpdump -i enp0s3 -n -X")	
		elif(int(c)==3):
			z=input("Enter file name")
			os.system("mkdir "+z)
			os.system("tcpdump -i enp0s3 -n -w "+z)	
		elif(int(c)==4):
			z=input("Enter file name in which we have packet data")	
			v=input("Enter file name in which you want to store file data in readble form")		
			os.system("tcpdump -n -r z > v")
		

		
	elif(int(a)==8):
		print("press 1: to check SSH status ")
		print("press 2: to connect throug SSH protocol")
		print("press 3: to transfer data through SCP protocol")
		print("press 4: to run any python file in host system")
		print("press 5: to run any command in host system")
		
		print()


		c=input("What you want: ")
		if(int(c)==1):
			os.system("systemctl status sshd")
		if(int(c)==2):
			z=input("Enter IP")
			u=input("User name")
			os.system("ssh "+u+"@"+z)
		elif(int(c)==3):
			f=input("Enter file name")
			z=input("Enter IP")
			p=input("Enter path where you want to copy data")
			os.system("scp "+f+" " +z+":"+p)
		elif(int(c)==4):
			f=input("Enter file name with path e.g. /root/file.py")
			z=input("Enter IP")
			os.system("ssh "+z+" python " +f)	
		elif(int(c)==5):
			z=input("Enter IP")
			u=input("User name")
			p=input("Enter command")
			os.system("ssh "+u+"@"+z+" "+p)
		
	elif(int(a)==9):
		print("press 1: to install docker ce edition")
		print("press 2: to start docker service")
		print("press 3: to download OS image")
		print("press 4: to run docker image")
		print("press 5: to check all running OS image")
		print("press 6: to stop any running OS")
		print("press 7: to start any pause OS  ")
		print("press 8: to see all docker images presesnt  ")
		print("press 9: to see all OS i.e. running,shutdown  ")
		print("press 10: to see delete any OS forcefully ")
		print("press 11: to see delete any image forcefully ")
		print("press 12: to connect to OS which is running ")
		print()


		c=input("What you want: ")
		if(int(c)==1):
			os.system("yum install docker-ce --nobest")
		if(int(c)==2):
			os.system("systemctl start docker")
		elif(int(c)==3):
			f=input("Enter image name with version e.g 'ubuntu:20.10'")
			os.system("docker pull "+f)
		elif(int(c)==4):
			f=input("Enter image name with version e.g 'ubuntu:20.10'")
			n=input("Enter OS name")		
			os.system("docker run -it --name "+n+" "+f)
		elif(int(c)==5):
			os.system("docker ps")
		elif(int(c)==6):
			f=input("Enter OS name")
			os.system("docker stop "+f)
		elif(int(c)==7):
			f=input("Enter OS name")
			os.system("docker start "+f)
		elif(int(c)==8):
			os.system("docker images")
		elif(int(c)==9):
			os.system("docker ps -a")
		elif(int(c)==10):
			n=input("Enter OS name")
			os.system("docker rm -f "+n)
		elif(int(c)==11):
			n=input("Enter image name")
			os.system("docker rmi "+n)
		elif(int(c)==12):
			n=input("Enter ID")
			os.system("docker attach "+n)

		
	elif(int(a)==10):
		print("press 1: to install httpd software")
		print("press 2: to start httpd service")
		print("press 3: to stop web server")
		print()


		c=input("What you want: ")
		if(int(c)==1):
			os.system("dnf install httpd")
		if(int(c)==2):
			os.system("systemctl start httpd")
		elif(int(c)==3):
			os.system("systemctl stop firewalld")

		
	elif(int(a)==11):
		print("press 1: to create partition")
		print("press 2: to all drive size")
		print("press 3: to format partiton")
		print("press 4: to mount partiton")
		print("press 5: to umount partiton")
		print()


		c=input("What you want: ")
		if(int(c)==1):
			p=input("Enter disk name where you want ot create partition e.g. /dev/sdb")
			os.system("fdisk "+p)
		if(int(c)==2):
			os.system("fdisk -l")
		elif(int(c)==3):
			p=input("Enter disk name whcih you want to format e.g. /dev/sdb")
			os.system("mkfs.ext4 "+p)
		elif(int(c)==4):
			p=input("Enter disk name whcih you want to mount e.g. /dev/sdb")
			f=input("Enter folder name where you want to mount")
			os.system("mount "+p+" "+f)
		elif(int(c)==5):
			p=input("Enter floder name which you want to umount")
			os.system("umount "+p)

	elif(int(a)==12):
		print("press 1: to create physical volume")
		print("press 2: to create volume group")
		print("press 3: to see volume group detail detial")
		print("press 4: to create logical volume(LV)")
		print("press 5: to see lv detail")
		print("press 6: to format lv")
		print("press 7: to mount lv")
		print("press 8: to extend LV")	
		print("press 9: to format new disk")
		print("press 10: to extend vg")

		print()


		c=input("What you want: ")
		if(int(c)==1):
			p=input("Enter disk name e.g. /dev/sdb")
			os.system("pvcreate "+p)
		if(int(c)==2):
			p=input("Enter Volume group name")
			z=input("Enter PV namd space sperated e.g. /dev/sdb /dev/sdc")
			os.system("vgcreate "+p+" "+z)
		elif(int(c)==3):
			p=input("Enter dvg nane")
			os.system("vgdisplay "+p)
		elif(int(c)==4):
			p=input("Enter lv nane")
			s=input("Enter size")
			v=input("Enter vg name")
			os.system("lvcreate --size +"+s+" --name "+p+" "+v)
		elif(int(c)==5):
			p=input("Enter vg name")
			l=input("Enter lg name")
			os.system("lvcdisplay "+p+"/"+l)

		elif(int(c)==6):
			p=input("Enter vg name")
			l=input("Enter lg name")
			os.system("mkfs.ext4 /dev/"+p+"/"+l)
		elif(int(c)==7):
			p=input("Enter vg name")
			l=input("Enter lg name")
			f=input("Enter floder name")
			os.system("mount /dev/"+p+"/"+l+" "+f)
		elif(int(c)==8):
			p=input("Enter lv nane")
			s=input("Enter size")
			v=input("Enter vg name")
			os.system("lvcextend --size "+s+" /dev/"+v+"/"+p)
		elif(int(c)==9):
			p=input("Enter vg name")
			l=input("Enter lg name")
			os.system("resize2fs /dev/"+p+"/"+l)
		elif(int(c)==10):
			v=input("Enter vg name")
			p=input("Enter pv name")
			os.system("vgextend "+v+" "+p)
	elif(int(a)==13):
		break
	
