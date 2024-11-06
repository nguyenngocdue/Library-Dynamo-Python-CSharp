

el_ref = sel1.PickObjects(ot1, "Select model elements") 
typelist = list() 
idlist = list() 
Elements=[] 
for i in el_ref: 
    typelist.append(doc.GetElement(i.ElementId)) 
OUT = typelist