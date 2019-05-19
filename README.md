## Tennis_probability_project ##
# Credits #
Sofiya Romanchuk and Danylo Nazaruk 
# Description #
Tennis_probability_project is a course work from the course "Programming fundamentals". 
The theme of this project is "Probability of winning of certain player in given tennis match". You can find more information on wiki. Our project is now finished. Its idea is to create the neural network to calculate the probability of the winning of particular tennis player against his opponent in tennis match.
In the Wiki you are able to find all the stages of my project. And the last, fifth one will end on 12.05.2019. There you could also find weekly reports. All the information in Wiki is in Ukrainian.
In the 1 stage you could find the theme, system requirements, description of this course work, description of the functionality of the API and the weekly reports.
In the 2 stage you could find functional system requirements, non-functional system requirements, description of the input data, description of the capabilities of modules, module packages, libraries that will be used to work with data in the program, description of the organization of group work on the project.
### Призначення та коротка характеристика програми ###
Ця програма призначена для визначення імовірного переможця тенісного матчу за заданими користувачем параметрами. 

Вхідні дані програми: ім'я першого тенісного гравця, ім'я другого тенісного гравця, тип корту та стать обох гравців. Вибір тенісиста/тенісистки обмежується рейтингом топ 501 ATP для чоловіків та топ 500 WTA для жінок. 4 типи корту на вибір - outdoor hard, indoor hard, clay, grass. Статі - female/male.

Вихідні дані: ім'я першого тенісиста, вирахуваний шанс його перемоги, ім'я другого тенісиста та тип корту, на якому повинен бути проведенй матч.

Користувач отримує інформацію про те, хто ж імовірно із двох попередньо введених тенісистів буде переможцем тенісного матчу. 

### Коротка інструкція по користуванню програмою ###
Потрібно відкрити пакет web_app та відкрити файл web_app.py. Потім натиснути run і ви побачите посилання. Перейшовши за ним здійснюйте наступні кроки:

  1 крок: вибрати із 2 поточних заданих варіантів 1 для статі - female/male. 
  
  2 крок: вибрати 1 тип корту із 4 попередньо-заданих нами, на якому повинен бути проведений турнір - outdoor hard/indoor hard/clay/grass.
  
  3 крок: ввести ім'я першого тенісного гравця - Вам знову ж таки допоможе список, який автоматично шукатиме збіжності за першимим ж символами. Пам'ятайте - гравець повинен відповідати тій статі, яку ви обрали попередньо(це можна завжди змінити).
  
  4 крок: ввести ім'я другого тенісного гравця - подальші інструкції ті ж самі, що і в 3 кроці. Проте пам'ятайте, що не можна обирати того самого гравця двічі.
  
  5 крок: натиснути кнопку "Calculate probability".
  
  6 крок: якщо всі попередні кроки були реалізовані, то на екрані вашого пристрою буде висвітлена наступна сторінка із результатом.
  
### Опис тестових прикладів для первірки працездатності програми. ###
* Перше вікно

![first_window_example](https://user-images.githubusercontent.com/47135579/57972131-38ba3880-799f-11e9-84ef-8fc3d1c02468.png)

* Друге вікно(виведений результат неробочий, це лише приклад)

![second_window_example](https://user-images.githubusercontent.com/47135579/57972137-466fbe00-799f-11e9-8864-d17678529116.png)

### Структура програми з коротким описом модулів, функцій, класів та методів. ###
Модуль neural_network.py

Цей модуль представляє собою реалізацію нейронної мережі. Він знаходиться у пакеті neural_network. Для тренування нейронної мережі ми використовуємо файли men_dataset.csv та women_dataset.csv. За допомогою них створюються збережені моделі men_tennis.h5 та women_tennis.h5. Модель, що використовується для передбачення, обирається відповідно до статі гравців.

Модуль data_processing.py

Цей модуль є досить великим і він складає основну базу нашої програми. У ньому ми опрацьовуємо всю інформацію надану нам Sportradar API. Знаходиться у пакеті modules.
* get_json(source) - повертає json словники за ссилкою;
* matches_from_tournaments(file) - повертає id матчів різних турнірів;
* player_profile(id, rankings_path) - повертає потрібну інформацію про тенісистів;
* surface_stats(data) - повертає відсоток виграшів на різних типах кортів;
* rank(id, rankings) - повертає рейтинги тенісистів;
* previous_encounters(id1, id2, date) - вираховує відсоток перемог в попередніх матчах тих самих гравців що відбувались до заданої дати;
* rankings(gender) - повертає список із рейтингами;
* tournaments(file, gender) - повертає список із турнірами. 

Модуль process_match.py

Цей модуль був створений для того, щоб перетворити введені на сайті на такі, що зможе сприймати нейронна мережа. Знаходиться у пакеті modules.
* preprocess(player1, player2, type, gender) - обробляє дані отримані з веб застосунку;
* predict_match(ranking, surface, previous, gender) - передбачає результат матчу;
* process_match(player1, player2, type, gender) - обробляє дані та передбачає результат матчу.

Модуль MatchesADT.py

Цей модуль містить абстрактний клас Matches. Це є клас на основі АТД стек, у нього заносяться id матчів. Методи: **add** - додає новий елемент до стеку; **pop** - видаляє та повертає елемент зі стеку; **is_empty** - повертає булевий вираз, в залежності від того чи стек пустий; **__len__** - повертає довжину стеку; **process_match**- працює із останнім елементом у стеку і повертає список із цих елементів: player id, name, player id, name, match id, ranking, surface performance, previous matches agains same opponent; **from_file** - добавляє у стек id з вказаного файлу; **process_and_write** - обробляє всі id зі стеку та записує у вказаний файл.
