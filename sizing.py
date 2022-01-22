# Parametres de la stratégie
# SL Fixe    (je trouve plus pertinent de définir un SL en fonction du dernier high/low du cours mais la c'est pour l exemple)
# TP calculé pour un RR (Risk Reward) de 2:1  je risque 1$ pour en gagner 2$  
# (c'est ce que je pratique generalement, avec un winrate de 40% t arrive a etre rentable)
# On peut partir sur un tp qui serait défini en fonction d'un autre paramètre cross ema ou autre
# Il ne sera donc pas inscrit dans les ordres ouverts mais executé lorsque les conditions sont presentes.

#Paramètres de base
capital_init = 100     #capital dédié au scalp
perte_max = 1   #exprimé en % perte maxi autorisé par trade 10$ dans notre cas
stop_loss = 1   #exprimé en % cas pour un stop loss fixe
rr = 5         #Risk Reward = % TP
levier = 2      #Levier utilisé

#Paramètres calculés
perte_maxcalc = perte_max / 100
perte_maxvalue = capital_init * perte_maxcalc
stop_losscalc = stop_loss / 100

# longIniPrice = round(row['close'],2)    A utilsier dans un bot
longIniPrice = 30000     #Pour exemple


#Pour un Long
stop_lossvalue =  round(longIniPrice * (1 - stop_losscalc),2)    #Stop Loss  exprime en dollar   ex pour le Btc, le round est a revoir pour les autres coins
risk_trade = abs(longIniPrice - stop_lossvalue)    #Perte maxi calculee exprime en dollar
max_amount = round((perte_maxvalue / risk_trade) * longIniPrice ,2)    #Taille maxi de la position exprime en $
max_qty = round((max_amount / longIniPrice) / levier ,3)    #qté du trade
take_profit = longIniPrice + ( risk_trade * rr )     #TP du trade
pertemax_recalc = (longIniPrice - stop_lossvalue ) * max_qty * levier
profit_recalc = (capital_init * (rr / 100)) + capital_init

print(f"Enter Price : {longIniPrice}")
print(f"Stop Loss : {stop_lossvalue}")
print(f"Take Profit : {take_profit}")
print(f"Valeur de la position du trade $ : {max_amount}")
print(f"Qté maxi du trade $ : {max_qty}")
print(f"Levier utilise : {levier}")
print(f"Perte max recalculé $ : {pertemax_recalc}")
print(f"Profit TP $ : {profit_recalc}")