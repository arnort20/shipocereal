
missing_ingredients = [
    "Sugar, Whole Grains (Corn, Oats, and Rice) and Corn Flour, Modified Corn Starch, Cocoa, Canola and/or Rice Bran Oil, Corn Syrup, Cocoa Processed with Alkali, Salt, Calcium Carbonate, Caramel and Beet Juice Concentrate Color, Tricalcium Phosphate, Trisodium Phosphate, Zinc and Iron, Artificial Flavor, Vitamin C, Niacinamide, Vitamin B6, Vitamin B2, Vitamin B1, Folic Acid, Vitamin B12, Wheat Starch, Vitamin E and BHT to preserve freshness."
]
theids = [1,2,3,4,5,6,8,9,10,11,7]

ingredients = [
"whole Grain Oats, Corn Starch, Sugar, Salt, Tripotassium Phosphate. Vitamin E (mixed tocopherols) Added to Preserve Freshness",
"whole Grain Wheat, Sugar, Rice Flour, Canola and/or Rice Bran Oil, Fructose, Maltodextrin, Dextrose, Salt, Cinnamon, Soy Lecithin, Trisodium Phosphate, Color Added. BHT Added to Preserve Freshness",
"""whole Grain Wheat, Crisp Rice (Rice Flour, Salt, Malt Extract), Sugar, Whole Grain Oats, Corn Bran, Honey, Canola Oil, Maltodextrin, Wheat Bran, Corn Starch, Brown Sugar Syrup, Salt,Cinnamon, Barley Malt Extract, Corn Syrup Solids, Color Added, Guar Gum, Cellulose Gum, Soy Lecithin, Artificial Flavor, Baking Soda, Trisodium Phosphate, Corn Oil, Vitamin E (Mixed Tocopherols) and BHT Added to Preserve Freshness, Vitamins and Minerals: Calcium Carbonate, Vitamin E Acetate, a B Vitamin (Niacinamide), Vitamin C (Sodium Ascorbate), Iron (a Mineral Nutrient), Vitamin B6 (Pyridoxine Hydrochloride), Vitamin B2 (Riboflavin), Vitamin B1 (Thiamin Mononitrate), Vitamin A (Palmitate), Vitamin B12, Vitamin D3.""",
"whole grain wheat, sugar, contains 2% or less of brown rice syrup, gelatin, BHT for freshness, Vitamins and Minerals: Reduced Iron, folic acid",
"""whole grain oats, sugar, corn starch, honey, brown sugar syrup, salt, tripotassium phosphate, canola oil, natural almond flavor. vitamin e (mixed tocopherols) added to preserve freshness. vitamins and minerals: calcium carbonate, vitamin c (sodium ascorbate), iron and zinc (mineral nutrients), a b vitamin (niacinamide), vitamin b6 (pyridoxine hydrochloride), vitamin b1 (thiamin mononitrate), vitamin a (palmitate), vitamin b2 (riboflavin), a b vitamin (folic acid), vitamin b12, vitamin d3.""",
"""sugar, whole grain corn flour, wheat flour, whole grain oat flour, oat fiber, soluble corn fiber, salt, milled corn, dried apples, apple juice concentrate, cornstarch, cinnamon, natural and artificial flavor, sodium ascorbate, ascorbic acid, modified corn starch, yellow #6, niacinamide, reduced iron, zinc oxide, turmeric color, baking soda, pyridoxine hydrochloride, blue #1, calcium phosphate, riboflavin, thiamin hydrochloride, red #40, vitamin a palmitate, bht, folic acid, vitamin d, vitamin b12.""",
"""rice, sugar, contains 2% or less of salt, malt flavor. vitamins and minerals: iron, vitamin c (ascorbic acid), vitamin e (alpha tocopherol acetate), niacinamide, vitamin a palmitate, vitamin b6 (pyridoxine hydrochloride), vitamin b2 (riboflavin), vitamin bi (thiamin hydrochloride), folic acid, vitamin b12, vitamin d.""",
"""Whole Grain Oats, Marshmallows (Sugar, Modified Corn Starch, Corn Syrup, Dextrose, Gelatin, Calcium Carbonate, Yellows 5 & 6, Blue 1, Red 40, Artificial Flavor), Sugar, Oat Flour, Corn Syrup, Corn Starch, Salt, Trisodium Phosphate, Color Added, Artificial Flavor, Vitamin E (Mixed Tocopherols) Added to Preserve Freshness. Vitamins and Minerals: Calcium Carbonate, Zinc and Iron (Mineral Nutrients), Vitamin C (Sodium Ascorbate), a B Vitamin (Niacinamide), Vitamin B6 (Pyridoxine Hydrochloride), Vitamin B2 (Riboflavin), Vitamin B1 (Thiamin Mononitrate), Vitamin A (Palmitate), a B Vitamin (Folic Acid), Vitamin B12, Vitamin D3.""",
"""Whole Wheat, Raisins, Wheat Bran, Sugar, High Fructose Corn Syrup, Salt, Malt Flavoring, Niacinamide, Reduced Iron, Zinc Oxide, Pyridoxine Hydrochloride (Vitamin B6), Riboflavin (Vitamin B2), Thiamin Hydrochloride (Vitamin B1), Vitamin A Palmitate, Folic Acid, Vitamin B12 and Vitamin D.""",
"""Whole Grain Corn, Sugar, Marshmallows (Sugar, Modified Corn Starch, Corn Syrup, Dextrose, Gelatin, Red 40, Yellows 5 & 6, Blue 1, Natural and Artificial Flavor), Corn Meal, Corn Starch, Canola and/or Rice Bran Oil, Corn Syrup, Cocoa Processed with Alkali, Salt, Tricalcium Phosphate, Red 40, Yellows 5 & 6, Blue 1 and Other Color Added, Natural and Artificial Flavor, Trisodium Phosphate, BHT Added to Preserve Freshness. Vitamins and Minerals: Calcium Carbonate, Zinc and Iron (Mineral Nutrients), Vitamin C (Sodium Ascorbate), a B Vitamin (Niacinamide), Vitamin B6 (Pyridoxine Hydrochloride), Vitamin B2 (Riboflavin), Vitamin B1 (Thiamin Mononitrate), Vitamin A (Palmitate), a B Vitamin (Folic Acid), Vitamin B12, Vitamin D3.""",
"""Milled Corn, Sugar, Corn Syrup, Molasses, Salt, Partially Hydrogenated Vegetable Oil (One or More of: Coconut, Cottonseed, and Soybean) (Adds a Negligible Amount of Fat.) (Less than 0.5 g Trans Fat per Serving.), Sodium Ascorbate and Ascorbic Acid (Vitamin C), Niacinamide, Reduced Iron, Zinc Oxide, Wheat Starch, Pyridoxine Hydrochloride (Vitamin B6), Riboflavin (Vitamin B2), Thiamin Hydrochloride (Vitamin B1), Annatto Color, Vitamin A Palmitate, BHT (Preservative), Folic Acid, Vitamin B12 and Vitamin D.""",
"whole grain wheat, sugar, glucose syrup, honey, palm oil.",
"""Whole grain wheat, corn meal, sugar, brown sugar syrup, canola and/or rice bran oil, dextrose, baking soda, salt, natural flavor. Calcium carbonate, zinc and iron (mineral nutrients), vitamin C (sodium ascorbate), A B vitamin (niacinamide), vitamin b6 (pyridoxine hydrochloride), vitamin B2 (riboflavin), vitamin b1 (thiamin mononitrate), vitamin A (palmitate), A B vitamin (folic acid), vitamin b12, vitamin d3.""",
"""whole grain oat flour, sugar, wheat starch, calcium carbonate, salt, trisodium phosphate, natural flavor, annatto (color), bht added to preserve freshness. vitamins and minerals: ferric orthophosphate (source of iron), niacinamide (vitamin b3), zinc oxide, thiamin mononitrate (vitamin b1), calcium pantothenate (vitamin b5), pyridoxine hydrochloride (vitamin b6), folic acid.""",
"""Sugar, corn flour blend (whole grain yellow corn flour, degerminated yellow corn flour), wheat flour, whole grain oat flour, oat fiber, modified food starch, soluble corn fiber, contains 2% or less of hydrogenated vegetable oil (coconut, soybean and/or cottonseed), salt, natural flavor, red 40, turmeric extract color, yellow 6, blue 1, annatto extract color, BHT for freshness.Vitamins and Minerals: Vitamin C (sodium ascorbate and ascorbic acid), niacinamide, reduced iron, zinc oxide, vitamin B6 (pyridoxine hydrochloride), vitamin B2 (riboflavin), vitamin B1 (thiamin hydrochloride), vitamin A palmitate, folic acid, vitamin B12, vitamin D3.""",
"""whole grain oats, sugar, wheat bran, palm oil, oat bran, corn syrup, wheat starch, coconut, contains 2% or less of molasses, cinnamon, malt extract, natural flavor, salt, soy lecithin, nutmeg. vitamins and minerals: reduced iron, niacinamide, vitamin b1 (thiamin hydrochloride), vitamin b6 (pyridoxine hydrochloride), vitamin b2 (riboflavin), folic acid, vitamin d3, vitamin b12.""",
"""Whole grain corn, corn meal, sugar, salt, brown sugar syrup, baking soda, vitamin E (mixed tocopherols) added to preserve freshness. Vitamins and minerals: calcium carbonate, iron and zinc (mineral nutrients), vitamin C (sodium ascorbate), a b vitamin (niacinamide), vitamin b6 (pyridoxine hydrochloride), vitamin b2 (riboflavin), vitamin b1 (thiamin mononitrate), vitamin a (palmitate), a b vitamin (folic acid), vitamin b12, vitamin d3.""",
"whole grain oat flour, sugar, corn flour, whole wheat flour, rice flour, calcium carbonate, salt, cinnamon, disodium phosphate, caramel color, reduced iron, yellow 6, niacinamide*, bht (to preserve freshness), yellow 5, red 40, natural flavor, thiamine mononitrate*, pyridoxine hydrochloride*, riboflavin*. blue 1, folic acid*. *one of the b vitamins.",
"milled corn, sugar, contains 2% or less of malt flavor, salt, bht for freshness. vitamins and minerals: iron, vitamin c (ascorbic acid and sodium ascorbate), niacinamide, vitamin b (pyridoxine hydrochloride), vitamin b2 (riboflavin), vitamin b, (thiamin hydrochloride), vitamin a palmitate, folic acid, vitamin d, vitamin b12. corn used in this product",
"""corn flour, sugar, whole grain oat fiber, molasses, canola oil, rice flour, salt, corn syrup, milled corn, honey, palm oil, baking soda, paprika extract (for color), caramel color, artificial flavor, yellow 5, yellow 6, bht added to preserve freshness. Vitamins and minerals: ferric orthophosphate (source of iron), niacinamide (vitamin b3), zinc oxide, thiamin mononitrate (vitamin b1), calcium pantothenate (vitamin b5), pyridoxine hydrochloride (Vitamin b6), folic acid.""",
"whole grain oat flour, sugar, corn flour, whole wheat flour, rice flour, calcium carbonate, salt, cinnamon, disodium phosphate, caramel color, reduced iron, yellow 6, niacinamide*, bht (to preserve freshness), yellow 5, red 40, natural flavor, thiamine mononitrate*, pyridoxine hydrochloride*, riboflavin*. blue 1, folic acid*. *one of the b vitamins.",
"""Rice, Sugar, Cocoa (Treated with Alkali), Semisweet Chocolate (Sugar, Chocolate, Dextrose), Partially Hydrogenated Vegetable Oil (One or More of: Coconut, Cottonseed and Soybean) (Less than 0.5 g Trans Fat Per Serving), Salt, Malt Flavoring, Calcium Carbonate, High Fructose Corn Syrup, Ascorbic Acid, and Sodium Ascorbate (Vitamin C), Iron, Niacinamide, Artificial Flavor, Zinc Oxide, Pyridoxine Hydrochloride (Vitamin B6), Riboflavin (Vitamin B2), Thiamin Hydrochloride (Vitamin B1), Vitamin A Palmitate, Folic Acid, BHT (Preservative), Vitamin D and Vitamin B12.""",
"rice, sugar, contains 2% or less of salt, malt flavor. vitamins and minerals: iron, vitamin c (ascorbic acid), vitamin e (alpha tocopherol acetate), niacinamide, vitamin a palmitate, vitamin b6 (pyridoxine hydrochloride), vitamin b2 (riboflavin), vitamin bi (thiamin hydrochloride), folic acid, vitamin b12, vitamin d.",
"rice, milled corn, sugar, contains 2% or less of salt, molasses, brown rice syrup, baking soda, turmeric extract color. vitamins and minerals: iron (ferric phosphate), niacinamide, vitamin b6 (pyridoxine hydrochloride), vitamin b2 (riboflavin), vitamin b1 (thiamin hydrochloride), folic acid, vitamin d3. vitamin b12.",
"kashi seven whole grains and sesame blend (whole: hard red wheat, brown rice, barley, triticale, oats, rye, buckwheat, sesame seeds), soy flakes, brown rice syrup, dried cane syrup, chicory root fiber (inulin), whole grain oats, expeller pressed canola oil, honey, salt, cinnamon, mixed tocopherols for freshness.",
"milled corn, sugar, malt flavor, contains 2% or less of salt. vitamins and minerals: iron, vitamin c (sodium ascorbate, ascorbic acid), niacinamide, vitamin 86 (pyridoxine hydrochloride), vitamin b2 (riboflavin), vitamin b1 (thiamin hydrochloride), vitamin a palmitate, folic acid, vitamin d, vitamin b12. corn used in this product",
"sugar, wheat, corn syrup, salt, honey, caramel color. vitamins and minerals: thiamin mononitrate (vitamin b1), calcium pantothenate (vitamin 85), folic acid.",
"rice, sugar, canola oil, salt, natural and artificial flavor, red 40, yellow 6, yellow 5, turmeric oleoresin (color), blue 1, blue 2, bht and bha added to preserve freshness. vitamins and minerals: sodium ascorbate and ascorbic acid (vitamin c), niacinamide (vitamin b3), reduced iron, zinc oxide, vitamin a palmitate, pyridoxine hydrochloride (vitamin b6), thiamin mononitrate (vitamin b1), riboflavin (vitamin b2), folic acid, vitamin d3, vitamin b12.",
"Corn Flour, Sugar, Oat Flour, Brown Sugar, Palm and/or Coconut Oil, Salt, Sodium Citrate, Natural and Artificial Flavor, Strawberry Juice Concentrate, Red 40, Reduced Iron, Yellow 5, Niacinamide*, Malic Acid, Zinc Oxide, Blue 1, Yellow 6, Thiamin Mononitrate*, Riboflavin*, BHT (a preservative), Pyridoxine Hydrochloride*, Folic Acid*.",
"rispy flakes of multi-grain toasted corn, oats, wheat, and rice",
"Whole grain wheat, sugar, rice, raisins, wheat bran, whole grain oats, brown sugar syrup, vegetable glycerin. Contains 2% or less of corn syrup, salt, natural flavor, modified corn starch, molasses, palm oil, cinnamon, honey, mixed tocopherols (vitamin E) for freshness.",
"whole grain oat flour, whole wheat flour, brown sugar, sugar, maltodextrin, malted barley extract, natural flavor, salt, baking soda, tocopherols (to preserve freshness). vitamins & minerals: reduced iron, folic acid.",
"wheat, organic barley malt extract, organic cane sugar, sea salt.",
"corn, whole grain wheat, sugar, whole grain rolled oats, almonds, rice, canola oil, wheat flour, malted barley flour, corn syrup, salt, molasses, honey, caramel color, barley malt extract, cinnamon, natural and artificial flavor, annatto extract (color). bht added to preserve freshness. vitamins and minerals: reduced iron, niacinamide (vitamin b3), vitamin a palmitate, pyridoxine hydrochloride (vitamin b6), zinc oxide, (vitamin b1), riboflavin (vitamin b2), folic acid, vitamin d3, vitamin b12.",
"whole grain rice, rice, sugar, salt, molasses. vitamin e (mixed tocopherols) added to preserve freshness. vitamins and minerals: calcium carbonate, iron and zinc (mineral nutrients), vitamin c (sodium ascorbate), a b vitamin (niacinamide), vitamin b6 (pyridoxine hydrochloride), vitamin b1 (thiamin mononitrate), vitamin a (palmitate), vitamin b2 (riboflavin), a b vitamin (folic acid), vitamin b12, vitamin d3.",
"rice, sugar, cocoa (processed with alkali), canola oil, salt, caramel color, natural flavor, rosemary extract (antioxidant). vitamins and minerals: reduced iron, zinc oxide, thiamin mononitrate (vitamin b1), calcium pantothenate (vitamin b5), folic acid.",
'whole grain corn, sugar, reese"s peanut butter (peanuts, sugar, monoglycerides, peanut oil, salt, molasses, corn starch), dextrose, corn meal, corn syrup, canola oil, salt',
"whole grain corn, sugar, corn meal, yellow corn flour, canola oil, corn syrup, cocoa processed with alkali, brown sugar syrup, salt, caramel color, baking soda, natural flavor. vitamins and minerals: calcium carbonate, tricalcium phosphate, iron and zinc (mineral nutrients), vitamin c (sodium ascorbate), a b vitamin (niacinamide), vitamin b: (pyridoxine hydrochloride), vitamin b2 (riboflavin), vitamin b, (thiamin mononitrate), vitamin a (palmitate), a b vitamin (folic acid), vitamin b12, vitamin d3.",
'whole grain oats, sugar, corn starch, apple puree concentrate, corn syrup, canola oil, refiner"s syrup, salt, cinnamon, trisodium phosphate. vitamin e (mixed tocopherols) added to preserve freshness. vitamins and minerals: calcium carbonate, vitamin c (sodium ascorbate), iron and zinc (mineral nutrients). a b vitamin (niacinamide). vitamin b6 (pyridoxine hydrochloride), vitamin b1 (thiamin mononitrate), vitamin a (palmitate), vitamin b2 (riboflavin), a b vitamin (folic acid). vitamin b12, vitamin d3.',
"whole grain corn flour, sugar, whole grain oat flour, corn flour, honey, salt, natural andartificial flavour, colour, wheat starch, bht added to preserve freshness."]


