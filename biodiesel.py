#BIODIESEL TRANSESTERIFICATION YIELD CALCULATOR


option = 'S'

other = [0, 0, 0, 0, 0, 0, 0, 0]
macid = [0, 0, 0, 0, 0, 0, 0, 0]
molacid = [0, 0, 0, 0, 0, 0, 0, 0]
MMacido = [144.2, 172.27, 200.32, 228.37, 256.42, 284.47, 282.46, 280.44]
babacu = [3.5, 4.5, 44.7, 17.5, 9.7, 3.1, 15.2, 1.8]
palma = [0, 0, 0.1, 1.2, 46.8, 3.8,37.6, 10.5]
pinhao = [0, 0, 0.02, 0.07, 12.9, 5.63, 39.73, 40]
andiroba = [0, 0, 0, 0, 29.91, 9.95, 46.90, 10.74]
macuaba = [5.39, 3.96, 36.09, 10.19, 8.65, 3.58, 27.7, 3.39]
soja = [0, 0, 0, 0, 10.82, 3.69, 24.18, 52.72]
cafe = [0, 0, 0, 0, 10.90, 3.73, 26.23, 51]
concesp = [0, 0, 0, 0, 0, 0, 0, 0]
rend = [0, 0, 0, 0, 0, 0, 0, 0]
mestersp = [0, 0, 0, 0, 0, 0, 0, 0]
MMester = [0, 0, 0, 0, 0, 0, 0, 0]


def rendimento(df, concesp, pmm):
    croma = [0, 0, 0, 0, 0, 0, 0, 0]
    s1 = 0
    s2 = 0
    print('Enter the concentration provided by the chromatograph in g/g: ')
    for i in range(0,6):
        #croma.append(input(f'C{2*i+8}'))
        croma[i] = input(f'C{2*i+8}: ')
    croma[6] = input(f'C18:1 = ')
    croma[7] = input(f'C18:2 = ') 
    #croma.append(input(f'C18:1 = '))  
    #croma.append(input(f'C18:2 = '))     
    for i in range(0,8):
        if concesp[i] == 0:
            rend[i] = 0
            #rend.append(0)
        else:
            rend[i] = 100*croma[i]*df/concesp[i]
            #rend.append(100*croma[i]*fd/concesp[i])
            s1 = s1 + croma[i]*df
            s2 = s2 + concesp[i]
    if s2 == 0:
        rendtotal = 0
    else:
        rendtotal = s1/s2
    
    print('RENDIMENTOS PARCIAIS')
    for i in range(0,6):
        print(f'C{2*i+8} = {rend[i]:.2f}')
    print(f'C18:1 = {rend[6]:.2f}')
    print(f'C18:2 = {rend[7]:.2f}')
    print(f'RENDIMENTO TOTAL = {100*rendtotal:.2f}%')
    return rendtotal

for i in range(0,8):
    MMester.append(MMacido[i] + 28)
    

