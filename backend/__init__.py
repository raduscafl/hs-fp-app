def process_user_query(query_string):
    population=[]
    player=[]
    page=""
    warning="You have enter a wiki page which is not about a football player or a city"
    query_string=query_string.strip().split()
    query_string = [x.replace('•', ' ') for x in query_string]
    query_string = [i for i in query_string if i != ' ']

    check_page=query_string[:300]

    if any("Personal" in pers for pers in check_page):
        page="Football Player"
    elif any("Country" in count for count in check_page):
        page="City"
    else:
        pass

    if page=="City":
        city=query_string.index("From")
        if city==1:
            population.append("City:" + query_string[0])
        elif city==2:
            population.append("City:" + query_string[0]+ " " +query_string[1])
        elif city==3:
            population.append("City:" + query_string[0]+ " " +query_string[1]+ " " +query_string[2])
        else:
            population.append("City:" + query_string[0]+ " " +query_string[1]+ " " +query_string[2]+ " " +query_string[3])

        country=query_string.index("Country")
        population.append("Country:" + query_string[country+1])

        area=query_string.index("km2")
        population.append("Area:" + query_string[area-1]+ " "+ query_string[area])

        i=query_string.index("Population")
        i=i+3
        if query_string[i]=="Total" or query_string[i]=="Metropolis" or query_string[i]=="City" or query_string[i]=="London" or query_string[i]=="Urban" or query_string[i]=="Special" or query_string[i]=="2016"or query_string[i]=="2016)"or query_string[i]=="Metropolitan" :
            i=i+1
        else:
            pass
        if query_string[i]=="Total" or query_string[i]=="Metropolis" or query_string[i]=="City" or query_string[i]=="London" or query_string[i]=="Urban" or query_string[i]=="Special"or query_string[i]=="2016"or query_string[i]=="2016)"or query_string[i]=="Metropolitan"or query_string[i]=="Metropolitan" :
            i=i+1
        else:
            pass
        if query_string[i]=="Total" or query_string[i]=="Metropolis" or query_string[i]=="City" or query_string[i]=="London" or query_string[i]=="Urban" or query_string[i]=="Special"or query_string[i]=="2016"or query_string[i]=="2016)"or query_string[i]=="Metropolitan" :
            i=i+1
        else:
            pass
        population.append("Population:" + query_string[i])

        return population

    elif page=="Football Player":
        name=query_string.index("Full")
        if query_string[name+4]=="Date":
            player.append("Name:" + query_string[name+2]+ " " + query_string[name+3])
        elif query_string[name+5]=="Date":
            player.append("Name:" + query_string[name+2]+ " " + query_string[name+3]+ " " + query_string[name+4])
        elif query_string[name+6]=="Date":
            player.append("Name:" + query_string[name+2]+ " " + query_string[name+3]+ " " + query_string[name+4]+ " " + query_string[name+5])
        else:
            player.append("Name:" + query_string[name+2]+ " " + query_string[name+3]+ " " + query_string[name+4]+ " " + query_string[name+5]+ " " + query_string[name+6])

        birth=query_string.index("birth")
        player.append("Date of Birth:" + query_string[birth+1] +" "+ query_string[birth+2] +" " + query_string[birth+3])
        height=query_string.index("Height")
        player.append("Place of Birth:" + query_string[height-1])
        player.append("Height:" + query_string[height+1] + query_string[height+2])

        position=query_string.index("position")
        if query_string[position+2]=="Club":
            player.append("Position:" + query_string[position+1])
        else:
            player.append("Position:" + query_string[position+1]+ " "+ query_string[position+2])

        team=query_string.index("team")
        if query_string[team+2]=="Number":
            player.append("Team:" + query_string[team+1])
        else:
            player.append("Team:" + query_string[team+1]+" "+ query_string[team+2])

        return player

    else:
        return warning

process_user_query(r'''''')
