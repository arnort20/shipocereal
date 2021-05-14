query_template_product_manID = """INSERT INTO "ship_o_cereal_products_manId" ("products_id","manufacturers_id") VALUES({P},{M});\n"""
#"Kellogg's" = 1
#"General Mills" = 4
#"Quaker Oats Company" = 5
#"Post Foods" = 6
#"Kashi" = 7
#"Malt-O-Meal" = 8
#"Weetabix" = 9
productID = 39

manufactuer = ["General Mills","General Mills","General Mills","Kellogg's","General Mills","Kellogg's","Kellogg's"
,"General Mills","Kellogg's","General Mills","Kellogg's","Kellogg's","General Mills","Post Foods","Kellogg's","Kellogg's"
,"General Mills","Quaker Oats Company","Kellogg's","Quaker Oats Company","Quaker Oats Company","Kellogg's","Kellogg's"
,"Kellogg's","Kashi","Kellogg's","Post Foods","Post Foods","Quaker Oats Company","Kellogg's","Kellogg's","Quaker Oats Company"
,"Weetabix","Post Foods","General Mills","Malt-O-Meal","General Mills","General Mills","General Mills","Post Foods"]

with open('populate_product_manid.txt', 'w+') as PC:
    print('haha')
    for i in range(40):
        if manufactuer[i] == "Kellogg's":
            manid = 1
        elif manufactuer[i] == "General Mills":
            manid = 4
        elif manufactuer[i] == "Quaker Oats Company":
            manid = 5
        elif manufactuer[i] == "Post Foods":
            manid = 6
        elif manufactuer[i] == "Weetabix":
            manid = 9
        elif manufactuer[i] == "Kashi":
            manid = 7
        elif manufactuer[i] == "Malt-O-Meal":
            manid = 8
        query = query_template_product_manID.format(P=productID,M=manid)
        PC.write(query)
        productID += 1
