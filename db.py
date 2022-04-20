from app import db, City

db.create_all()

# vilnius = City("Vilnius", 544386, "Lithuania")
# kaunas = City("Kaunas", 295269, "Lithuania")
# panevezys = City("Panevėžys", 85885, "Lithuania")
# siauliai = City("Šiauliai", 101511, "Lithuania")
# klaipeda = City("Klaipėda", 152818, "Lithuania")
#
# db.session.add_all([vilnius, kaunas, panevezys, siauliai, klaipeda])
# db.session.commit()
#
# print(vilnius.id, kaunas.id, panevezys.id, siauliai.id, klaipeda.id)

alytus = City("Alytus", 49195, "Lithuania", "1377")
balberiskis = City("Balbieriškis", 966, "Lithuania", "")

db.session.add_all([alytus, balberiskis])
db.session.commit()
