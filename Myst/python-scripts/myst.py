# main function and should be called in another file


import speedtest # testing node strenth
import random # returning random node
import pandas as pd # node array
import os # reload mysteriumVPN


def sanatize():
    prop = [line.strip() for line in open("/root/dockerdata/data/proposals.list", 'r')]
    del prop[0]

    for x in range (len(prop)):
        prop[x] = prop[x].split("|")

    df = pd.DataFrame(prop, columns=[0, 'Identity', 'Type', 'Country', 4, 5]) # names each column
    df = df.drop([0, 4, 5], axis='columns') # dropping blank columns

    # sanatize each column
    for x in range(len(df)):
        df['Identity'][x] = df['Identity'][x].replace('Identity:', '').replace(' ', '')
        df['Type'][x] = df['Type'][x].replace('Type:', '').replace(' ', '')
        df['Country'][x] = df['Country'][x].replace('Country:', '').replace(' ', '')

    return(df)


def test_connection(random_node_string):
    #print('test_connection', flush=True)
    servers = []
    st = speedtest.Speedtest()
    st.get_servers(servers)
    st.get_best_server()
    try:
        if st.download() > 10000000:# and st.upload > 5000000:
            return True
        else:
            # write the node to the blacklist and return False
            BL = open("/root/dockerdata/data/blacklist.txt", "a")
            BL.write(str(random_node_string) + "\n")
            BL.close()
            return False
    except Exception as E:
        print("Except: " + str(E) + " & Node: " + str(random_node_string), flush=True) # most likely could not find server
        return False


def in_blacklist(random_node_string):
    #print('seeing if node is in blacklist', flush=True)
    BL = open("/root/dockerdata/data/blacklist.txt", "r")
    Blacklisted_Nodes = BL.read()

    for x in Blacklisted_Nodes:
        if random_node_string == x:
            return True
            break # no need to continue; it is blacklisted

        # see if we have compared all nodes in blacklist
        elif x == len(Blacklisted_Nodes):
            return False
            break # node is not in blacklist
        else:
            continue # node is not blacklisted
            

def reload_connection(random_node_string):
    #print('connecting to new node: ' + str(random_node_string), flush=True)
    os.system("myst connection down")  # stops the vpn
    os.system("myst connection up --agreed-terms-and-conditions " + random_node_string)  # starts new connection with node


def new_connection(Country, Type):
    df = sanatize()
    df = df[df['Country'].str.contains(Country) == True] # removes all nodes that dont match the County
    df = df[df['Type'].str.contains(Type) == True] # removes all nodes that dont match the Type
    
    random_node = df.sample()['Identity'] # gets randome row and returns the node
    random_node_string = random_node.to_string(index=False, header=False)# gets randome row and returns the node as a string

    # must test to see if the node is blacklisted
    if in_blacklist(random_node_string) == True:
        new_connection(Country, Type)

    # Then must ensure node is quick enough
    else:
        if test_connection(random_node_string) == False:
            new_connection(Country, Type)

        # node passed both tests
        else:
            # load next node and return True
            reload_connection(random_node_string) 
            return True