labels = ["calories","fat","carbs","protein"]
nutriens = [[15.83,42.82,27.17,39.56]
,[29.25,44.9,49.25,48.63]
,[41.96,16.56,17.24,35.85]
,[48.11,32.57,20.88,38.95]
,[18.09,26.24,40.01,8.67]
,[31.98,38.93,13.84,37.4]
,[25.74,5.9,20.48,14.36]
,[26.25,9.34,36.74,44.93]
,[34.32,6.59,7.4,10.71]
,[45.39,48.97,11.43,24.58]
,[16.65,40.7,15.69,18.55]
,[29.42,7.26,45.44,23.33]
,[23.77,24.1,13.38,13.52]
,[45.35,26.23,47.22,29.15]
,[44.7,46.7,12.53,39.68]
,[25.71,27.75,18.59,40.82]
,[9.95,28.87,38.53,6.66]
,[34.73,28.63,14.74,21.2]
,[8.88,27.2,28.57,12.17]
,[33.22,10.39,8.04,39.83]
,[40.03,28.55,26.17,41.71]
,[6.04,21.77,33.77,15.31]
,[6.54,14.28,15.65,44.4]
,[28.21,28.88,31.61,22.86]
,[16.56,27.87,44.25,9.78]
,[45.44,8.84,21.88,29.7]
,[44.63,46.74,43.26,44.37]
,[9.52,47.78,25.2,10.12]
,[29.51,28.81,20.21,8.29]
,[5.06,32.17,14.75,45.6]
,[32.87,29.39,24.16,42.66]
,[29.69,42.88,47.38,49.17]
,[46.44,22.72,35.6,16.64]
,[16.1,16.9,16.44,24.58]
,[21.37,40.76,27.91,39.48]
,[21.88,15.21,23.91,39.8]
,[8.07,45.61,30.89,47.79]
,[9.23,29.16,19.4,47.88]
,[35.87,22.6,7.33,7.8]
,[30.61,35.55,48.2,11.61]
,[49.35,9.81,41.68,15.54]
,[28.2,45.12,17.61,21.63]
,[27.0,44.1,22.96,23.99]
,[47.01,21.91,30.33,41.59]
,[16.35,46.94,11.55,6.07]
,[42.96,32.07,21.53,36.71]
,[39.22,37.01,21.23,33.32]
,[11.58,16.2,13.81,6.09]
,[8.9,16.22,28.1,20.44]
,[10.72,19.36,14.93,35.35]
,[6.27,37.9,29.24,16.37]
,[28.2, 45.12, 17.61, 21.63]
,[27.0, 44.1, 22.96, 23.99]
,[47.01, 21.91, 30.33, 41.59]
,[6.27,37.9,29.24,16.37]
,[10.72,19.36,14.93,35.35]
]


