class Akinator:
    def __init__(self):
        self.categories = {
            "un Deportista": [
                {"name": "Cristiano Ronaldo", "questions": ["¿Juega fútbol?", "¿Juega en el Al Nassr en Arabia?", "¿Su frase célebre es '¡Siiuuu!'?"]},
                {"name": "Messi", "questions": ["¿Juega fútbol?", "¿Es argentino?", "¿Jugó para el Barcelona?", "¿Es el actual campeón del mundo?"]},
                {"name": "Chicharito", "questions": ["¿Juega fútbol?", "¿Inició su carrera en el equipo de Chivas?", "¿Es el máximo goleador de la selección mexicana?"]},
                {"name": "Checo Pérez", "questions": ["¿Participa en la Fórmula 1 como conductor?", "¿Es mexicano?", "¿Nació en Guadalajara?"]},
            ],
            "un Superhéroe": [
                {"name": "Spider-Man", "questions": ["¿Una picadura de araña le dió superpoderes?", "¿Es conocido por su sentido arácnido?"]},
                {"name": "Batman", "questions": ["¿Es millonario?", "¿Lucha contra el crimen en Gotham City?", "¿Conduce un batimovil?"]},
                {"name": "La Mole", "questions": ["¿Es parte de los Cuatro Fantásticos de Marvel?", "¿Está hecho de roca?"]},
                {"name": "Doctor Strange", "questions": ["¿Es el Hechicero Supremo de Marvel?", "¿Lleva consigo objetos místicos como el Ojo de Agamotto, la Capa de Levitación y el Libro de Vishanti?"]},
            ],
            "una Caricatura": [
                {"name": "Wanda", "questions": ["¿Aparece en Los Padrinos Mágicos?", "¿Puede levitar?", "¿Tiene el pelo rosa?"]},
                {"name": "Cosmo", "questions": ["¿Aparece en Los Padrinos Mágicos?", "¿Puede levitar?", "¿Tiene el pelo verde?"]},
                {"name": "Comegalletas", "questions": ["¿Aparece en Plaza Sésamo?", "¿Le encanta comer galletas?"]},
                {"name": "Bambi", "questions": ["¿Es un personaje de una película de Disney?", "¿Es un venado?", "¿Su madre muere en la película?"]},
                {"name": "Calamardo", "questions": ["¿Aparece en Bob Esponja?", "¿Es un calamar?", "¿Tocaba el clarinete?"]},
                {"name": "Mamá Coco", "questions": ["¿Aparece en una película de Disney?", "¿Es una viejita?", "¿Muere al final de la película?"]},
                {"name": "Miguel Coco", "questions": ["¿Aparece en una película de Disney?", "¿Es un niño?", "¿Toca la guitarra?"]},
                {"name": "Mulan", "questions": ["¿Es un personaje de Disney?", "¿Es una mujer?", "¿Se hizo pasar por hombre para unirse al ejército?"]},
                {"name": "Andy", "questions": ["¿Es un personaje humano de las películas de Pixar?", "¿Sus dos juguetes favoritos son un vaquero y un astronauta?"]},
                {"name": "Patricio Estrella", "questions": ["¿Es una estrella de mar?", "¿Aparece en Bob Esponja?", "¿Es de color rosa?"]},
            ],
            "de un Videojuego": [
                {"name": "Yoshi", "questions": ["¿Es un dinosaurio verde?", "¿Es la mascota de Mario (Nintendo)?", "¿Es tierno y juguetón?"]},
                {"name": "Kratos", "questions": ["¿Pertenece a Santa Monica Studios de Playstation?", "¿Es el dios de la guerra?", "¿Acabó con todo el Olimpo?"]},
                {"name": "Leon S. Kennedy", "questions": ["¿Pertenece a Capcom?", "¿Comenzó su carrera como policía en Racoon City?", "¿Ha enfrentado horrores de la saga Resident Evil?"]},
                {"name": "Mario Bros", "questions": ["¿Es el ícono de Nintendo?", "¿Es un fontanero?", "¿Es de origen italiano?"]},
                {"name": "Wario", "questions": ["¿Es el villano de Mario (Nintendo)?", "¿Su traje es amarillo?", "¿Es conocido por su avaricia y personalidad excéntrica?"]},
                {"name": "Sonic", "questions": ["¿Es un erizo de color azul?", "¿Corre a velocidades supersónicas?", "¿Es la mascota de SEGA?"]},
                {"name": "Dinosaurio de Google", "questions": ["¿Lo juegas cuando se va internet en un navegador de Google?", "¿Es un minijuego de saltar obstáculos y esquivar cactus?"]},
                {"name": "Lueyna Kushinada", "questions": ["¿Es de la ciudad de Night City en el videojuego Cyberpunk?", "¿Es un personaje jugable en Cyberpunk 2077?"]},
                {"name": "El Penitente", "questions": ["¿Es un personaje de Blasphemous?", "¿Tiene un papel fundamental en la historia del juego?"]},
                {"name": "Ezio", "questions": ["¿Pertenece a la saga de Assassin's Creed?", "¿Es un noble italiano del siglo XV?", "¿Sus habilidades incluyen el uso de hojas ocultas, la escalada libre, la lucha con espadas y técnicas de sigilo?"]},
            ],
            "de un Ánime": [
                {"name": "Gohan", "questions": ["¿Aparece en Dragon Ball?", "¿Es el hijo de Goku?"]},
                {"name": "Goku", "questions": ["¿Fue enviado a la Tierra cuando era un bebé?", "¿Aparece en Dragon Ball?", "¿Fue entrenado por el Maestro Roshi?"]},
                {"name": "Naruto", "questions": ["¿Pertenece a la Aldea de la Hoja?", "¿Quiere convertirse en Hokage?", "¿Viste un traje naranja con blanco?"]},
                {"name": "Luffy", "questions": ["¿Proviene del pueblo Foosha en el East Blue?", "¿Es el protagonista de One Piece?", "¿Su mayor deseo es convertirse en el Rey de los Piratas?"]},
                {"name": "Seiya", "questions": ["¿Es un Caballero del Zodiaco?", "¿Lleva la Armadura de Pegaso?", "¿Domina técnicas de combate conocidas como 'Cosmo' y 'Poderes de Pegaso'?"]},
            ],
            "Cantante/Músico": [
                {"name": "Michael Jackson", "questions": ["¿Es conocido como el Rey del Pop?", "¿Cambió su tonalidad de piel a lo largo de su vida debido a una enfermedad en la piel?", "¿Es famoso por álbumes como 'Thriller' y 'Bad'?"]},
                {"name": "Freddie Mercury", "questions": ["¿Su canción más popular es We will rock you?", "¿Fue el líder de la banda Queen?", "¿Murió a causa del SIDA?"]},
                {"name": "Luis Miguel", "questions": ["¿Es conocido como 'El Sol de México'?", "¿Una de sus canciones más populares es La chica del vikini azul?"]},
                {"name": "Junior H", "questions": ["¿Toca música perteneciente al género 'corridos tumbados'?", "¿Uno de sus álbumes se titula 'Atrapado en un sueño'?"]}
            ],
            "Histórico": [
                {"name": "Napoleón", "questions": ["¿Era francés?", "¿Fue un emperador?", "¿Tuvo un impacto significativo en la historia europea del siglo XIX?"]},
                {"name": "Adolf Hitler", "questions": ["¿Fue una figura extremadamente controvertida de Alemania?", "¿Lideró el Partido Nazi?", "¿Fue el líder de Alemania durante la Segunda Guerra Mundial?"]},
                {"name": "Juan Escutia", "questions": ["¿Fue un niño héroe?", "¿Tuvo un papel importante en la defensa del Castillo de Chapultepec durante la Guerra México-Estados Unidos?"]},
                {"name": "Leonardo da Vinci", "questions": ["¿Fue un pintor famoso del Renacimiento?", "¿Pintó obras icónicas como 'La Última Cena' y 'La Mona Lisa'?"]},
                {"name": "AMLO", "questions": ["¿Es una figura política mexicana?", "¿Es el actual presidente de México?"]},
                {"name": "Colosio", "questions": ["¿Fue asesinado poco después de tomar su cargo como gobernador de Sonora?", "¿Fue candidato a la presidencia de México en 1994?"]},
            ],
            "una Celebridad": [
                {"name": "Franco Escamilla", "questions": ["¿Es comediante?", "¿Es miembro del grupo 'La Diablo Squad'?", "¿Su esposa se llama Gaby?"]},
                {"name": "Mr. Beast", "questions": ["¿Se dedica a YouTube?", "¿Es conocido por tener uno de los canales con más suscriptores en el mundo?"]},
                {"name": "Triple H", "questions": ["¿Es un luchador profesional?", "¿Ha competido en la WWE (World Wrestling Entertainment)?", "¿Su nombre es Paul Levesque?"]},
                {"name": "La Mole (Iván Femat)", "questions": ["¿Es comediante?", "¿Es miembro del podcast 'Hermanos de Leche'?", "¿También forma parte del podcast 'Amos del Universo'?"]},
            ],
            "un Meme ó Mascota de marcas": [
                {"name": "Cheems", "questions": ["¿Es un perro?", "¿Es conocido por su expresión facial en memes humorísticos?", "¿Recientemente murió?"]},
                {"name": "Dr. Simi", "questions": ["¿Pertenece a una marca de medicina (Farmacias similares)?", "¿Es un personaje que realiza bailes en su publicidad generalmente en una botarga de doctor?"]},
                {"name": "Tigre Toño", "questions": ["¿Promociona un cereal?", "¿Es un personaje de mascota de una marca de cereal azucarado?", "¿Esta mascota es un tigre?"]},
            ],
            "un Demonio": [
                {"name": "Beelzebub", "questions": ["¿Es un ente demoníaco conocido como el señor de las moscas?", "¿Según algunos textos demonológicos es conocido como uno de los siete príncipes del infierno?"]},
                {"name": "Lucifugio", "questions": ["¿Es ampliamente conocido como una figura demoníaca?", "¿Se le atribuye el título de 'Rey de los Demonios'?"]},
            ],
        }

    def guess_character(self):
        print()
        print("Piensa en un personaje y responde las siguientes preguntas con 's' para sí y 'n' para no:")
        print("A continuación se muestran todos los personajes disponibles a adivinar:")
        print()
        print("CR7, Messi, Chicharito, Checo Perez, Spider-Man, Batman, La Mole, Doctor Strange, Wanda, Cosmo, Comegalletas, Bambi, Calamardo, Mama Coco, Miguel Coco, Mulan, Andy, Patricio, Yoshi, Kratos, Leon S. Kennedy, Mario Bros, Wario, Sonic, Dinosaurio de Google, LUEYNA KUSHINADA, El penitente, Etzio, Gohan, Goku, Naruto, Luffy, Seiya, Michael Jackson, Freddie Mercury, Luis Miguel, Junior H, Napoleon, Hitler, Juan Escutia, Da Vinci, Franco Escamilla, Mr. Beast, AMLO, Colosio, Triple H, La Mote (Iván Femat), Cheems, Dr. Simi, Tigre Toño, Beelzebub, Lucifugio")
        print()
        
        play_again = 's'

        while play_again == 's':
            for category, category_characters in self.categories.items():
                print(f"¿Tu personaje es {category}?")
                response = self.get_valid_response("¿Sí o no? (s/n): ")
                if response == 's':
                    self.guess_character_in_category(category_characters)

            play_again = self.get_valid_response("¿Quieres jugar de nuevo? (s/n): ")

    def guess_character_in_category(self, category_characters):
        print("Excelente, tu personaje está en esta categoría.")
        print()
        for character in category_characters:
            correct_guess = True
            for question in character["questions"]:
                response = self.get_valid_response(question + " (s/n): ")
                if response != 's':
                    correct_guess = False
                    break
            if correct_guess:
                guess = self.get_valid_response(f"¿Se trata de {character['name']}? (s/n): ")
                if guess == 's':
                    print(f"Tu personaje es: {character['name']}!")
                    print()
                    print("Prueba con otra categoria")
                    return
                else:
                    print(f"Incorrecto. El personaje correcto era {character['name']}.")
                    return

        print("No has adivinado ningún personaje en esta categoría.")
        return

    def get_valid_response(self, prompt):
        while True:
            response = input(prompt).strip().lower()
            if response == 's' or response == 'n':
                return response
            else:
                print("Por favor, ingresa 's' para sí o 'n' para no.")

if __name__ == "__main__":
    akinator = Akinator()
    akinator.guess_character()