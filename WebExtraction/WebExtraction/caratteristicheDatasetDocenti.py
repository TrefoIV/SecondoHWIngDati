import json

class caratteristiche_dataset_docenti(object):
    valNullNomeBocconi = 0
    valNullQualificaBocconi = 0
    valNullEmailBocconi = 0
    valNullDipartimentoBocconi = 0
    valNullCorsiBocconi = 0
    with open('WebExtraction/dettagliDocentiBocconi.json', 'r') as fp: 
        dataBocconi = json.load(fp)
    for i in range(len(dataBocconi)):   
        if dataBocconi[i]['nome'] is None:
            valNullNomeBocconi += 1
        if dataBocconi[i]['qualifica'] is None:
            valNullQualificaBocconi += 1
        if dataBocconi[i]['dipartimento'] is None:
            valNullDipartimentoBocconi += 1
        if dataBocconi[i]['email'] is None:
            valNullEmailBocconi += 1
        if len(dataBocconi[i]['corsi']) == 0:
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
        dataR3 = json.load(fp)
        #print(data)
    for i in range(len(dataR3)): 
        if dataR3[i]['nome'] is None:
            valNullNomeR3 += 1
        if dataR3[i]['qualifica'] is None:
            valNullQualificaR3 += 1
        if dataR3[i]['dipartimento'] is None:
            valNullDipartimentoR3 += 1
        if dataR3[i]['email'] is None:
            valNullEmailR3 += 1
        if len(dataR3[i]['corsi']) == 0:
            valNullCorsiR3 += 1

    caratteristicheR3 = {
        'valNullNomeR3' : valNullNomeR3,
        'valNullQualificaR3' : valNullQualificaR3,
        'valNullDipartimentoR3' : valNullDipartimentoR3,
        'valNullEmailR3' : valNullEmailR3,
        'valNullCorsiR3' : valNullCorsiR3
    }

    percentualiValoriNulli ={
        'percValNullNomiR3' : (valNullNomeR3/len(dataR3))*100,
        'valNullNomeBocconi' : (valNullNomeBocconi/len(dataBocconi))*100,
        'percValNullQualificaR3' : (valNullQualificaR3/len(dataR3))*100,
        'valNullQualificaBocconi' : (valNullQualificaBocconi/len(dataBocconi))*100,
        'valNullDipartimentoR3' : (valNullDipartimentoR3/len(dataR3))*100,
        'valNullDipartimentoBocconi' : (valNullDipartimentoBocconi/len(dataBocconi))*100,
        'valNullEmailR3' : (valNullEmailR3/len(dataR3))*100,
        'valNullEmailBocconi' : (valNullEmailBocconi/len(dataBocconi))*100,
        'valNullCorsiR3' : (valNullCorsiR3/len(dataR3))*100,
        'valNullCorsiBocconi' : (valNullCorsiBocconi/len(dataBocconi))*100,
        }

    dimensioniDataset = {
        'numDocentiR3' : len(dataR3),
        'numDocentiBocconi' : len(dataBocconi),
        }

    for i in dimensioniDataset:
        print(i, dimensioniDataset[i])
    
    for i in caratteristicheBocconi:
        print(i, caratteristicheBocconi[i])

    for i in caratteristicheR3:
        print(i, caratteristicheR3[i])

    for i in percentualiValoriNulli:
        print(i, percentualiValoriNulli[i])

    #print(dimensioniDataset)
    #print(percentualiValoriNulli)
    #print(caratteristicheBocconi)
    #print(caratteristicheR3)