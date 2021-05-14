query_template_product_typeID = """INSERT INTO "ship_o_cereal_products_typeId" ("products_id","producttypes_id") VALUES({P},1);\n"""
with open('populate_product_typeid.txt', 'w+') as PC:
    for i in range(39,79):
        query = query_template_product_typeID.format(P=i)
        PC.write(query)