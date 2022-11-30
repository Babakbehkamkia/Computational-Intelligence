# Q2_graded

!pip install simpful

# Q2_graded

from simpful import *

FS = FuzzySystem()

player_price = AutoTriangle(6, terms=['very_cheap', 'cheap', 'normal', 'expensive', 'very_expensive', 'extremely_expensive'], universe_of_discourse=[20,600])
player_age = AutoTriangle(5, terms=['very_young', 'young', 'middle_age', 'old', 'very_old'], universe_of_discourse=[18,35])
last_5_maches = AutoTriangle(3, terms=['bad', 'medium', 'good'], universe_of_discourse=[0,5])

FS.add_linguistic_variable("price_goalkeeper_Foolad", player_price)
FS.add_linguistic_variable("age_goalkeeper_Foolad", player_age)

FS.add_linguistic_variable("price_left_difender_Foolad", player_price)
FS.add_linguistic_variable("age_left_difender_Foolad", player_age)

FS.add_linguistic_variable("price_right_difender_Foolad", player_price)
FS.add_linguistic_variable("age_right_difender_Foolad", player_age)

FS.add_linguistic_variable("price_mid_difender_1_Foolad", player_price)
FS.add_linguistic_variable("age_mid_difender_1_Foolad", player_age)

FS.add_linguistic_variable("price_mid_difender_2_Foolad", player_price)
FS.add_linguistic_variable("age_mid_difender_2_Foolad", player_age)

FS.add_linguistic_variable("price_mid_fielder_1_Foolad", player_price)
FS.add_linguistic_variable("age_mid_fielder_1_Foolad", player_age)

FS.add_linguistic_variable("price_mid_fielder_2_Foolad", player_price)
FS.add_linguistic_variable("age_mid_fielder_2_Foolad", player_age)

FS.add_linguistic_variable("price_mid_fielder_3_Foolad", player_price)
FS.add_linguistic_variable("age_mid_fielder_3_Foolad", player_age)

FS.add_linguistic_variable("price_right_forward_Foolad", player_price)
FS.add_linguistic_variable("age_right_forward_Foolad", player_age)

FS.add_linguistic_variable("price_left_forward_Foolad", player_price)
FS.add_linguistic_variable("age_left_forward_Foolad", player_age)

FS.add_linguistic_variable("price_center_forward_Foolad", player_price)
FS.add_linguistic_variable("age_center_forward_Foolad", player_age)


# ====================================


FS.add_linguistic_variable("price_goalkeeper_Sepahan", player_price)
FS.add_linguistic_variable("age_goalkeeper_Sepahan", player_age)

FS.add_linguistic_variable("price_left_difender_Sepahan", player_price)
FS.add_linguistic_variable("age_left_difender_Sepahan", player_age)

FS.add_linguistic_variable("price_right_difender_Sepahan", player_price)
FS.add_linguistic_variable("age_right_difender_Sepahan", player_age)

FS.add_linguistic_variable("price_mid_difender_1_Sepahan", player_price)
FS.add_linguistic_variable("age_mid_difender_1_Sepahan", player_age)

FS.add_linguistic_variable("price_mid_difender_2_Sepahan", player_price)
FS.add_linguistic_variable("age_mid_difender_2_Sepahan", player_age)

FS.add_linguistic_variable("price_mid_fielder_1_Sepahan", player_price)
FS.add_linguistic_variable("age_mid_fielder_1_Sepahan", player_age)

FS.add_linguistic_variable("price_mid_fielder_2_Sepahan", player_price)
FS.add_linguistic_variable("age_mid_fielder_2_Sepahan", player_age)

FS.add_linguistic_variable("price_mid_fielder_3_Sepahan", player_price)
FS.add_linguistic_variable("age_mid_fielder_3_Sepahan", player_age)

FS.add_linguistic_variable("price_right_forward_Sepahan", player_price)
FS.add_linguistic_variable("age_right_forward_Sepahan", player_age)

FS.add_linguistic_variable("price_left_forward_Sepahan", player_price)
FS.add_linguistic_variable("age_left_forward_Sepahan", player_age)

FS.add_linguistic_variable("price_center_forward_Sepahan", player_price)
FS.add_linguistic_variable("age_center_forward_Sepahan", player_age)


# =====================


FS.add_linguistic_variable("performance_Foolad", last_5_maches)
FS.add_linguistic_variable("performance_Sepahan", last_5_maches)


