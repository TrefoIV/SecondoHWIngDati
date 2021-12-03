import json

class caratteristiche_dataset_docenti(object):
    valNullNomeBocconi = 0
    valNullQualificaBocconi = 0
    valNullEmailBocconi = 0
    valNullDipartimentoBocconi = 0
    valNullCorsiBocconi = 0
    with open('WebExtraction/dettagliDocentiBocconi.json', 'r') as fp: 
        data = json.load(fp)
    for i in range(len(data)):   
        if data[i]['nome'] is None:
            valNullNomeBocconi += 1
        if data[i]['qualifica'] is None:
            valNullQualificaBocconi += 1
        if data[i]['dipartimento'] is None:
            valNullDipartimentoBocconi += 1
        if data[i]['email'] is None:
            valNullEmailBocconi += 1
        if len(data[i]['corsi']) == 0:
            valNullCorsiBocconi += 1

    caratteristicheBocconi = {
        'valNullNomeBocconi' : valNullNomeBocconi,
        'valNullQualificaBocconi' : valNullQualificaBocconi,
        'valNullDipartimentoBocconi' : valNullDipartimentoBocconi,
        'valNullEmailBocconi' : valNullEmailBocconi,
        'valNullCorsiBocconi' : valNullCorsiBocconi
    }

    valNullNomeR3 = 0
    valNullQualificaR3 = 0
    valNullEmailR3 = 0
    valNullDipartimentoR3 = 0
    valNullCorsiR3 = 0
    with open('WebExtraction/dettagliDocentiR3.json', 'r', encoding="utf8") as fp: 
        data = json.load(fp)
        #print(data)
    for i in range(len(data)): 
        if data[i]['nome'] is None:
            valNullNomeR3 += 1
        if data[i]['qualifica'] is None:
            valNullQualificaR3 += 1
        if data[i]['dipartimento'] is None:
            valNullDipartimentoR3 += 1
        if data[i]['email'] is None:
            valNullEmailR3 += 1
        if len(data[i]['corsi']) == 0:
            valNullCorsiR3 += 1

    caratteristicheR3 = {
        'valNullNomeR3' : valNullNomeR3,
        'valNullQualificaR3' : valNullQualificaR3,
        'valNullDipartimentoR3' : valNullDipartimentoR3,
        'valNullEmailR3' : valNullEmailR3,
        'valNullCorsiR3' : valNullCorsiR3
    }

    print(caratteristicheBocconi)
    print(caratteristicheR3)