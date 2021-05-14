cereal = ["Cheerios","Cinnamon Toast Crunch","Wheaties","Frosted Mini-Wheats","Honey Nut Cheerios","Apple Jacks"
,"Rice Krispies","Lucky Charms","Raisin Bran","Count Chocula!","Corn Pops","Honey Smacks","Golden Grahams"
,"Alpha-Bits","Froot Loops",'Cracklin" Oat Bran',"Kix","Life","Frosted Flakes",'Honey Graham Oh"s'
,"Cinnamon Life","Cocoa Krispies","Rice Krispies Treats Cereal","Crispix","Go Lean! Crunch","Corn Flakes"
,"Golden Crisp","Fruity Pebbles",'Cap"n Crunch With Crunch Berries',"Product 19","Raisin Bran Crunch"
,"Quaker Oatmeal Squares - Brown Sugar","Weetabix","Honey Bunches of Oats With Almonds","Rice Chex","Cocoa Dyno-Bites"
,'Reese"s Peanut Butter Puffs"',"Cookie Crisp","Apple Cinnamon Cheerios","Honeycomb"]

price = [1300,2800,1200,1300,800,600,2300,2100,1100,2000,2100,700,1200,1500,700,2000,2400,1800,2400,1500,1900,1700,2400,2600,900,1100,700,2600,2300,600,1000,700,1900,1900,2300,600,1000,700,1900,1900,2300,1500,1700,1700,1600,1200]

image=["1_cheerios.jpg","2_cinnamon_toast_crunch.jpg","3_wheaties.jpg","4_frosted_miniwheats.jpg","5_honey_nut_cheerios.jpg","6_apple_jacks.jpg","7_rice_krispies.jpg","8_lucky_charms.jpg","9_raisin_bran.jpg","10_count_chocula.jpg","11_corn_pops.jpg","12_honey_smacks.jpg","13_golden_grahams.jpg","14_alphabits.jpg",
"15_froot_loops.jpg","16_cracklin_oat_bran.jpg","17_kix.jpg","18_life.jpg","19_frosted_flakes.jpg","20_honey_graham_ohs.jpg","21_cinnamon_life.jpg","22_cocoa_krispies.jpg","23_rice_krispies_treats_cereal.jpg","24_crispix.jpg","25_go_lean_crunch.jpg","26_corn_flakes.jpg","27_golden_crisp.jpg","28_fruity_pebbles.jpg",
"29_capn_crunch_with_crunch_berries.jpg","30_product_19.jpg","31_raisin_bran_crunch.jpg","32_quaker_oatmeal_squares__brown_sugar.jpg","33_weetabix.jpg","34_honey_bunches_of_oats_with_almonds.jpg","35_rice_chex.jpg","36_cocoa_dynobites.jpg","37_reeses_peanut_butter_puffs.jpg","38_cookie_crisp.jpg","39_apple_cinnamon_cheerios.jpg"
,"40_honeycomb.jpg"]

stock = [4393,3034,507,2103,2430,2245,3172,3988,1413,4453,4798,4102,1232,4270,2971,3839,4483,1547,3386,2582,2362,1053,3678,500,1018,1420,2827,4417,1743,4524,1209,
2945,1998,525,3067,3467,2019,2104,756,3350]


import string
result = string.punctuation

count = 1
for name in cereal:
    for letter in name:
        if letter in result:
            name = name.replace(letter, "")
        elif letter == " ":
            name = name.replace(letter, "_")
    image.append("'"+str(count)+"_"+name.lower()+".jpg"+"'")
    count+=1



query_template_product = """INSERT INTO ship_o_cereal_products ("name","description","image","price","stock","isFood") VALUES('{N}','Morgunkorn sem allir elska','{I}',{P},{S},True);\n"""
with open('populate_product.txt', 'w+') as PC:
    for i in range(40):
        query = query_template_product.format(N=cereal[i],I=image[i],P=price[i],S=stock[i])
        PC.write(query)