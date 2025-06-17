# =================  UTILS   =================
def linear_search( data, target ):
    
    for i in range( len(data) ):
        if( target == data[i] ): return i

    return None

def binary_search( data, target, begin=0, end=None ):

    if end is None:
        end = len(data)-1
        
    if begin <= end:
        mid = ( begin + end ) // 2
        
        if data[mid] == target:
            return mid
        if target < data[mid]:
            return binary_search( data, target, begin, mid-1 )
        else:
            return binary_search( data, target, mid+1, end )
        
    return None

def exponential_search( data, target ):
    if( data[0] == target ):
        return 0

    index = 1
    while( index < len(data) and data[index] < target ):
        index *= 2

    if( index > len(data) - 1):
        index = len(data) - 1

    return binary_search( data, target, (index // 2), index )
# =================  UTILS   =================



# ================= GEN DATA =================
import random

def gen_data():
    data = [ [], [], [], [], [], [], [] ]

    for i in range(1, len(data) ):

        for j in range(10**i):
            data[i].append( random.randrange(99999) )

        # Organiza o dataset
        data[i].sort()

    return data
# ================= GEN DATA =================



# =================   MAIN   =================
import time

# Cria dataset
data = gen_data()
time_list = []

for j in range( 1, len(data) ):
    print( "Data lenght:", len(data[j]) )

    # Viriavel auxiliar para calculo do tempo total
    aux = 0

    # Cria lista com elementos a serem buscados
    # primeiro, central, ultimo, nao existente
    to_search = [ data[j][0] ]

    mid_element = ( len(data[j]) - 1 ) // 2
    to_search.append( data[j][mid_element] )

    last_element = len( data[j] ) - 1
    to_search.append( data[j][last_element] )

    to_search.append( to_search[2] * 2 )

    for k in range(4):
        t1 = time.perf_counter()
        linear_search( data[j], to_search[k] )
        #binary_search( data[j], to_search[k] )
        #exponential_search( data[j], to_search[k] )
        t2 = time.perf_counter()

        dt = format( (t2 - t1), ".10f" )
        print( f"Searching for\t{to_search[k]}\t\t{dt} (s)" )

    print( f"{format( (t2 - t1), '.10f' )}" )
    print( "=========================================" )
# =================   MAIN   =================