cereal_ingredients = "Sugar, Whole Grains (Corn, Oats, and Rice) and Corn Flour, Modified Corn Starch, Cocoa, Canola and/or Rice Bran Oil, Corn Syrup, Cocoa Processed with Alkali, Salt, Calcium Carbonate, Caramel and Beet Juice Concentrate Color, Tricalcium Phosphate, Trisodium Phosphate, Zinc and Iron, Artificial Flavor, Vitamin C, Niacinamide, Vitamin B6, Vitamin B2, Vitamin B1, Folic Acid, Vitamin B12, Wheat Starch, Vitamin E and BHT to preserve freshness."
milk_ingredients = "water, fat, protein, sugar (lactose), minerals, vitamins and enzymes."
cereal_id = [1,2,3,4,5,6,7,8,9,10]
milk = [33,34,35,36,37,38]
new_cereal = range(39,79)
nutriens_counter = 0
ingredients_counter = 0

query_template_product_nutriens = """INSERT INTO "ship_o_cereal_nutrients" ("productId_id","calories","carbs","fat","ingredients","protein") VALUES({X},{K},{C},{F},'{I}',{P});"""

with open('populate_nutrients.txt','w') as PC:
    for x in cereal_id:
        query = query_template_product_nutriens.format(X=x,K=nutriens[nutriens_counter][0],C=nutriens[nutriens_counter][1],F=nutriens[nutriens_counter][2],I=cereal_ingredients,P=nutriens[nutriens_counter][3])
        PC.write(query)

        nutriens_counter +=1
        #print(query)
    for y in milk:
        query = query_template_product_nutriens.format(X=y, K=nutriens[nutriens_counter][0], C=nutriens[nutriens_counter][1],
                                                           F=nutriens[nutriens_counter][2], I=milk_ingredients,
                                                           P=nutriens[nutriens_counter][3])
        PC.write(query)
        nutriens_counter += 1
        #print(query)
    for z in new_cereal:
        query = query_template_product_nutriens.format(X=z, K=nutriens[nutriens_counter][0], C=nutriens[nutriens_counter][1],
                                                           F=nutriens[nutriens_counter][2], I=ingredients[ingredients_counter],
                                                           P=nutriens[nutriens_counter][3])
        PC.write(query)
        print(query)
        nutriens_counter += 1
        ingredients_counter += 1












