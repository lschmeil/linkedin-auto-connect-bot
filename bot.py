import time
import json
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

cookies_file = "cookies.json"
registro_file = "enviados.json"
limite_convites = 20

mensagens = [
    "Oi {nome}, tudo bem? Sou Lucas, dev júnior de 17 anos. Quero muito me conectar com você para trocar experiências e aprender mais sobre tecnologia!",
    "Olá {nome}! Sou Lucas, dev júnior de 17 anos. Estou começando na área e seria ótimo ter você na minha rede.",
    "Hey {nome}, tenho 17 anos e estou iniciando como dev júnior. Seria incrível poder aprender com você!",
    "Prazer {nome}! Sou Lucas, dev júnior de 17 anos. Vamos nos conectar e compartilhar conhecimento?"
]

# carregar registro
try:
    with open(registro_file, "r") as f:
        enviados = json.load(f)
except:
    enviados = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com")
time.sleep(3)

# login com cookies
with open(cookies_file, "r") as f:
    cookies = json.load(f)
for cookie in cookies:
    try:
        driver.add_cookie(cookie)
    except:
        pass

driver.get("https://www.linkedin.com/feed/")
time.sleep(3)
print("✅ Login automático feito com cookies")

# busca
driver.get("https://www.linkedin.com/search/results/people/?keywords=desenvolvedor")
time.sleep(4)

# scroll infinito
def rolar_infinito(max_scrolls=10):
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(max_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

rolar_infinito()

# pegar links de perfis
links = driver.find_elements(By.XPATH, "//a[contains(@href,'/in/')]")
links = [l.get_attribute("href") for l in links]
print(f"🔗 Perfis coletados: {len(links)}")

convites = 0

for link in links:
    if convites >= limite_convites:
        break

    driver.get(link)
    time.sleep(3)

    try:
        # procurar botão conectar
        botoes = driver.find_elements(By.XPATH, "//button")
        botao_conectar = None
        for b in botoes:
            texto = b.text.lower().strip()
            if "conectar" in texto or "connect" in texto:
                botao_conectar = b
                break

        if not botao_conectar:
            print("⚠ Este perfil não tem opção de Conectar, pulando...")
            continue

        botao_conectar.click()
        time.sleep(2)

        # abrir campo de nota
        try:
            nota_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label,'Adicionar nota')]")
            nota_btn.click()
            time.sleep(1)
        except:
            print("⚠ Não tem opção de nota, pulando...")
            driver.find_element(By.XPATH, "//button[contains(., 'Fechar')]").click()
            continue

        # nome do perfil
        try:
            nome_el = driver.find_element(By.XPATH, "//h2[contains(@class,'artdeco-modal__header')]")
            nome = nome_el.text.split("\n")[0].strip()
        except:
            nome = "amigo"

        if nome in enviados:
            print(f"⚠ Já enviado → {nome}")
            driver.find_element(By.XPATH, "//button[contains(., 'Fechar')]").click()
            continue

        # mensagem personalizada
        mensagem = random.choice(mensagens).format(nome=nome)

        # localizar campo de mensagem (id ou textarea)
        try:
            campo = driver.find_element(By.ID, "custom-message")
        except:
            campo = driver.find_element(By.XPATH, "//textarea")

        campo.clear()
        campo.send_keys(mensagem)
        time.sleep(1)

        # botão enviar
        botoes_modal = driver.find_elements(By.XPATH, "//div[contains(@class,'artdeco-modal')]//button")
        botao_confirmar = None
        for b in botoes_modal:
            texto = b.text.lower().strip()
            if "enviar" in texto or "send" in texto or "conectar" in texto:
                botao_confirmar = b
                break

        if botao_confirmar:
            botao_confirmar.click()
            print(f"✅ Convite enviado para: {nome}")
            enviados.append(nome)
            convites += 1
            with open(registro_file, "w") as f:
                json.dump(enviados, f, indent=4)
            time.sleep(2)
        else:
            print(f"⚠ Não achei botão de enviar para {nome}")
            driver.find_element(By.XPATH, "//button[contains(., 'Fechar')]").click()

    except Exception as e:
        print("Erro:", e)
        try:
            driver.find_element(By.XPATH, "//button[contains(., 'Fechar')]").click()
        except:
            pass
        continue

print("\n----------------------")
print(f"🎉 FINALIZADO — Convites enviados: {convites}")
print("----------------------")

input("Pressione ENTER para fechar...")
driver.quit()