result = AutoTriangle(3, terms=['Sepahan_win', 'tie', 'Foolad_win'], universe_of_discourse=[-10,10])
FS.add_linguistic_variable("result_1", result)
FS.add_linguistic_variable("result_2", result)
FS.add_linguistic_variable("result_3", result)
FS.add_linguistic_variable("result_4", result)
FS.add_linguistic_variable("result_5", result)
FS.add_linguistic_variable("result_6", result)

# Q2_graded

# res1 = goal keeper value
# res2 = defender value
# res3 = forwards value
# res4 = goalkeeper value vs forward value
# res5 = defender value vs forward value
# res6 = last 5 maches

# Q2_graded

Rules1 = [
        "IF (price_goalkeeper_Foolad IS expensive) THEN (result_1 IS Foolad_win)",
        "IF (price_goalkeeper_Sepahan IS expensive) THEN (result_1 IS Sepahan_win)",
        "IF (age_goalkeeper_Sepahan IS middle_age) THEN (result_1 IS Sepahan_win)",
        "IF (age_goalkeeper_Foolad IS very_old) THEN (result_1 IS Sepahan_win)",
        "IF (age_goalkeeper_Sepahan IS very_old) THEN (result_1 IS Foolad_win)",
        "IF (price_goalkeeper_Foolad IS cheap) THEN (result_1 IS Sepahan_win)",
]

# Q2_graded

Rules2 = [
        "IF (price_mid_difender_1_Foolad IS expensive) THEN (result_2 IS Foolad_win)",
        "IF (price_mid_difender_1_Sepahan IS expensive) THEN (result_2 IS Sepahan_win)",
        "IF (age_mid_difender_1_Foolad IS middle_age) THEN (result_2 IS Foolad_win)",
        "IF (age_mid_difender_1_Sepahan IS middle_age) THEN (result_2 IS Sepahan_win)",
        "IF (age_mid_difender_1_Foolad IS very_old) THEN (result_2 IS Sepahan_win)",
        "IF (age_mid_difender_1_Sepahan IS very_old) THEN (result_2 IS Foolad_win)",
        "IF (price_mid_difender_1_Foolad IS cheap) THEN (result_2 IS Sepahan_win)",
        "IF (price_mid_difender_1_Sepahan IS cheap) THEN (result_2 IS Foolad_win)",

        "IF (price_mid_difender_2_Foolad IS expensive) THEN (result_2 IS Foolad_win)",
        "IF (price_mid_difender_2_Sepahan IS expensive) THEN (result_2 IS Sepahan_win)",
        "IF (age_mid_difender_2_Foolad IS middle_age) THEN (result_2 IS Foolad_win)",
        "IF (age_mid_difender_2_Sepahan IS middle_age) THEN (result_2 IS Sepahan_win)",
        "IF (age_mid_difender_2_Foolad IS very_old) THEN (result_2 IS Sepahan_win)",
        "IF (age_mid_difender_2_Sepahan IS very_old) THEN (result_2 IS Foolad_win)",
        "IF (price_mid_difender_2_Foolad IS cheap) THEN (result_2 IS Sepahan_win)",
        "IF (price_mid_difender_2_Sepahan IS cheap) THEN (result_2 IS Foolad_win)",

        "IF (price_left_difender_Foolad IS expensive) THEN (result_2 IS Foolad_win)",
        "IF (price_left_difender_Sepahan IS expensive) THEN (result_2 IS Sepahan_win)",
        "IF (age_left_difender_Foolad IS middle_age) THEN (result_2 IS Foolad_win)",
        "IF (age_left_difender_Sepahan IS middle_age) THEN (result_2 IS Sepahan_win)",
        "IF (age_left_difender_Foolad IS very_old) THEN (result_2 IS Sepahan_win)",
        "IF (age_left_difender_Sepahan IS very_old) THEN (result_2 IS Foolad_win)",
        "IF (price_left_difender_Foolad IS cheap) THEN (result_2 IS Sepahan_win)",
        "IF (price_left_difender_Sepahan IS cheap) THEN (result_2 IS Foolad_win)",

        "IF (price_right_difender_Foolad IS expensive) THEN (result_2 IS Foolad_win)",
        "IF (price_right_difender_Sepahan IS expensive) THEN (result_2 IS Sepahan_win)",
        "IF (age_right_difender_Foolad IS middle_age) THEN (result_2 IS Foolad_win)",
        "IF (age_right_difender_Sepahan IS middle_age) THEN (result_2 IS Sepahan_win)",
        "IF (age_right_difender_Foolad IS very_old) THEN (result_2 IS Sepahan_win)",
        "IF (age_right_difender_Sepahan IS very_old) THEN (result_2 IS Foolad_win)",
        "IF (price_right_difender_Foolad IS cheap) THEN (result_2 IS Sepahan_win)",
        "IF (price_right_difender_Sepahan IS cheap) THEN (result_2 IS Foolad_win)"
]

