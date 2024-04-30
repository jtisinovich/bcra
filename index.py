from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

# Datos JSON proporcionados
json_data = '''

{"status":200,"errorMessages":"","results":[{"idVariable":1,"cdSerie":246,"descripcion":"Reservas Internacionales del BCRA\u00A0(en millones de dólares - cifras provisorias sujetas a cambio de valuación)","fecha":"24/04/2024","valor":"30.023"},{"idVariable":4,"cdSerie":7927,"descripcion":"Tipo de Cambio Minorista ($ por USD) Comunicación B 9791 - Promedio vendedor","fecha":"26/04/2024","valor":"918,36"},{"idVariable":5,"cdSerie":272,"descripcion":"Tipo de Cambio Mayorista ($ por USD) Comunicación A 3500\u00A0- Referencia","fecha":"26/04/2024","valor":"874,75"},{"idVariable":6,"cdSerie":7935,"descripcion":"Tasa de Política Monetaria (en % n.a.)","fecha":"26/04/2024","valor":"60,00"},{"idVariable":7,"cdSerie":1222,"descripcion":"BADLAR en pesos de bancos privados (en % n.a.)","fecha":"25/04/2024","valor":"56,5000"},{"idVariable":8,"cdSerie":7922,"descripcion":"TM20 en pesos de bancos privados\u00A0(en % n.a.)","fecha":"24/04/2024","valor":"61,9375"},{"idVariable":9,"cdSerie":7920,"descripcion":"Tasas de interés de las operaciones de pase activas para el BCRA, a 1 día de plazo\u00A0(en % n.a.)","fecha":"26/04/2024","valor":"90,00"},{"idVariable":10,"cdSerie":7921,"descripcion":"Tasas de interés de las operaciones de pase pasivas para el BCRA, a 1 día de plazo\u00A0(en % n.a.)","fecha":"26/04/2024","valor":"60,00"},{"idVariable":11,"cdSerie":3139,"descripcion":"Tasas de interés por préstamos entre entidades financiera privadas (BAIBAR)\u00A0(en % n.a.)","fecha":"25/04/2024","valor":"56,18"},{"idVariable":12,"cdSerie":1212,"descripcion":"Tasas de interés por depósitos a 30 días de plazo en entidades financieras\u00A0(en % n.a.)","fecha":"25/04/2024","valor":"57,16"},{"idVariable":13,"cdSerie":7924,"descripcion":"Tasa de interés de préstamos por adelantos en cuenta corriente","fecha":"24/04/2024","valor":"73,03"},{"idVariable":14,"cdSerie":7925,"descripcion":"Tasa de interés de préstamos personales","fecha":"24/04/2024","valor":"87,45"},{"idVariable":15,"cdSerie":250,"descripcion":"Base monetaria\u00A0- Total (en millones de pesos)","fecha":"24/04/2024","valor":"13.344.121"},{"idVariable":16,"cdSerie":251,"descripcion":"Circulación monetaria\u00A0(en millones de pesos)","fecha":"24/04/2024","valor":"8.561.894"},{"idVariable":17,"cdSerie":251,"descripcion":"Billetes y monedas en poder del público\u00A0(en millones de pesos)","fecha":"24/04/2024","valor":"7.795.024"},{"idVariable":18,"cdSerie":296,"descripcion":"Efectivo en entidades financieras\u00A0(en millones de pesos)","fecha":"24/04/2024","valor":"766.870"},{"idVariable":19,"cdSerie":252,"descripcion":"Depósitos de los bancos en cta. cte. en pesos en el BCRA\u00A0(en millones de pesos)","fecha":"24/04/2024","valor":"4.782.227"},{"idVariable":21,"cdSerie":444,"descripcion":"Depósitos en efectivo en las entidades financieras - Total (en millones de pesos)","fecha":"24/04/2024","valor":"82.684.965"},{"idVariable":22,"cdSerie":446,"descripcion":"En cuentas corrientes (neto de utilización FUCO)\u00A0(en millones de pesos)","fecha":"24/04/2024","valor":"15.345.183"},{"idVariable":23,"cdSerie":450,"descripcion":"En Caja de ahorros\u00A0(en millones de pesos)","fecha":"24/04/2024","valor":"26.994.549"},{"idVariable":24,"cdSerie":452,"descripcion":"A plazo (incluye inversiones y excluye CEDROS)\u00A0(en millones de pesos)","fecha":"24/04/2024","valor":"35.893.192"},{"idVariable":25,"cdSerie":7919,"descripcion":"M2 privado, promedio móvil de 30 días, variación interanual\u00A0(en %)","fecha":"24/04/2024","valor":"150,8"},{"idVariable":26,"cdSerie":392,"descripcion":"Préstamos de las entidades financieras al sector privado\u00A0(en millones de pesos)","fecha":"24/04/2024","valor":"25.807.692"},{"idVariable":27,"cdSerie":7931,"descripcion":"Inflación mensual (variación en %)","fecha":"31/03/2024","valor":"11,0"},{"idVariable":28,"cdSerie":7932,"descripcion":"Inflación interanual\u00A0(variación en % i.a.)","fecha":"31/03/2024","valor":"287,9"},{"idVariable":29,"cdSerie":7933,"descripcion":"Inflación esperada - REM próximos 12 meses\u00A0- MEDIANA (variación en % i.a)","fecha":"31/03/2024","valor":"120,0"},{"idVariable":30,"cdSerie":3540,"descripcion":"CER\u00A0(Base 2.2.2002=1)","fecha":"29/04/2024","valor":"352,6255"},{"idVariable":31,"cdSerie":7913,"descripcion":"Unidad de Valor Adquisitivo (UVA)\u00A0(en pesos -con dos decimales-, base 31.3.2016=14.05)","fecha":"29/04/2024","valor":"881,25"},{"idVariable":32,"cdSerie":7914,"descripcion":"Unidad de Vivienda (UVI)\u00A0(en pesos -con dos decimales-, base 31.3.2016=14.05)","fecha":"29/04/2024","valor":"686,90"},{"idVariable":34,"cdSerie":7936,"descripcion":"Tasa de Política Monetaria (en % e.a.)","fecha":"26/04/2024","valor":"82,12"},{"idVariable":35,"cdSerie":7937,"descripcion":"BADLAR en pesos de bancos privados (en % e.a.)","fecha":"24/04/2024","valor":"81,6000"},{"idVariable":37,"cdSerie":8145,"descripcion":"Inflación esperada - REM Diciembre 2023 MEDIANA (variación en % i.a)","fecha":"24/04/2024","valor":"147.371.710,0"},{"idVariable":40,"cdSerie":7988,"descripcion":"Índice para Contratos de Locación (ICL-Ley 27.551, con dos decimales, base 30.6.20=1)","fecha":"29/04/2024","valor":"12,29"},{"idVariable":41,"cdSerie":7990,"descripcion":"Tasas de interés de las operaciones de pase pasivas para el BCRA, a 1 día de plazo\u00A0(en % e.a.)","fecha":"26/04/2024","valor":"82,12"},{"idVariable":42,"cdSerie":266,"descripcion":"Pases pasivos para el BCRA - Saldos (en millones de pesos)","fecha":"24/04/2024","valor":"32.358.993"}]}


'''

