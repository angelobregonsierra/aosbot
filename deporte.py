# -*- coding: utf-8 -*-

from pywikibot import pagegenerators as pg
import pywikibot


cambiar_compite = {"Q191691": "Q542", # 1500 metros en deporte debería estar en compite en la disciplina deportiva (P2416) -> atletismo en deporte
"Q334734": "Q542", # 400 metros -> atletismo
"Q271008": "Q542", # 800 metros -> atletismo
"Q1026754": "Q542", # 60 metros vallas -> atletismo
"Q163892": "Q542", # 10 000 metros -> atletismo
"Q164731": "Q542", # 100 metros vallas -> atletismo
"Q1629556": "Q542", # 1 000 metros -> atletismo
"Q231419": "Q542", # 400 metros vallas -> atletismo
"Q211155": "Q542", # 200 metros -> atletismo
"Q230057": "Q542", # relevo 4 x 400 metros -> atletismo
"Q164761": "Q542", # 100 metros -> atletismo
"Q230061": "Q542", # relevo 4 x 100 metros -> atletismo
"Q223779": "Q542", # 3000 metros -> atletismo
"Q170737": "Q542", # salto de longitud -> atletismo
"Q624482": "Q542", # carrera de velocidad -> atletismo
"Q26303": "Q542", # ultramaratón -> atletismo
"Q500050": "Q542", # campo a través -> atletismo
"Q10437559": "Q542", # 3000 metros con obstáculos -> atletismo
"Q105674": "Q542", # carrera a pie -> atletismo
"Q917206": "Q542", # carrera de larga distancia -> atletismo
"Q1163256": "Q542", # carrera de media distancia -> atletismo
"Q182570": "Q542", # lanzamiento de disco -> atletismo
"Q178108": "Q542", # lanzamiento de jabalina -> atletismo
"Q184865": "Q542", # lanzamiento de martillo -> atletismo
"Q180935": "Q542", # lanzamiento de peso -> atletismo
"Q185027": "Q542", # salto con pértiga -> atletismo
"Q165704": "Q542", # salto de altura -> atletismo
"Q537769": "Q542", # carreras de vallas -> atletismo
"Q223836": "Q542", # carreras con obstáculos -> atletismo
"Q187204": "Q542", # triple salto -> atletismo
"Q40244": "Q542", # maratón -> atletismo
"Q202391": "Q542", # marcha atlética -> atletismo
"Q1805420": "Q542", # carrera de resistencia -> atletismo
"Q170004": "Q542", # 110 metros vallas -> atletismo
"Q3991761": "Q542", # two handed javelin throw -> atletismo
"Q243264": "Q542", # heptatlón -> atletismo
"Q184654": "Q542", # decatlón -> atletismo
"Q30902198": "Q542", # speed walking -> atletismo
"Q5369934": "Q542", # carreras lisas -> atletismo
"Q1934817": "Q542", # caminata de calle -> atletismo
"Q3216963": "Q542", # prueba de lanzamiento -> atletismo
"Q3924425": "Q542", # pruebas combinadas -> atletismo
"Q3694569": "Q542", # running -> atletismo
"Q352749": "Q542", # sprint -> atletismo
"Q11706688": "Q542", # sprinting -> atletismo
"Q21002582": "Q542", # beach walking -> atletismo
"Q245249": "Q31920", # estilo mariposa -> natación
"Q31987": "Q31920", # freestyle swimming -> natación
"Q657196": "Q31920", # Medley -> natación
"Q15243549": "Q31920", # men's 100 metre backstroke S10 -> natación
"Q1968": "Q5386", # Fórmula 1 -> automovilismo
"Q1199515": "Q5386", # formula racing -> automovilismo
"Q1089579": "Q5386", # antecedentes de la Fórmula 1 -> automovilismo
"Q1758324": "Q5386", # stock car -> automovilismo
"Q371804": "Q5386", # sports car racing -> automovilismo
"Q17163326": "Q328716", # motorcycle racing -> motociclismo
"Q3548048": "Q2093999", # ultra-trail -> carrera de montaña
"Q3962667": "Q2093999", # Skyrunning -> carrera de montaña
"Q4010279": "Q2093999", # vertical kilometre -> carrera de montaña
"Q1754518": "Q130949", # Freeride -> esquí
"Q26787631": "Q178678", # K-1 -> kick boxing
"Q193654": "Q192431", # patinaje de velocidad sobre pista corta -> patinaje de velocidad
"Q17165362": "Q192431", # patinaje de velocidad sobre pista larga -> patinaje de velocidad
"Q2597988": "Q221635", # Carrera por puntos -> ciclismo en pista
"Q1307101": "Q221635", # individual pursuit -> ciclismo en pista
"Q7076153": "Q14085739", # ocean racing -> vela
"Q6071065": "Q212845", # pelota mano -> pelota vasca
"Q1218163": "Q43450", # Tumbling -> gimnasia
"Q646211": "Q10980", # ultra-triathlon -> triatlón
"Q838781": "Q179226", # concurso completo -> equitación
"Q216033": "Q179226", # doma clásica -> equitación
"Q1392681": "Q179226", # enganches ecuestres -> equitación
"Q902378": "Q179226", # deporte ecuestre -> equitación
"Q211773": "Q179226", # salto ecuestre -> equitación
"Q2283687": "Q2483334", # Raspall -> pelota valenciana
"Q1156606": "Q12100", # Sable -> esgrima
"Q16996906": "Q41323", # fútbol americano cubierto -> fútbol americano
"Q1109032": "Q41323", # fútbol americano universitario -> fútbol americano
"Q2313068": "Q779272", # marathon speed skating -> patinaje sobre hielo
"Q1192132": "Q189472", # mogul skiing -> esquí acrobático
"Q477500": "Q189472", # slopestyle -> esquí acrobático

}