# Q2_graded

Rules3 = [
        "IF (price_center_forward_Foolad IS expensive) THEN (result_3 IS Foolad_win)",
        "IF (price_center_forward_Sepahan IS expensive) THEN (result_3 IS Sepahan_win)",
        "IF (age_center_forward_Foolad IS middle_age) THEN (result_3 IS Foolad_win)",
        "IF (age_center_forward_Sepahan IS middle_age) THEN (result_3 IS Sepahan_win)",
        "IF (age_center_forward_Foolad IS very_old) THEN (result_3 IS Sepahan_win)",
        "IF (age_center_forward_Sepahan IS very_old) THEN (result_3 IS Foolad_win)",
        "IF (price_center_forward_Foolad IS cheap) THEN (result_3 IS Sepahan_win)",
        "IF (price_center_forward_Sepahan IS cheap) THEN (result_3 IS Foolad_win)",

        "IF (price_left_forward_Foolad IS expensive) THEN (result_3 IS Foolad_win)",
        "IF (price_left_forward_Sepahan IS expensive) THEN (result_3 IS Sepahan_win)",
        "IF (age_left_forward_Foolad IS middle_age) THEN (result_3 IS Foolad_win)",
        "IF (age_left_forward_Sepahan IS middle_age) THEN (result_3 IS Sepahan_win)",
        "IF (age_left_forward_Foolad IS very_old) THEN (result_3 IS Sepahan_win)",
        "IF (age_left_forward_Sepahan IS very_old) THEN (result_3 IS Foolad_win)",
        "IF (price_left_forward_Foolad IS cheap) THEN (result_3 IS Sepahan_win)",
        "IF (price_left_forward_Sepahan IS cheap) THEN (result_3 IS Foolad_win)",

        "IF (price_right_forward_Foolad IS expensive) THEN (result_3 IS Foolad_win)",
        "IF (price_right_forward_Sepahan IS expensive) THEN (result_3 IS Sepahan_win)",
        "IF (age_right_forward_Foolad IS middle_age) THEN (result_3 IS Foolad_win)",
        "IF (age_right_forward_Sepahan IS middle_age) THEN (result_3 IS Sepahan_win)",
        "IF (age_right_forward_Foolad IS very_old) THEN (result_3 IS Sepahan_win)",
        "IF (age_right_forward_Sepahan IS very_old) THEN (result_3 IS Foolad_win)",
        "IF (price_right_forward_Foolad IS cheap) THEN (result_3 IS Sepahan_win)",
        "IF (price_right_forward_Sepahan IS cheap) THEN (result_3 IS Foolad_win)"
]

# Q2_graded

Rules4 = [
        "IF (price_goalkeeper_Foolad IS expensive) AND (price_center_forward_Sepahan IS expensive) THEN (result_4 IS tie)",
        "IF (price_goalkeeper_Sepahan IS expensive) AND (price_center_forward_Foolad IS expensive) THEN (result_4 IS tie)",
        "IF (age_goalkeeper_Foolad IS middle_age) AND (age_center_forward_Sepahan IS young) THEN (result_4 IS Foolad_win)",
        "IF (age_goalkeeper_Sepahan IS middle_age) AND (age_center_forward_Foolad IS very_old) THEN (result_4 IS Sepahan_win)",
        "IF (age_goalkeeper_Foolad IS very_old) AND (age_center_forward_Sepahan IS middle_age) THEN (result_4 IS Sepahan_win)",
        "IF (age_goalkeeper_Sepahan IS very_old) AND (age_center_forward_Foolad IS young) THEN (result_4 IS Foolad_win)",
        "IF (price_goalkeeper_Foolad IS normal) AND (price_center_forward_Sepahan IS expensive) THEN (result_4 IS Sepahan_win)",
        "IF (price_goalkeeper_Sepahan IS normal) AND (price_center_forward_Foolad IS expensive) THEN (result_4 IS Foolad_win)"       
]

# Q2_graded

