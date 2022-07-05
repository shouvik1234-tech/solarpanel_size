import math
def electric_energy_requiredin_elipse_BOL(power_eclipse_BOL,Tecl):
    electric_energy_requiredin_elipse_BOL=power_eclipse_BOL*(Tecl*60)
    return electric_energy_requiredin_elipse_BOL

def Totalpower_required(power_eclipse_BOL,power_forchargebattery):
    Totalpower_required=power_eclipse_BOL+power_forchargebattery
    return Totalpower_required

def power_forchargebattery(eta_charge,eta_discharge,Tsun,electric_energy_requiredin_elipse_BOL):
    power_forchargebattery=electric_energy_requiredin_elipse_BOL/(eta_charge*0.01*eta_discharge*0.01*Tsun*60)
    return power_forchargebattery

def Energystored_battery(electric_energy_requiredin_elipse_BOL,eta_discharge):
    Energystored_battery=electric_energy_requiredin_elipse_BOL/(eta_discharge*0.01)
    return Energystored_battery

def areaofsolarpanel_required(Totalpower_required,phi,eta_ofpvcells,loss_efficiency,theta):
    areaofsolarpanel_required=Totalpower_required/(phi*math.cos(theta*(3.14/180))*eta_ofpvcells*0.01*(1-other_losses*0.01))
    return areaofsolarpanel_required



power_eclipse_EOL=float(input("enter the power required by cubsat in watt during eclipse period in EOL:")) #EOL-end of life
degradation_peryear=float(input("enter the degradation of solar array per year in %:"))  #2.7% per year
flight_period=float(input("enter the total time of flight of the cubsat in years:"))
power_eclipse_BOL=power_eclipse_EOL/(1-(degradation_peryear*0.01))**flight_period #BOL-beginning of life
Tecl=float(input("enter the eclipse period in min:"))
Torbit=float(input("enter the orbital period:"))
Tsun=Torbit-Tecl
eta_charge=float(input("enter the charging efficiency:"))  #100%
eta_discharge=float(input("enter the discharging efficiency:"))  #94% for battery temp less than 15 degree celcius
theta=float(input("enter the angle of incident of sunray on solarpanel in degrees:"))
eta_ofpvcells=float(input("enter the effiency of pvcells:"))   #30%
other_losses=float(input("enter the loss of efficiency by other reasons:")) #5 to 10 %
phi=1370  #in watts/m^2


print("the power required during eclipse in BOL",power_eclipse_BOL)

electric_energy_requiredin_elipse_BOL=electric_energy_requiredin_elipse_BOL(power_eclipse_BOL,Tecl)
print("electric energy required during eclipse in BOL:",electric_energy_requiredin_elipse_BOL,"jouls")

Totalpower_required=Totalpower_required(power_eclipse_BOL,power_forchargebattery(eta_charge,eta_discharge,Tsun,electric_energy_requiredin_elipse_BOL))
print("total power required by the cubsat in the non eclipse phase to power its load and charge its battery:",Totalpower_required,"watt")


Energystored_battery= Energystored_battery(electric_energy_requiredin_elipse_BOL,eta_discharge)
print("energy should be stored in the batteries to power the load during eclipse:",Energystored_battery,"joules")

areaofsolarpanel_required=areaofsolarpanel_required(Totalpower_required,phi,eta_ofpvcells,other_losses,theta)
print("area of solar panel required for generation of required power:",areaofsolarpanel_required,"m^2")




