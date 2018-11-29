# coding=utf-8
import math
import string

#EF Function
#def f_ef(arg_assValue,arg_ef):
#    fefResult = (float(arg_ef)/100)float(arg_assValue))*
#    return fefResult

#SLE Function
def f_sle(arg_efval,arg_wholeAssValue):
    fv_ef = float(arg_efval)/float(100)
    fsleResult = (fv_ef)*(arg_wholeAssValue)
    return fsleResult

#Definiciones
vdefine_ef = "EF(EXPOSURE FACTOR)\nEs el porciento de perdia del valor de un activo \nfrente a la materialización de cierta amenaza.\n"
vdefine_sle = "SLE(SINGLE LOSS EXPENTACY)--\nEs el producto del EF y el valor total del activo.\n"
vdefine_aro = "ARO(ANUALIZED RATE OF OCURRENCE)\nEs la numero de veces en que podría presentarse\nla perdida entre el num de meses que podría suceder.\n"
vdefine_ale = "ALE(ANUALIZED LOSS EXPENTACY)\nEs el producto del SLE y el ARO\n"

#Imprime definiciones
print "----------------------------------"
print vdefine_ef
print "----------------------------------"
print vdefine_sle
print "----------------------------------"
print vdefine_aro
print "----------------------------------"
print vdefine_ale
print "----------------------------------"

#Calcular SLE
raw_input("Press enter to star calculations.. ")
print "\n***CALCULATE SINGLE LOSS EXPENTANCY***"

assetValue = input("--Enter the full value of the asset:> ")
ef_porcent = input("--Enter Exposure Factor Percentage:> ")
#print str("EF = ",(float("{0:.2f}".format(f_ef(ef_porcent,assetValue)))))
efvar = float(ef_porcent)/float(100)
print "SLE=(full asset value * EF)"
print "Asset Value = ",(str(assetValue))
print "EF=",efvar
print "SLE =",(str(assetValue))," x ",(str(efvar)),"=",(str(f_sle(ef_porcent,assetValue))),"\n"