while option == 'S':
    print('*'*5 + 'BIODIESEL TRANSESTERIFICATION YIELD CALCULATOR' + '*'*5 + "\n")
    print("1 - Babacu \n2 - Palma \n3 - Pinhao Manso \n4 - Andiroba \n5 - Macauba (amendoa) \n6 - Soja \n7 - Cafe \n8 - Outro \n")
    oil = int(input("Choose between above options which one is yours: "))

    if oil == 8:
        MMacid = 0
        print("Input with oil composition in %: \n")
        i = 0
        for i in range(6):
            x = 2*i +8
            other[i] = float(input(f'C{x} = '))


        other[6] = float(input("C18:1 = "))
        other[7] = float(input("C18:2 = "))
        print(other)
        
        i = 0
        for i in range(8):
            MMacid = MMacid + other[i]*MMacido[i]/100
        MMoil = 3*MMacid + 38

        print(f'Oil molar mass = {MMoil:.2f} g/mol')

    option = input('Do you use any solvent for biodiesel production? [s/n] ').upper()

    if option == "S":
        ps = float(input('Wich % does the solvent corespond? '))

    sam = float(input('Sample diluition before chromatografic analysis: \nsample mass (g) = '))
    som = float(input('solvent mass (g) = '))

    if (option == 'S'):
        df = (sam + som)/((1 - ps/100)*sam)
    else:
        df = (sam + som)/sam
    print(f'Dilution factor = {df:.4f}')

    print('Input the molar rate between reagents ')
    oil_mol = float(input("Oil mol = "))
    ethanol_mol = float(input("Ethanol mol = "))
    MMacid = 0

    if oil == 1:
        for i in range(0,8):
            MMacid = MMacid + babacu[i]*MMacido[i]/100 
        MMoil = 3*MMacid + 38
        print(f'Oil molar mass = {MMoil:.2f} g/mol')
        pmo = 1 - 38/MMoil
        pmm = 1 + ethanol_mol*46/MMoil

        
        for i in range(0,8):
            macid[i] = float(pmo*babacu[i]/100)
            if (macid[i] == 0):
                molacid[i] = 0
            else:
                molacid[i] = float(macid[i]/MMacido[i])
            if (molacid[i] == 0):
                mestersp[i] = 0
            else:
                mestersp[i] = float(molacid[i]*MMester[i])
                concesp[i] = float(mestersp[i]/pmm)

        print(f'o concesp é {concesp}')
        print(f'o molacid é {molacid}')
        print(f'o mestersp é {mestersp}')
        print(f'o MMester é {MMester}')

    if oil == 2:
        for i in range(0,8):
            MMacid = MMacid + palindrome[i]*MMacido[i]/100
        MMoil = 3*MMacid + 38
        print(f'Oil molar mass = {MMoil:.2f} g/mol')
        pmo = 1 - 38/MMoil
        pmm = 1 + ethanol_mol*46/MMoil

        for i in range(0,8):
            macid[i] = pmo*palma[i]/100
            if (macid[i] == 0):
                molacid[i] == 0
            else:
                molacid[i] = macid[i]/MMacido
            if (molacid[i] == 0):
                mestersp[i] = 0
            else:
                mestersp[i] = molacid[i]*MMester[i]
                concesp[i] = mestersp[i]/pmm
    
    if oil == 3:
        for i in range(0,8):
            MMacid = MMacid + palindrome[i]*MMacido[i]/100
        MMoil = 3*MMacid + 38
        print(f'Oil molar mass = {MMoil:.2f} g/mol')
        pmo = 1 - 38/MMoil
        pmm = 1 + ethanol_mol*46/MMoil

        for i in range(0,8):
            macid[i] = pmo*palma[i]/100
            if (macid[i] == 0):
                molacid[i] == 0
            else:
                molacid[i] = macid[i]/MMacido
            if (molacid[i] == 0):
                mestersp[i] = 0
            else:
                mestersp[i] = molacid[i]*MMester[i]
                concesp[i] = mestersp[i]/pmm
    
    if oil == 4:
        for i in range(0,8):
            MMacid = MMacid + palindrome[i]*MMacido[i]/100
        MMoil = 3*MMacid + 38
        print(f'Oil molar mass = {MMoil:.2f} g/mol')
        pmo = 1 - 38/MMoil
        pmm = 1 + ethanol_mol*46/MMoil

        for i in range(0,8):
            macid[i] = pmo*palma[i]/100
            if (macid[i] == 0):
                molacid[i] == 0
            else:
                molacid[i] = macid[i]/MMacido
            if (molacid[i] == 0):
                mestersp[i] = 0
            else:
                mestersp[i] = molacid[i]*MMester[i]
                concesp[i] = mestersp[i]/pmm
    
    if oil == 5:
        for i in range(0,8):
            MMacid = MMacid + palindrome[i]*MMacido[i]/100
        MMoil = 3*MMacid + 38
        print(f'Oil molar mass = {MMoil:.2f} g/mol')
        pmo = 1 - 38/MMoil
        pmm = 1 + ethanol_mol*46/MMoil

        for i in range(0,8):
            macid[i] = pmo*palma[i]/100
            if (macid[i] == 0):
                molacid[i] == 0
            else:
                molacid[i] = macid[i]/MMacido
            if (molacid[i] == 0):
                mestersp[i] = 0
            else:
                mestersp[i] = molacid[i]*MMester[i]
                concesp[i] = mestersp[i]/pmm
    if oil == 6:
        for i in range(0,8):
            MMacid = MMacid + palindrome[i]*MMacido[i]/100
        MMoil = 3*MMacid + 38
        print(f'Oil molar mass = {MMoil:.2f} g/mol')
        pmo = 1 - 38/MMoil
        pmm = 1 + ethanol_mol*46/MMoil

        for i in range(0,8):
            macid[i] = pmo*palma[i]/100
            if (macid[i] == 0):
                molacid[i] == 0
            else:
                molacid[i] = macid[i]/MMacido
            if (molacid[i] == 0):
                mestersp[i] = 0
            else:
                mestersp[i] = molacid[i]*MMester[i]
                concesp[i] = mestersp[i]/pmm

    if oil == 7:
        for i in range(0,8):
            MMacid = MMacid + palindrome[i]*MMacido[i]/100
        MMoil = 3*MMacid + 38
        print(f'Oil molar mass = {MMoil:.2f} g/mol')
        pmo = 1 - 38/MMoil
        pmm = 1 + ethanol_mol*46/MMoil

        for i in range(0,8):
            macid[i] = pmo*palma[i]/100
            if (macid[i] == 0):
                molacid[i] == 0
            else:
                molacid[i] = macid[i]/MMacido
            if (molacid[i] == 0):
                mestersp[i] = 0
            else:
                mestersp[i] = molacid[i]*MMester[i]
                concesp[i] = mestersp[i]/pmm

    if oil == 8:
        for i in range(0,8):
            MMacid = MMacid + palindrome[i]*MMacido[i]/100
        MMoil = 3*MMacid + 38
        print(f'Oil molar mass = {MMoil:.2f} g/mol')
        pmo = 1 - 38/MMoil
        pmm = 1 + ethanol_mol*46/MMoil

        for i in range(0,8):
            macid[i] = pmo*palma[i]/100
            if (macid[i] == 0):
                molacid[i] == 0
            else:
                molacid[i] = macid[i]/MMacido
            if (molacid[i] == 0):
                mestersp[i] = 0
            else:
                mestersp[i] = molacid[i]*MMester[i]
                concesp[i] = mestersp[i]/pmm
    
    rendimento(df,concesp, pmm)

    option = input('Deseja executar novamente [s/n]? ').upper()