cambiar_errores = {"Q961015": "Q32112", # boxeo femenino en deporte -> boxeo en deporte debería estar
"Q11513337": "Q542", # atleta -> atletismo
"Q13365117": "Q8418", # balonmanista -> balonmano
"Q2887217": "Q5372", # baloncesto femenino -> baloncesto
"Q3312129": "Q542", # Atletismo de pista y campo -> atletismo
"Q13382608": "Q179687", # esquiador de fondo -> esquí de fondo
"Q9017214": "Q11419", # karateka -> karate
"Q983987": "Q32485", # pentatlón femenino -> pentatlón
"Q13381428": "Q542", # saltador de longitud -> atletismo
"Q10843402": "Q31920", # nadador -> natación
"Q25999": "Q14085739", # vela -> vela
"Q816745": "Q12100", # Espada ropera -> esgrima
"Q13383011": "Q177275", # piloto de bobsleigh -> bobsleigh
"Q6388": "Q31920", # natación -> natación
"Q11338576": "Q32112", # boxeador -> boxeo
"Q18156733": "Q159992", # surf -> surf
"Q2309784": "Q2215841", # ciclista -> ciclismo de competición
"Q35752": "Q131359", # WWE Superstars -> lucha libre profesional
"Q231204": "Q12100", # sable -> esgrima
"Q850292": "Q328716", # Campeonato del Mundo de Motociclismo -> motociclismo
"Q13381753": "Q542", # mediofondista -> atletismo
"Q471447": "Q12100", # florete -> esgrima
"Q2730732": "Q187916", # jinete hípico -> turf
"Q3897311": "Q2215841", # rodador -> ciclismo de competición
"Q2757019": "Q1734", # volleyball -> voleybol
"Q17524364": "Q7707", # waterpolista -> waterpolo
"Q2665822": "Q136851", # skip -> curling
"Q606060": "Q2736", # fútbol femenino -> fútbol
"Q7078900": "Q5386", # off-road racing -> automovilismo
"Q326704": "Q300920", # FIFA -> deporte electrónico
"Q15037754": "Q192420", # kart -> karting
"Q2380088": "Q22857", # escalador -> ciclismo
"Q14554839": "Q12100", # competitive fencing -> esgrima
"Q2393176": "Q186222", # esquí alpino -> esquí alpino
"Q53121": "Q2215841", # ciclismo -> ciclismo de competición
"Q18544844": "Q179687", # esquí de fondo -> esquí de fondo
"Q1081491": "Q2736", # fútbol -> fútbol
"Q20855541": "Q884250", #fútbol para ciegos -> fútbol para ciegos
"Q13108218": "Q43450", # gymnastics -> gimnasia
"Q1340655": "Q1759797", # lead climbing -> lead climbing
"Q2094922": "Q1875777" # maniobra aérea acrobática -> carrera aérea
"Q16014286": "Q7735" # platform diving -> salto
"Q14405929": "Q7735" # salto de gran altura -> salto
"Q16014295": "Q7735" # salto de trampolín -> salto
"Q2393462": "Q108429" # target archery -> tiro con arco
"Q2167372": "Q2093999" # carrera de montaña -> carreras de montaña
"Q743526": "Q2736", # Association Football -> fútbol
}


