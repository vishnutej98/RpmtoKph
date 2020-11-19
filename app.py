from openpyxl import Workbook
from openpyxl.styles import Font

print('''
Data Sheet of the Vehicle
please enter the specification for the vehicle
''')

book = Workbook()
Sheet = book.active
Gear = int(input('No of Gear Box: '))
if Gear >= 6:
    print("Sorry this Program only runs for 4 and 5 Speed Gear Box.")
else:
    print(f"{Gear} Speed Gear Box.")
    Vehicle_name = str(input('Name of the Vehicle: ')).title()
    Project_Code = input('Project Code: ').upper()
    PI = 3.142857
    print(f"The Data is Calculated for {Vehicle_name} / {Project_Code}.")
    P = float(input("Primary Gear Ratio: "))  # Primary Transmission Ratio.
    S = float(input("Secondary Gear Ratio: "))  # Secondary Transmission Ratio.
    R = float(input('Wheel Rolling radius in meters: '))  # Dynamic Rolling Radius in meters.
    Factor = round(2 * PI * R * 0.06, 3)
    PPM = int(input('Peak Power RPM: '))  # Peak Power RPM.
    G2 = float(input('2nd Gear Ratio: '))  # 2nd Gear Ratio.
    G3 = float(input('3rd Gear Ratio: '))  # 3rd Gear Ratio.
    if Gear == 5:
        G4 = float(input('4th Gear Ratio: '))  # 4th Gear Ratio.
    R2 = round(P * S * G2, 3)  # Total 2nd Gear Ratio.
    R3 = round(P * S * G3, 3)  # Total 3rd Gear Ratio.
    RK2 = round(R2 / Factor, 3)  # 2nd Gear RPM to KPH Ratio.
    RK3 = round(R3 / Factor, 3)  # 3rd Gear RPM to KPH Ratio.
    ES2 = round(float(((0.75 * PPM) / R2) * Factor))  # Entry Speed at 2nd Gear in KPH.
    ES3 = round(float(((0.75 * PPM) / R3) * Factor))  # Entry Speed at 3rd Gear in KPH.
    EXS2 = round(float((PPM / R2) * Factor))  # Exit Speed at 2nd Gear in KPH.
    EXS3 = round(float((PPM / R3) * Factor))  # Exit Speed at 3rd Gear in KPH.

    print(f"""
    The {Vehicle_name} with Project code {Project_Code} with {Gear} Gears has the following values.
    """)
    spec_list = [
        Vehicle_name, Project_Code, Gear, Factor, P, S, R, PPM, G2, G3, RK2, RK3, ES2, EXS2, ES3, EXS3
    ]
    spec_names = [
        "Vehicle name", "Project Code", "Gear Box", "Factor = (2 * PI * R * 0.06)", "Primary Gear Ratio",
        "Secondary Gear Ratio", "Dynamic Rolling Radius in meters", "Max Peak Power RPM", "Total 2ndGear ratio",
        "Total 3rdGear ratio", "2ndGear RPMtoKPH ratio", "3rdGear RPMtoKPH ratio", "Entry Speed at 2nd Gear in KPH",
        "Exit Speed at 2nd Gear in KPH", "Entry Speed at 3rd Gear in KPH", "Exit Speed at 3rd Gear in KPH"
    ]

    # Output Result Display Variables.
    i = 0
    j = 0
    for f in range(0, 3):  # Output Result Display loop.
        print(f"{spec_names[i]}: {spec_list[j]}")
        i += 1
        j += 1

    # Excel Result Variables.
    n = 0
    m = 0
    for g in range(5, 21):  # Excel Result loop.
        Sheet[f'C{g}'] = f'{spec_names[n]}'
        Sheet[f'D{g}'] = f'{spec_list[m]}'
        n += 1
        m += 1

    #  Making Rows(Top two and bottom four rows) Bold.
    for b in list(range(5, 7)) + list(range(17, 22)):
        Sheet[f'C{b}'].font = Font(bold=True)
        Sheet[f'D{b}'].font = Font(bold=True)
    book.save(str(Project_Code) + ".xlsx")
    print(f"Data is saved in Excel file named as {Project_Code}.")