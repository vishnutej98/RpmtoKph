class InputData():
  
  def Ratio_Input():
    primary_ratio = float(input('Primary Transmission Ratio: '))
    secondary_ratio = float(input('Secondary Transmission ratio: '))
    Rolling_Radius = float(input('Rolling radius (in m): '))
    peak_power_rpm = float(input('Peak Power RPM: '))
    Gear2 = float(input('2nd Gear ratio: '))
    Gear3 = float(input('3rd Gear ratio: '))
    total_2nd_gear_ratio = round(primary_ratio * secondary_ratio * Gear2, 3)
    total_3rd_gear_ratio = round(primary_ratio * secondary_ratio * Gear3, 3)
    return primary_ratio, secondary_ratio, Rolling_Radius, peak_power_rpm, Gear2, Gear3, total_2nd_gear_ratio, total_3rd_gear_ratio


class GearRatio():

  def fact(Rolling_Radius, pi=3.147):
    factor = round(2*pi*Rolling_Radius*0.06, 3)
    return factor
    # print(factor)

  def RPM_to_KPH_ratio_2nd_Gear(total_2nd_gear_ratio, fact):
    Ratio_2nd_gear = round(total_2nd_gear_ratio/fact, 3)
    # return Ratio_2nd_gear
    return Ratio_2nd_gear

  def RPM_to_KPH_ratio_3rd_Gear(total_3rd_gear_ratio, fact):
    Ratio_3rd_gear = round(total_3rd_gear_ratio / fact, 3)
    return Ratio_3rd_gear

  def Entry_Speed_2nd_Gear(peak_power_rpm, total_2nd_gear_ratio, fact):
    Entry_Speed_2nd_Gear = round(float(((0.75 * peak_power_rpm) / total_2nd_gear_ratio) * fact), 2)
    return Entry_Speed_2nd_Gear
  
  def Entry_Speed_3rd_Gear(peak_power_rpm, total_3rd_gear_ratio, fact):
    Entry_Speed_3rd_Gear = round(float(((0.75 * peak_power_rpm) / total_3rd_gear_ratio) * fact), 2)
    return Entry_Speed_3rd_Gear

  def Exit_Speed_2nd_Gear(peak_power_rpm, total_2nd_Gear_ratio, fact):
    Exit_Speed_2nd_Gear = round(float((peak_power_rpm / total_2nd_Gear_ratio) * fact), 2)
    return Exit_Speed_2nd_Gear

  def Exit_Speed_3rd_Gear(peak_power_rpm, total_3rd_Gear_ratio, fact):
    Exit_Speed_3rd_Gear = round(float((peak_power_rpm / total_3rd_Gear_ratio) * fact), 2)
    return Exit_Speed_3rd_Gear

class DataLabel():

  def Label():
    return ['primary_ratio', 'secondary_ratio', 'Rolling_Radius', 'peak_power_rpm', 'Gear2', 'Gear3', 'total_2nd_gear_ratio', 'total_3rd_gear_ratio']

