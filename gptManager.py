import openai
from ascii_magic import AsciiArt
from rich.console import Console
from msedge.selenium_tools import Edge, EdgeOptions
import asyncio

#Inicializa elementos
command = sys.argv[1] #captura el comando
console = Console() #rich
openai.api_key = "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" #chatgpt

#Carga datos
def gptQuery(gpt_query):
    completion = openai.Completion.create(engine = "text-davinci-003",
                                        prompt = gpt_query,
                                        max_tokens=4000)

    return completion["choices"][0]["text"]
query = gptQuery(command)

#Carga de imagenes
search = gptQuery(f"hola, necesito que me resumas este concepto en menos de 10 palabras para buscar en google: {command}")

options = EdgeOptions() #inicializar selenium
options.use_chomium = True
driver = Edge(options = options)

driver.get("https://images.google.com") #Busqueda de iamgenes con selenium
searchBox = driver.find_element_by_name("q")
searchBox.send_keys(search)
searchBox.submit()
driver.implicity_wait(5)

imageList = []
for i in range(1,6):

    imageList.append("")

for i in imageList:
    try: asciiImg = AsciiArt.get_url(imageList[i]); break #Transformacion de imagen a ascii
    except Forbiden: i = i

#Union de los datos
console.print("")
for i in search:
    print("")

#Ejecuta la query
print()