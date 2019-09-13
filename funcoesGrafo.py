def recupera_distancia(json_object, aeroportoOrigem, aeroportoDestino):
    for dicionario in json_object:
        if aeroportoOrigem == dicionario['ORIGIN_AIRPORT'] and \
            aeroportoDestino == dicionario['DESTINATION_AIRPORT']:
            return dicionario['DISTANCE']