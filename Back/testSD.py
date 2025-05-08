from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver.exe', options=options)

# Ouvrir Pokémon Showdown
driver.get("https://play.pokemonshowdown.com")

# Attendre que la page charge complètement
time.sleep(5)

# Vérifier si tu es connecté à ton compte Google (exemple en cherchant une icône de profil)
try:
    profile_icon = driver.find_element(By.XPATH, "//img[@alt='Profile']")
    print("Connexion réussie à ton compte Google !")
except:
    print("Impossible de trouver l'icône de profil. Tu n'es peut-être pas connecté.")

# Garde la fenêtre ouverte
input("Appuie sur Entrée pour quitter...")
driver.quit()
