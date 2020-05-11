#! /usr/bin/python3 
import os
banner = '''
 ██████╗ ███████╗██████╗  █████╗ ██████╗  █████╗ ██╗   ██╗
██╔════╝ ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
██║  ███╗█████╗  ██████╔╝███████║██████╔╝███████║ ╚████╔╝ 
██║   ██║██╔══╝  ██╔══██╗██╔══██║██╔═══╝ ██╔══██║  ╚██╔╝  
╚██████╔╝███████╗██║  ██║██║  ██║██║     ██║  ██║   ██║   
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝  
 #######################################
 #(no-ip)dns dinamico                  #
 #site do (no-ip)http://www.noip.com/  #
 #######################################
 #(duckdns)dns dinamico                #
 #site do (duckdns)www.duckdns.org     #
 #######################################
 #criador darkcode/rootcode            #
 #######################################
 #versao 1  12/1/2017                  #
 #######################################
  '''
banner_install_duck = '''
██████╗ ██╗   ██╗ ██████╗██╗  ██╗██████╗ ███╗   ██╗███████╗
██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔══██╗████╗  ██║██╔════╝
██║  ██║██║   ██║██║     █████╔╝ ██║  ██║██╔██╗ ██║███████╗
██║  ██║██║   ██║██║     ██╔═██╗ ██║  ██║██║╚██╗██║╚════██║
██████╔╝╚██████╔╝╚██████╗██║  ██╗██████╔╝██║ ╚████║███████║
╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                           
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗          
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║          
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║          
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║          
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗     
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝ 
'''
banner_install_noip = '''
███╗   ██╗ ██████╗       ██╗██████╗                   
████╗  ██║██╔═══██╗      ██║██╔══██╗                  
██╔██╗ ██║██║   ██║█████╗██║██████╔╝                  
██║╚██╗██║██║   ██║╚════╝██║██╔═══╝                   
██║ ╚████║╚██████╔╝      ██║██║                       
╚═╝  ╚═══╝ ╚═════╝       ╚═╝╚═╝                       
                                                      
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
'''
print(banner)
print("como o senhor(a) vai hoje !!")
tempo = os.system("sleep 2")
inicio = int(input("você já tem algum serviço de dns para  roda o seu payload 1=sim =2não"))
if (inicio==1):
	print("pois bém vamos começar")
else:
	dns = int(input("qual dns você quer 1=(no-ip) 2=(duckdns) :"))
	if (dns==1):
		print(banner_install_noip)
		time = os.system('sleep 2')
		print("vou baixar o pacote do no-ip para o senhor e instalar ")
		du = int(input("você tem uma conta no no-ip 1=sim 2=não :"))
		if (du==1):
			print(banner_install_noip)
			install = os.system('bash /opt/gerapay/install_noip/install.sh')
			print("no-ip instalado, agora vamos retornar para o programar apra você poder gerar o seu payload")
			time = os.system('sleep 2 ')
		else:
			print("vou abrir o seu firefox para  você criar a sua conta ")
			fire = os.system('firefox https://www.noip.com/pt-BR/sign-up')
			log = os.system('bash /opt/gerapay/install_noip/install.sh')
			time = os.system('sleep')
	else:
		print(banner_install_duck)
		time = os.system('sleep 2')
		print("vou usar o pacote duckdns gui linux ")
		du = int(input("você tem uma conta no duckdns 1=s =2 :"))
		limp = os.system('clear')
		if (du==1):
			print("qual e o seu sistem (1-base-arch 2-base-debian/ubuntu 3-base-suse)? :")
			install = int(input("qual o seu su sistema (/1/2/3/)"))
			if(install==1):
				print("arch") #configuração do  duckdns no arch linux 
				time = os.system('sleep 2')
				limp = os.system('clear')
				install = os.system('pacman -S zenity cron curl')
				install = os.system("bash /opt/gerapay/install_duckdns/duck-setup-gui.sh")
				print("pronto, agora va gerar o seu payload")
				re = os.system("python gera.py")

			if (install==2): # configuração do duckdns no ubuntu / debian
				print("ubunut/debian")
				time = os.system('sleep 2')
				limp = os.system('clear')
				install = os.system("apt-get install  zenity cron curl")
			else: #configura;'ao do duckdns no suse-base
				print("base-suse")
				time = os.system('sleep 2')
				limp = os.system('clear')
				install = os.system("yum install zenity cron curl")
			install = os.system("bash /opt/gerapay/install_duckdns/duck-setup-gui.sh")
			print("pront va,ps gerar o payload")
		else: #configura'ao da conta do duckdns com loop
			print("vou abrir o seu firefox para voce se loga")
			fire = os.system("firefox https://www.duckdns.org/login?generateRequest=persona")
			print("conta ceiada ? , volte e configure o seu dns :D")

	re = os.system('python gera.py')
																										
