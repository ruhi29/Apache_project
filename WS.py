
print('''
░░░░░░  ░░    ░░ ░░   ░░ ░░ 
▒▒   ▒▒ ▒▒    ▒▒ ▒▒   ▒▒ ▒▒ 
▒▒▒▒▒▒  ▒▒    ▒▒ ▒▒▒▒▒▒▒ ▒▒ 
▓▓   ▓▓ ▓▓    ▓▓ ▓▓   ▓▓ ▓▓ 
██   ██  ██████  ██   ██ ██ ''')

with open("website.log","r") as f:
    lines=f.readlines()
    with open("output.txt", "w+") as nf:
        for line in lines:
            line=line.split()
            nf.write("IP\t            Date Time\t                Request\tPath\t                    Protocol\tStatus  Code\tUser\tAgent\n")
            nf.write(f'{line[0]}\t{line[3]+line[4]}\t{line[5]}\t{line[6]}\t{line[7]}\t{line[8]}\t\t{line[11]+line[12]+line[13]+line[14]}\n')



