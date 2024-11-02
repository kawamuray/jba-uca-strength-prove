import math

FRONT_WEIGHT_KG = 1030
WHEEL_BASE_MM = 2650
SHEET1_OFFSET_MM = 1300
SHEET1_PPL = 2
SHEET2_OFFSET_MM = 2100
SHEET2_PPL = 3
PERSON_WEIGHT_KG = 55
LOAD_FACTOR = 2.5
SAFETY_FACTOR = 1.6



ARM_OD_MM = 26.92
ARM_ID_MM = 19.05
TUBE_TENSIL_MPA = 517 # Mpa
TUBE_TENSIL_KGF_MM = round(TUBE_TENSIL_MPA * 0.10197, 2) # Kgf/mm2
print(TUBE_TENSIL_KGF_MM)

tau_max = TUBE_TENSIL_KGF_MM
d1 = round(((ARM_OD_MM / 2.0)**2 - (ARM_ID_MM / 2.0)**2) * 3.14, 2)
shear_tsuyosa = round(tau_max / math.sqrt(3), 2)
shear_force = round(d1 * shear_tsuyosa, 2)

front_w_total = round(FRONT_WEIGHT_KG + PERSON_WEIGHT_KG * (SHEET1_PPL * (WHEEL_BASE_MM - SHEET1_OFFSET_MM) + SHEET2_PPL * (WHEEL_BASE_MM - SHEET2_OFFSET_MM)) / WHEEL_BASE_MM, 2)
front_w_half = round(front_w_total / 2, 2)
front_w_half = round(front_w_half * LOAD_FACTOR, 2)

multi_factor = round(shear_force / (front_w_half / 2.0), 2)


print("車両総前軸重: {}".format(front_w_total))
print("車両総片前軸重: {}".format(front_w_half / LOAD_FACTOR))
print("片前軸最大荷重: {}".format(front_w_half))

print("引張強度(Kgf/mm2): {}".format(TUBE_TENSIL_MPA))
print("断面積: {}".format(d1))
print("せん断強さ: {}".format(shear_tsuyosa))
print("せん断力: {}".format(shear_force))

print("破壊安全率: {}".format(multi_factor))