Rules5 = [
        "IF (age_mid_difender_1_Foolad IS young) AND (age_mid_difender_2_Foolad IS young) AND (age_center_forward_Sepahan IS very_old) THEN (result_5 IS Foolad_win)",
        "IF (age_mid_difender_1_Sepahan IS young) AND (age_mid_difender_2_Sepahan IS young) AND (age_center_forward_Foolad IS very_old) THEN (result_5 IS Sepahan_win)",
        "IF (age_mid_difender_1_Foolad IS very_old) AND (age_mid_difender_2_Foolad IS middle_age) AND (age_center_forward_Sepahan IS young) THEN (result_5 IS Sepahan_win)",
        "IF (age_mid_difender_1_Sepahan IS old) AND (age_mid_difender_2_Sepahan IS young) AND (age_center_forward_Foolad IS old) THEN (result_5 IS Sepahan_win)",
        "IF (age_mid_difender_1_Sepahan IS old) AND (age_mid_difender_2_Sepahan IS old) AND (age_center_forward_Foolad IS middle_age) THEN (result_5 IS Foolad_win)",

        "IF (age_left_difender_Foolad IS young) AND (age_right_forward_Sepahan IS very_old) THEN (result_5 IS Foolad_win)",
        "IF (age_left_difender_Sepahan IS young) AND (age_right_forward_Foolad IS very_old) THEN (result_5 IS Sepahan_win)",
        "IF (age_left_difender_Foolad IS very_old) AND (age_right_forward_Sepahan IS young) THEN (result_5 IS Sepahan_win)",
        "IF (age_left_difender_Sepahan IS old) AND (age_right_forward_Foolad IS old) THEN (result_5 IS Sepahan_win)",
        "IF (age_left_difender_Sepahan IS old) AND (age_right_forward_Foolad IS middle_age) THEN (result_5 IS Foolad_win)",

        "IF (age_right_difender_Foolad IS young) AND (age_left_forward_Sepahan IS very_old) THEN (result_5 IS Foolad_win)",
        "IF (age_right_difender_Sepahan IS young) AND (age_left_forward_Foolad IS very_old) THEN (result_5 IS Sepahan_win)",
        "IF (age_right_difender_Foolad IS very_old) AND (age_left_forward_Sepahan IS young) THEN (result_5 IS Sepahan_win)",
        "IF (age_right_difender_Sepahan IS old) AND (age_left_forward_Foolad IS old) THEN (result_5 IS Sepahan_win)",
        "IF (age_right_difender_Sepahan IS old) AND (age_left_forward_Foolad IS middle_age) THEN (result_5 IS Foolad_win)",

        "IF (price_mid_difender_1_Foolad IS expensive) AND (price_mid_difender_2_Foolad IS expensive) AND (price_center_forward_Sepahan IS very_cheap) THEN (result_5 IS Foolad_win)",
        "IF (price_mid_difender_1_Sepahan IS expensive) AND (price_mid_difender_2_Sepahan IS expensive) AND (price_center_forward_Foolad IS very_cheap) THEN (result_5 IS Sepahan_win)",
        "IF (price_mid_difender_1_Foolad IS very_cheap) AND (price_mid_difender_2_Foolad IS normal) AND (price_center_forward_Sepahan IS expensive) THEN (result_5 IS Sepahan_win)",
        "IF (price_mid_difender_1_Sepahan IS cheap) AND (price_mid_difender_2_Sepahan IS expensive) AND (price_center_forward_Foolad IS cheap) THEN (result_5 IS Sepahan_win)",
        "IF (price_mid_difender_1_Sepahan IS cheap) AND (price_mid_difender_2_Sepahan IS cheap) AND (price_center_forward_Foolad IS normal) THEN (result_5 IS Foolad_win)",
        
        "IF (price_left_difender_Foolad IS expensive) AND (price_right_forward_Sepahan IS very_cheap) THEN (result_5 IS Foolad_win)",
        "IF (price_left_difender_Sepahan IS expensive) AND (price_right_forward_Foolad IS very_cheap) THEN (result_5 IS Sepahan_win)",
        "IF (price_left_difender_Foolad IS very_cheap) AND (price_right_forward_Sepahan IS expensive) THEN (result_5 IS Sepahan_win)",
        "IF (price_left_difender_Sepahan IS cheap) AND (price_right_forward_Foolad IS cheap) THEN (result_5 IS Sepahan_win)",
        "IF (price_left_difender_Sepahan IS cheap) AND (price_right_forward_Foolad IS normal) THEN (result_5 IS Foolad_win)",

        "IF (price_right_difender_Foolad IS expensive) AND (price_left_forward_Sepahan IS very_cheap) THEN (result_5 IS Foolad_win)",
        "IF (price_right_difender_Sepahan IS expensive) AND (price_left_forward_Foolad IS very_cheap) THEN (result_5 IS Sepahan_win)",
        "IF (price_right_difender_Foolad IS very_cheap) AND (price_left_forward_Sepahan IS expensive) THEN (result_5 IS Sepahan_win)",
        "IF (price_right_difender_Sepahan IS cheap) AND (price_left_forward_Foolad IS cheap) THEN (result_5 IS Sepahan_win)",
        "IF (price_right_difender_Sepahan IS cheap) AND (price_left_forward_Foolad IS normal) THEN (result_5 IS Foolad_win)",
        
]