borrar_deporte = {"Q33999",  #actor debe borrarse
"Q488111", #actor pornográfico
"Q41583", #entrenador
"Q4596040", #1 point player
"Q539632", #Baidar
"Q171529", #canoa
"Q204368", #Chi kung
"Q492", #memoria
"Q177054", #Burger King
"Q184940", #tauromaquia
"Q126701", #regata
"Q791187", #pelota de béisbol
"Q4610556", #modelo
"Q309252", #fitness
"Q1707432", #Patín sobre ruedas tradicional
"Q204686", #deporte de invierno
"Q11047409", #deporte atlético
"Q2284014", #deporte de contacto
"Q5367", #deportes de motor
"Q31668", #Crashed Ice
"Q21061444": #Taikyoku ken
}

anadir_deporte = {"Q11957145": "Q193036", # acróbata en ocupación -> acrobacia en deporte
"Q4696968": "Q43114", # aikidoka -> aikidō
"Q27062049": "Q2497700", # aizcolari -> aizcolari
"Q10873124": "Q718", # ajedrecista -> ajedrez
"Q2229544": "Q718", # árbitro de ajedrez -> ajedrez
"Q15916915": "Q718", # funcionario de ajedrez -> ajedrez
"Q15916730": "Q718", # entrenador de ajedrez -> ajedrez
"Q30176225": "Q1128406", # ajedrecista por correspondencia -> ajedrez postal
"Q11124885": "Q11417", # artista marcial -> arte marcial
"Q11607585": "Q114466", # luchador de artes marciales mixtas -> artes marciales mixtas
"Q21141381": "Q542", # decatleta -> atletismo
"Q7831495": "Q542", # árbitro de atletismo -> atletismo
"Q19827985": "Q542", # entrenador de atletismo -> atletismo
"Q7627813": "Q542", # atleta estudiante -> atletismo
"Q2312865": "Q542", # atleta militar -> atletismo
"Q13381689": "Q542", # lanzador de disco -> atletismo
"Q18510502": "Q542", # lanzador de jabalina -> atletismo
"Q13856320": "Q542", # lanzador de martillo -> atletismo
"Q18534714": "Q542", # lanzador de peso -> atletismo
"Q4439155": "Q542", # fondista -> atletismo
"Q13381753": "Q542", # mediofondista -> atletismo
"Q13382460": "Q542", # maratonista -> atletismo
"Q17405793": "Q542", # marchador atlético -> atletismo
"Q15972912": "Q542", # pentatleta -> atletismo
"Q13848274": "Q542", # saltador de triple salto -> atletismo
"Q1440873": "Q542", # showrunner -> atletismo
"Q19827218": "Q542", # ultramaratonista -> atletismo
"Q4009406": "Q542", # velocista -> atletismo
"Q13381428": "Q542", # saltador de longitud -> atletismo
"Q13464497": "Q542", # saltador de pértiga -> atletismo
"Q13382122": "Q542", # saltador de altura -> atletismo
"Q11513337": "Q542", # atleta -> atletismo
"Q14605941": "Q542", # atleta de pruebas combinadas -> atletismo
"Q25439032": "Q1757181", # atleta paralímpico -> atletismo paralímpico
"Q15958185": "Q5386", # piloto de automovilismo -> automovilismo
"Q3332120": "Q5386", # mecánico de carreras automovilísticas -> automovilismo
"Q10841764": "Q5386", # piloto de Fórmula Uno -> automovilismo
"Q13141064": "Q7291", # badmintonista -> bádminton
"Q28143257": "Q7291", # entrenador de bádminton -> bádminton
"Q3665646": "Q5372", # baloncestista -> baloncesto
"Q2182752": "Q5372", # árbitro de baloncesto -> baloncesto
"Q17279652": "Q5372", # entrenador asistente de baloncesto -> baloncesto
"Q2182752": "Q5372", # árbitro de baloncesto -> baloncesto
"Q13365117": "Q8418", # balonmanista -> balonmano
"Q13365201": "Q8418", # entrenador de balonmano -> balonmano
"Q18702210": "Q183018", # jugador de bandy -> bandy
"Q11336312": "Q5369", # beisbolista profesional -> béisbol
"Q10871364": "Q5369", # beisbolista -> béisbol
"Q865935": "Q5369", # técnico asistente de beisbol -> béisbol
"Q16029547": "Q166788", # biatleta -> biatlón
"Q20540007": "Q3341285", # billarista (billar americano) -> billar
"Q13383011": "Q177275", # piloto de bobsleigh -> bobsleigh
"Q11338576": "Q32112", # boxeador -> boxeo
"Q22122536": "Q32112", # entrenador de boxeo -> boxeo
"Q2859667": "Q32112", # árbitro de boxeo -> boxeo
"Q22269196": "Q2631720", # boxeador profesional -> boxeo profesional
"Q18437198": "Q188966", # jugador de bridge -> bridge
"Q2309784": "Q2215841", # ciclista -> ciclismo de competición
"Q19799599": "Q520611", # ciclista de montaña -> ciclismo de montaña
"Q15117395": "Q221635", # ciclista de pista -> ciclismo en pista
"Q15117415": "Q335638", # ciclista de ciclocrós -> ciclocrós
"Q13382605": "Q201965", # esquiador de combinada nórdica -> combinada nórdica
"Q12299841": "Q5375", # jugador de críquet -> críquet
"Q2143894": "Q5375", # árbitro de críquet -> críquet
"Q24238692": "Q193387", # jugador de croquet -> croquet
"Q15982795": "Q124100", # culturista -> culturismo
"Q18574233": "Q131471", # jugador de dardos -> dardos
"Q4379701": "Q300920", # jugador profesional de videojuegos -> deporte electrónico
"Q466640": "Q179226", # entrenador de caballos -> equitación
"Q3951423": "Q1154336", # escalador en roca -> escalada en roca
"Q13381863": "Q12100", # esgrimista -> esgrima
"Q4270517": "Q130949", # esquiador -> esquí
"Q18617021": "Q189472", # esquiador acrobático -> esquí acrobático
"Q18710968": "Q472827", # esquiador acuático -> esquí acuático
"Q4144610": "Q186222", # esquiador alpino -> esquí alpino
"Q13382608": "Q179687", # esquiador de fondo -> esquí de fondo
"Q19801627": "Q1075998", # esquiador de travesía -> esquí de travesía
"Q51208995": "Q1358925", # esquiador de velocidad -> esquí de velocidad
"Q628099": "Q2736", # entrenador de fútbol -> fútbol
"Q937857": "Q2736", # futbolista -> fútbol
"Q859528": "Q2736", # árbitro de fútbol -> fútbol
"Q2445218": "Q2736", # entrenador de guardametas -> fútbol
"Q937857": "Q2736", # futbolista -> fútbol
"Q19204627": "Q41323", # jugador de fútbol americano -> fútbol americano
"Q716711": "Q41323", # árbitro de fútbol americano -> fútbol americano
"Q13414980": "Q50776", # jugador de fútbol australiano -> fútbol australiano
"Q19841381": "Q248534", # jugador de fútbol canadiense -> fútbol canadiense
"Q7079487": "Q248534", # árbitro de fútbol canadiense -> fútbol canadiense
"Q17351861": "Q204632", # jugador de fútbol gaélico -> fútbol gaélico
"Q18515558": "Q171401", # jugador de fútbol sala -> fútbol sala
"Q50654094": "Q171401", # entrenador de fútbol sala -> fútbol sala
"Q16947675": "Q43450", # gimnasta -> gimnasia
"Q13381572": "Q326827", # gimnasta artístico -> gimnasia artística
"Q23892384": "Q465014", # gimnasta de trampolín -> gimnasia en trampolín
"Q24037210": "Q61465", # gimnasta rítmico -> gimnasia rítmica
"Q12039558": "Q11413", # jugador de go -> go
"Q3186699": "Q11413", # jugador profesional de go -> go
"Q11303721": "Q5377", # golfista -> golf
"Q490253": "Q5377", # golfista profesional -> golf
"Q13381376": "Q83462", # halterófilo -> halterofilia
"Q10843263": "Q1622659", # jugador de hockey -> hockey
"Q1757103": "Q41466", # árbitro de hockey sobre hielo -> hockey sobre hielo
"Q5137576": "Q41466", # entrenador de hockey sobre hielo -> hockey sobre hielo
"Q11774891": "Q41466", # jugador de hockey sobre hielo -> hockey sobre hielo
"Q3621342": "Q1455", # árbitro de hockey sobre césped -> hockey sobre hierba
"Q9017214": "Q11419", # karateka -> karate
"Q16004471": "Q2094083", # kayakista -> kayak
"Q11296761": "Q178678", # kickboxer -> kick boxing
"Q17682262": "Q185851", # jugador de lacrosse -> lacrosse
"Q27062349": "Q3997677", # levantador de piedras -> levantamiento de piedras
"Q23845879": "Q213796", # levantador de potencia -> levantamiento de potencia
"Q27978698": "Q42486", # luchador -> lucha
"Q19595175": "Q838089", # luchador -> lucha aficionada
"Q13474373": "Q131359", # luchador profesional -> lucha libre profesional
"Q721051": "Q131359", # árbitro de lucha profesional -> lucha libre profesional
"Q13382981": "Q273285", # luger -> luge
"Q9149093": "Q36908", # montañero -> montañismo
"Q3014296": "Q328716", # piloto de motociclismo -> motociclismo
"Q12327806": "Q215862", # piloto de motocross -> motocross
"Q388513": "Q120931", # luchador de muay thai -> muay thai
"Q10843402": "Q31920", # nadador -> natación
"Q20730773": "Q31920", # entrenador de natación -> natación
"Q18715859": "Q180692", # nadador sincronizado -> natación sincronizada
"Q17619498": "Q231200", # jugador de netball -> netball
"Q6060450": "Q193210", # paracaidista -> paracaidismo
"Q749387": "Q193210", # paracaidista militar -> paracaidismo
"Q13219587": "Q38108", # patinador artístico sobre hielo -> patinaje artístico sobre hielo
"Q10866633": "Q192431", # patinador de velocidad -> patinaje de velocidad
"Q18200514": "Q192431", # patinador de velocidad sobre pista corta -> patinaje de velocidad
"Q9394993": "Q779272", # patinador sobre hielo -> patinaje sobre hielo
"Q19746576": "Q212845", # pelotari -> pelota vasca
"Q13382566": "Q213934", # piragüista -> piragüismo
"Q15295720": "Q80131", # jugador de póquer -> póquer
"Q10842936": "Q7856", # piloto de rally -> rally
"Q17611899": "Q754586", # jugador de raquetbol -> raquetbol
"Q13382576": "Q159354", # remero -> remo
"Q21121588": "Q159354", # entrenador de remo -> remo
"Q13415036": "Q5378", # jugador de rugby -> rugby
"Q14089670": "Q5378", # jugador de rugby union -> rugby
"Q2859671": "Q5849", # árbitro de rugby a 15 -> rugby a 15
"Q15041977": "Q5849", # entrenador de rugby a 15 -> rugby a 15
"Q14373094": "Q10962", # jugador de liga de rugby -> rugby league
"Q13382603": "Q7718", # saltador de esquí -> salto de esquí
"Q17502714": "Q842284", # skater -> skateboarding
"Q17165321": "Q11015", # jugador de snooker -> snooker
"Q15709642": "Q178131", # snowboarder -> snowboarding
"Q13388586": "Q171038", # jugador de sóftbol -> sóftbol
"Q16278103": "Q133201", # jugador de squash -> squash
"Q2727289": "Q40561", # luchador de sumo -> sumo
"Q13561328": "Q159992", # surfista -> surf
"Q13382533": "Q36389", # taekwondista -> taekwondo
"Q10833314": "Q847", # tenista -> tenis
"Q3502546": "Q847", # árbitro de tenis -> tenis
"Q13219424": "Q847", # entrenador de tenis -> tenis
"Q13382519": "Q3930", # tenista de mesa -> tenis de mesa
"Q18814798": "Q1153025", # tenista en silla de ruedas -> tenis en silla de ruedas
"Q15306067": "Q10980", # triatleta -> triatlón
"Q846750": "Q187916", # jockey -> turf
"Q476246": "Q14085739", # regatista -> vela
"Q15117302": "Q1734", # voleibolista -> voleibol
"Q20730881": "Q1734", # entrenador de voleibol -> voleibol
"Q17361156": "Q4543", # jugador de voleibol de playa -> voleibol de playa
"Q13382191": "Q7707", # árbitro de waterpolo -> waterpolo
"Q17524364": "Q7707", # waterpolista -> waterpolo
"Q13382487": "Q191051", # windsurfista -> windsurf
"Q6665249": "Q11420", # yudoca -> yudo
}