# Función para filtrar los datos por fecha
def filtrar_por_fecha(data, desde, hasta):
    filtered_data = [entry for entry in data['results'] if desde <= entry['fecha'] <= hasta]
    return filtered_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener los datos del formulario
        endpoint_index = int(request.form['endpoint'])
        print(endpoint_index)
        fecha_desde = request.form['fecha_desde']
        fecha_hasta = request.form['fecha_hasta']
        print(fecha_hasta)
        
        # Cargar el JSON
        data = json.loads(json_data)
        id = str(data["results"][endpoint_index]["idVariable"])
        url = "https://api.bcra.gob.ar/estadisticas/v1/datosvariable/"+id+"/"+fecha_desde+"/"+fecha_hasta
        # Filtrar los datos por fecha
        #filtered_data = filtrar_por_fecha(data, fecha_desde, fecha_hasta)
        datos = requests.get(url, verify=False).json()
        endpoint = str(data["results"][endpoint_index]["descripcion"])
        
        return render_template('resultado.html', endpoint=endpoint, datos=datos)
    else:
        # Cargar el JSON
        data = json.loads(json_data)
        
        # Obtener los nombres de los endpoints disponibles
        endpoints = [entry['descripcion'] for entry in data['results']]
        
        return render_template('index.html', endpoints=endpoints)

if __name__ == '__main__':
    app.run(debug=True , host=0.0.0.0)
