import d

def gofirst():
    d.draw(5)

def intothevoid():
    if len(d.hand) > 2 and "93946239" in d.hand:
        d.hand.remove("93946239")
        d.draw(1)

def upstart():
    if "70368879" in d.hand:
        d.hand.remove("70368879")
        d.draw(1)

def potofdesires():
    if "35261759" in d.hand:
        d.hand.remove("35261759")
        d.banish(10)
        d.draw(2)

def allureofdarkness():
    if "01475311" in d.hand and ("35618217" or "50546208" or "14152693" or "52350806" or "70711847" or "16209941" \
            or "97631303" or "13893596" or "43694650" or "14785765"):
        d.draw(2)
        d.hand.remove("01475311")

        if d.hand.count("97631303") > 1 and ("97631303" in d.mfield and "97631303" in d.grave  or "13893596" not in d.deck):
            d.hand.remove("97631303")
        elif "35618217" in d.mfield or "35618217" in d.grave or d.hand.count("35618217") > 1:
            d.hand.remove("35618217")
        elif d.hand.count("52350806") > 1:
            d.hand.remove("52350806")
        elif d.hand.count("70711847") > 1:
            d.hand.remove("70711847")
        elif d.hand.count("43694650") > 1:
            d.hand.remove("43694650")
        elif "50546208" in d.hand:
            d.hand.remove("50546208")
        elif "14152693" in d.hand:
            d.hand.remove("14152693")
        elif "13893596" in d.hand:
            d.hand.remove("13893596")
        elif "16209941" in d.hand:
            d.hand.remove("16209941")
        elif "52350806" in d.hand:
            d.hand.remove("52350806")
        elif "43694650" in d.hand:
            d.hand.remove("43694650")
        elif "70711847" in d.hand:
            d.hand.remove("70711847")
        elif "35618217" in d.hand:
            d.hand.remove("35618217")
        elif "14785765" in d.hand:
            d.hand.remove("14785765")
        elif "14785765" in d.hand:
            d.hand.remove("14785765")
        elif "97631303" in d.hand:
            d.hand.remove("97631303")

def tenki():
    if "57103969" in d.hand:
        d.hand.remove("57103969")
        if ("83190280" in d.hand or "83190280" in d.pendzone) and "35618217" in d.deck :
            d.deck.remove("35618217")
            d.hand.append("35618217")

        elif ("35618217" in d.mfield or "35618217" in d.grave or d.hand.count("35618217") > 0) and "83190280" in d.deck:
            d.deck.remove("83190280")
            d.hand.append("83190280")

def foolishgoods():

    if "83190280" in d.hand and "48444114" in d.deck:
        # add discard here
        d.hand.remove("83190280")

        if ("83190280" in d.hand or "83190280" in d.pendzone) and "35618217" in d.deck :
            d.deck.remove("35618217")
            d.hand.append("35618217")
        elif ("35618217" in d.mfield or "35618217" in d.grave or d.hand.count("35618217") > 0) and "83190280" in d.deck:
            d.hand.append("83190280")
            d.deck.remove("83190280")




def magicianssouls():
    if "97631303" in d.hand and "13893596" in d.deck:
        d.send("13893596")
        d.mfield.append("97631303")
        d.hand.remove("97631303")


gofirst()

for i in range(6):
    magicianssouls()
    upstart()
    intothevoid()
    potofdesires()
    tenki()
    foolishgoods()
    allureofdarkness()

print(d.deck)
print(d.hand)
print(d.banished)
print(d.grave)
print(d.mfield)