def consulta(borra, site=None):
    query = """
    SELECT DISTINCT ?item WHERE {
       SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
       ?item wdt:P31 wd:Q5.
       ?item wdt:P641 wd:""" + borra + """.
       OPTIONAL { ?item wdt:P641 ?deporte. }
    } """
    # print(query)
    return pg.WikidataSPARQLPageGenerator(query, site=site)


def consulta_add(ocupacion, site=None):
    query = """
    SELECT DISTINCT ?item WHERE {
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
      ?item wdt:P31 wd:Q5.
      ?item wdt:P106 wd:""" + ocupacion + """.
      OPTIONAL { ?item wdt:P641 ?deporte. }
      FILTER (!BOUND(?deporte))
    } """
    # print(query)
    return pg.WikidataSPARQLPageGenerator(query, site=site)


def tarea1(repo, wikidata_site):
    print("Comienzo de tarea 1")
    # 1ª tarea, borrar todos los valores sin sentido de la propiedad deporte (P641). Se recogen del diccionario borrar_deporte
    # for borra in borrar_deporte:
        # pages = consulta(borra, site=wikidata_site)
        # for item in pages:
            # item.get()
            # print("<<<<< borrando " + borra + " de " + item.title())
            # item.removeClaims(item.claims['P2416'])


def tarea2(repo, wikidata_site):
    print("Comienzo de tarea 2")
    # 2ª tarea, se cambia el valor de deporte (P641) cuando los valores son erróneos pero tiene sentido sustituirles como atleta a atletismo. 
    # Se recogen los datos del diccionario cambiar_errores
    # for camb in cambiar_errores:
        # pages = consulta(camb, site=wikidata_site)
        # for item in pages:
            # item.get()
            # print(str(camb) + " " + str(item.title()))
            ## mira si existe ya introducido ese valor
            # for claim in item.claims['P641']:
                # if (str(claim.getTarget())=='[[wikidata:' + cambiar_errores[camb] + ']]'):
                   # cont+=1
                   # break
            # if (cont==0):
                # print(cambiar_errores[camb])
            # for claim in item.claims['P641']:
                # if (str(claim.getTarget())=='[[wikidata:' + cambiar_errores[camb] + ']]'):
                    # trgt = claim.getTarget()
                    # if trgt.id == camb:
                        # print("Cambiando {} por {}".format(camb, cambiar_errores[camb]))
                        # correct_page = pywikibot.ItemPage(repo, cambiar_errores[camb], 0)
                        # claim.changeTarget(correct_page)