# Q2_graded

Rules6 = [
        "IF (performance_Foolad IS bad) THEN (result_6 IS Sepahan_win)",
        "IF (performance_Sepahan IS good) THEN (result_6 IS Sepahan_win)",
        "IF (performance_Foolad IS bad) AND (performance_Sepahan IS bad) THEN (result_6 IS tie)",
        "IF (performance_Foolad IS medium) AND (performance_Sepahan IS medium) THEN (result_6 IS tie)"
]

# Q2_graded

FS.add_rules(Rules1 + Rules2 + Rules3 + Rules4 + Rules5 + Rules6, verbose=True)

# Q2_graded

FS.set_variable("performance_Sepahan", 4) 
FS.set_variable("performance_Foolad", 3) 

FS.set_variable("price_goalkeeper_Foolad", 270)
FS.set_variable("age_goalkeeper_Foolad", 27)

FS.set_variable("price_left_difender_Foolad", 338)
FS.set_variable("age_left_difender_Foolad", 23)

FS.set_variable("price_right_difender_Foolad", 428)
FS.set_variable("age_right_difender_Foolad", 24)

FS.set_variable("price_mid_difender_1_Foolad", 405)
FS.set_variable("age_mid_difender_1_Foolad", 25)

FS.set_variable("price_mid_difender_2_Foolad", 383)
FS.set_variable("age_mid_difender_2_Foolad", 22)

FS.set_variable("price_mid_fielder_1_Foolad", 225)
FS.set_variable("age_mid_fielder_1_Foolad", 32)

FS.set_variable("price_mid_fielder_2_Foolad", 225)
FS.set_variable("age_mid_fielder_2_Foolad", 29)

FS.set_variable("price_mid_fielder_3_Foolad", 585)
FS.set_variable("age_mid_fielder_3_Foolad", 29)

FS.set_variable("price_right_forward_Foolad", 496)
FS.set_variable("age_right_forward_Foolad", 28)

FS.set_variable("price_left_forward_Foolad", 405)
FS.set_variable("age_left_forward_Foolad", 22)

FS.set_variable("price_center_forward_Foolad", 405)
FS.set_variable("age_center_forward_Foolad", 31)


# ==========================

FS.set_variable("price_goalkeeper_Sepahan", 405)
FS.set_variable("age_goalkeeper_Sepahan", 33)

FS.set_variable("price_left_difender_Sepahan", 1080)
FS.set_variable("age_left_difender_Sepahan", 25)

FS.set_variable("price_right_difender_Sepahan", 698)
FS.set_variable("age_right_difender_Sepahan", 29)

FS.set_variable("price_mid_difender_1_Sepahan", 450)
FS.set_variable("age_mid_difender_1_Sepahan", 29)

FS.set_variable("price_mid_difender_2_Sepahan", 315)
FS.set_variable("age_mid_difender_2_Sepahan", 31)

FS.set_variable("price_mid_fielder_1_Sepahan", 585)
FS.set_variable("age_mid_fielder_1_Sepahan", 20)

FS.set_variable("price_mid_fielder_2_Sepahan", 495)
FS.set_variable("age_mid_fielder_2_Sepahan", 29)

FS.set_variable("price_mid_fielder_3_Sepahan", 450)
FS.set_variable("age_mid_fielder_3_Sepahan", 32)

FS.set_variable("price_right_forward_Sepahan", 563)
FS.set_variable("age_right_forward_Sepahan", 29)

FS.set_variable("price_left_forward_Sepahan", 270)
FS.set_variable("age_left_forward_Sepahan", 33)

FS.set_variable("price_center_forward_Sepahan", 540)
FS.set_variable("age_center_forward_Sepahan", 27)



res = FS.inference()

# Q2_graded

# dar sorati score ra dar nazar migirim ke kochektar az -1 ya bozorgtar az 1 bashad

Sepahan_score = 0
Foolad_score = 0

for i in range(1,7):
    if res[f"result_{i}"] < -1:
        Sepahan_score += 1
    elif res[f"result_{i}"] > 1:
        Foolad_score += 1

print(f"This matche's score is Sepahan {Sepahan_score}-{Foolad_score} Foolad")

