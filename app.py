#!Python3
# app.py - This application will calculate the Gear ratio's
# Vehicle Entry speed and calculated Exit speed for the vehicle.
# From this Calculation based on user requirement the calculation can be stored
# Files can be saved in .PDF, .xlsx, .txt
import time
from fpdf import FPDF
from openpyxl import Workbook as wb
from openpyxl.styles import Font
from calculation import GearRatio, InputData, DataLabel

Vehicle_name = str(input("Enter the Vehicle Name: ")).title()
Gear = int(input("No. of Gears: "))
# InputDataDict = {}

if Gear >= 6:
    print("Sorry! this file will calculate only for 4 or 5 speed gear box.")
    pass
elif Gear <=3:
  print("Sorry! this file will calculate only for 4 or 5 speed gear box.")
  pass
else:
  input_data = list(InputData.Ratio_Input())
  data_label = DataLabel.Label()
  # print(dl)
  InputDataDict = {}
  for key in data_label:
    for value in input_data:
      InputDataDict[key] = value
      input_data.remove(value)
      break

  factorial = GearRatio.fact(InputDataDict['Rolling_Radius'], pi=3.147)
  # print(factorial)

  #2nd and 3rd Gear Ratio calculation
  RTK_2ndGearRatio = GearRatio.RPM_to_KPH_ratio_2nd_Gear(InputDataDict['total_2nd_gear_ratio'], factorial)
  RTK_3rdGearRatio = GearRatio.RPM_to_KPH_ratio_3rd_Gear(InputDataDict['total_3rd_gear_ratio'], factorial)
  print(RTK_2ndGearRatio)
  print(RTK_3rdGearRatio)

  #Entry Speed calculations
  EntrySpeed_2ndGear = GearRatio.Entry_Speed_2nd_Gear(InputDataDict['peak_power_rpm'],InputDataDict['total_2nd_gear_ratio'],factorial)
  print(EntrySpeed_2ndGear)

  EntrySpeed_3rdGear = GearRatio.Entry_Speed_3rd_Gear(InputDataDict['peak_power_rpm'],InputDataDict['total_3rd_gear_ratio'],factorial)
  print(EntrySpeed_3rdGear)

  ExitSpeed_2ndGear = GearRatio.Exit_Speed_2nd_Gear(InputDataDict['peak_power_rpm'],InputDataDict['total_2nd_gear_ratio'],factorial)
  print(f'Exit Speed for 2nd gear: {ExitSpeed_2ndGear}')

  ExitSpeed_3rdGear = GearRatio.Exit_Speed_3rd_Gear(InputDataDict['peak_power_rpm'],InputDataDict['total_3rd_gear_ratio'],factorial)
  print(f'Exit Speed for 3rd gear: {ExitSpeed_3rdGear}')

  #Data_Label and Data collection for the results
  Spec_Label = ['Vehicle_name', 'Gear Box', 'Factor = (2 * PI * R * 0.06)', 'Primary Transmission Ratio', 'Secondary Transmission ratio', 'Dynamic Rolling Radius in m', 'Max Peak Power RPM', 'total_2nd_gear_ratio', 'total_3rd_gear_ratio', 'RTK_2ndGearRatio', 'RTK_3rdGearRatio', 'EntrySpeed_2ndGear', 'EntrySpeed_3rdGear', 'ExitSpeed_2ndGear', 'ExitSpeed_3rdGear']

  Spec_List = [Vehicle_name,Gear,factorial,InputDataDict['primary_ratio'], InputDataDict['secondary_ratio'], InputDataDict['Rolling_Radius'], InputDataDict['peak_power_rpm'], InputDataDict['total_2nd_gear_ratio'], InputDataDict['total_3rd_gear_ratio'], RTK_2ndGearRatio, RTK_3rdGearRatio, EntrySpeed_2ndGear, EntrySpeed_3rdGear, ExitSpeed_2ndGear, ExitSpeed_3rdGear]

  time.sleep(1)
  print('''
  Loading........
  ''')
  print(f"The data will be calculated for {Vehicle_name}.")
  time.sleep(1)
  print("""
      Please select the option below to save the data in a file:
      
          1. PDF(.pdf)
          2. Excel(.xlsx)
          3. Text(.txt) under construction
      """)
  user_input = int(input('Enter numerical value only: '))
  time.sleep(2)

  if user_input == 1:
          file = open("data.txt", "w")
          for i in range(0, 7):
              file.write(f"{Spec_Label[i]} : {Spec_List[i]}\n")

          file.write("\n")
          file.write("\n")

          for j in range(7, 11):
              file.write(f"{Spec_Label[j]} : {Spec_List[j]}\n")

          file.write("\n")
          file.write("\n")

          for k in range(11, 15):
              file.write(f"{Spec_Label[k]} : {Spec_List[k]}\n")
          file.close()

          pdf = FPDF()
          pdf.add_page()
          pdf.set_font("Times", size=14)
          read_file = open("data.txt", "r")
          for x in read_file:
            pdf.cell(200, 10, txt=x, ln=1, align='L')
          pdf.output(f"{Vehicle_name}.pdf")
          print(f"Data is saved in PDF file named as {Vehicle_name}.pdf")


  elif user_input == 2:
    # Ref 3import
        # from openpyxl import Workbook
        # Ref 4import
        # from openpyxl.styles import Font

        book = wb()
        Sheet = book.active
        n = 0
        m = 0
        for g in range(5, 20):  # Excel Result loop.
            Sheet[f'C{g}'] = f'{Spec_Label[n]}'
            Sheet[f'D{g}'] = f'{Spec_List[m]}'
            n += 1
            m += 1

        #  Making Rows(Top two and bottom four rows) Bold.
        for b in list(range(4, 6)) + list(range(16, 21)):
            Sheet[f'C{b}'].font = Font(bold=True)
            Sheet[f'D{b}'].font = Font(bold=True)
            Sheet.column_dimensions['C'].width = 27.33
        book.save(str(Vehicle_name) + ".xlsx")
        print(f"Data is saved in Excel file named as {Vehicle_name}.xlsx")

  elif user_input == 3:
    print('This module is still under construction!!')