def tarea3(repo, wikidata_site):
    print("Comienzo de tarea 3")
    # 3ª tarea, se cambia el valor de deporte (P641) cuando los valores deberían de estar en compite en la disciplina deportiva (P2416)
    # Se pasa el valor que está en P641 a P2416 y en P641 se pone lo que indique cambiar_compite
    # for comp in cambiar_compite:
        # pages = consulta(comp, site=wikidata_site)
        # for item in pages:
            # item.get()
            # print(str(comp) + " " + str(item.title()))
            # try:
                # for valor in item.claims['P2416']:
                # if (str(claim.getTarget())=='[[wikidata:' + comp + ']]'):
                    # cont=1
                    # break
            # except:
                # cont=0
            # # si no existía el valor en compite en la disciplina deportiva (P2416) entonces lo añade
            # if cont==0:
                # claim = pywikibot.Claim(repo, u'P2416')
                # target = pywikibot.ItemPage(repo, "Q334734")
                # claim.setTarget(target)
                # item.addClaim(claim, summary=u'Añadiendo')
            # # ahora cambia el valor que estaba por el nuevo que obtiene de cambiar_compite
            # for claim in item.claims['P641']:
                # if (str(claim.getTarget())=='[[wikidata:' + cambiar_compite[comp] + ']]'):
                    # trgt = claim.getTarget()
                    # if trgt.id == comp:
                        # print("Correcting {} to {}".format(comp, cambiar_compite[comp]))
                        # correct_page = pywikibot.ItemPage(repo, cambiar_compite[comp], 0)
                        # claim.changeTarget(correct_page)


def tarea4(repo, wikidata_site):
    print("Comienzo de tarea 4")
    # 4ª tarea, se busca aquellos artículos que tengan profesión u ocupación con un término deportivo, pero tienen deporte (P641) vacío
    for add in anadir_deporte:
        pages = consulta_add(add, site=wikidata_site)
        for item in pages:
            claim = pywikibot.Claim(repo, u'P641')
            target = pywikibot.ItemPage(repo, anadir_deporte[add])
            claim.setTarget(target)
            item.addClaim(claim, summary=u'Añadiendo deporte (P641)')


def main():
    wikidata_site = pywikibot.Site("wikidata", "wikidata")
    repo = wikidata_site.data_repository()
    cont=0
    tarea1(repo, wikidata_site)
    tarea2(repo, wikidata_site)
    tarea3(repo, wikidata_site)
    tarea4(repo, wikidata_site)


if __name__ == "__main__":
    main()